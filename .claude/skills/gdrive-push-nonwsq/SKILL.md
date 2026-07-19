---
name: gdrive-push-nonwsq
description: Push a NON-WSQ course's courseware (slide deck PPT + PDF, Learner Guide, Lesson Plan, labs) to the user-supplied Google Drive course folder — auto-creating each folder's archive/ subfolder and moving superseded versions into it, never deleting, then emitting anyone-with-link viewer links. No assessment is ever uploaded.
---

# gdrive-push-nonwsq — push NON-WSQ courseware to Google Drive

The non-WSQ sibling of `gdrive-push`. Same transport and archive discipline, with the
WSQ funding/compliance layer removed.

## How it differs from the WSQ version

| | WSQ (`gdrive-push`) | Non-WSQ (this skill) |
|---|---|---|
| Destination | Resolved from the LMS **Courseware Link** by TGS code | **Always** user-supplied on the command line |
| Assessment | Uploads all four DOCX (papers + answer keys) | **Never** — a non-WSQ course has no assessment |
| Deck PPT | `Master Trainer Slides` | `Trainer Slides` |
| Deck PDF | `Learner Guide` (alongside the LG) | `Learner Slides` (its own folder) |
| Follow-up | `/tms-push` writes links to the LMS | none — links are for the trainer/learners |

There is no LMS lookup because non-WSQ courses aren't tracked there, which means there
is also no safety net matching the folder to a course code. **The link must therefore be
explicit every time** — the script refuses to run without one rather than guessing.

## Folder routing

Folders are matched case-insensitively under the given root and **created if missing**:

| Drive folder | Contents |
|---|---|
| Trainer Slides | the slide deck **`.pptx`** |
| Learner Slides | the slide deck **`.pdf`** |
| Learner Guide | **LG** `.docx` + `.pdf` |
| Lesson Plan | **LP** `.docx` + `.pdf` |
| Activities | the **`labs/`** tree (additive — see below) |

A `Trainer Resources` folder is left untouched — it holds material the trainer manages
by hand, not build output.

### Activities is ADDITIVE, deliberately

Activities is where the **trainer's working material** lives — Excel datasets
(`SPCdata.xls`, `ProcessCapability.xls`) and `.xlsx` templates (Process FMEA, Pugh
Matrix, Control Plan) that have no counterpart in the repo. A mirroring `rclone sync`
would sweep every one of them into `archive/` on the first push.

So labs are pushed with `rclone copy`: lab files are uploaded and updated, and
**anything else already in Activities is left alone**. Pass `--mirror` to opt into the
old behaviour when you genuinely want Drive to match `labs/` exactly (extras are then
moved to `Activities/archive/`, never deleted).

The trade-off: a lab file deleted locally keeps existing on Drive. Use `--mirror` — or
remove it by hand — when a lab is retired.

## The archive convention (automatic)

Every folder gets a lowercase **`archive/`** subfolder, created automatically on first
push. Before new files land, every pre-existing file that isn't identical to one being
pushed is **moved server-side** into it. Nothing on Drive is ever deleted.

Also handled automatically:
- an `Archive` / `archives` variant is renamed to the canonical lowercase `archive`;
- an `old versions/`-style folder is merged into `archive/` and the empty folder removed;
- for `labs/`, this applies only under `--mirror` (changed/removed files move to
  `Activities/archive/` via rclone's `--backup-dir`); the additive default archives nothing.

Note that rclone **cannot** use `--backup-dir` pointing inside the destination
("destination and parameter to --backup-dir mustn't overlap"), which is why files are
archived with an explicit `moveto` **before** the upload rather than in one pass.

## Transport — rclone, not the MCP connector

The Google Drive **MCP connector cannot move or delete files**, so it cannot
archive-and-replace — it would only pile up duplicates. `rclone` supports server-side
move, MD5 change detection and folder scoping via `--drive-root-folder-id`.

One-time setup if missing:

```bash
brew install rclone
rclone config create gdrive drive scope=drive
```

Sign in as the account that **owns or has Editor on** the destination folder.

## Steps

1. **Sweep local junk** so it can't be pushed:
   ```bash
   find . -name ".DS_Store" -type f -delete
   find . -name '~$*'       -type f -delete   # Word/PowerPoint lock files
   ```
2. **Build first** — Drive holds only links, so what lands there is what learners get:
   ```bash
   bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
   ```
3. **QA must pass** — run the prohibited-content scan; do not push on a failure:
   ```bash
   python3 ~/.claude/skills/non-wsq-courseware-qa/scan_prohibited.py .
   ```
4. **Dry run, then push:**
   ```bash
   python3 <scripts-dir>/gdrive_push_nonwsq.py "<folder-link>" --dry-run
   python3 <scripts-dir>/gdrive_push_nonwsq.py "<folder-link>"
   ```
5. **Report** per folder: what was archived, uploaded, or skipped as unchanged, plus each
   file's anyone-with-link viewer link.

Change detection is by MD5 — unchanged files are skipped entirely, so re-running the
push is cheap and won't churn the archive.

## Flags

- `--dry-run` — print the plan; touch nothing.
- `--repo DIR` — course repo root (default: current directory).
- `--links-only` — re-emit the link block for what's already on Drive, uploading nothing.
- `--mirror` — make Activities match `labs/` exactly, archiving anything else it holds.
  Off by default so trainer datasets/templates are never swept away.
