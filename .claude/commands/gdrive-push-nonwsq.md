---
description: Push this NON-WSQ course's courseware (slide deck PPT + PDF, Learner Guide, Lesson Plan, labs) to the user-provided Google Drive course folder — auto-creating each folder's archive/ and moving superseded versions into it, never deleting, and emitting anyone-with-link viewer links. No assessment is ever uploaded.
argument-hint: <google-drive-course-folder-link>
---

# /gdrive-push-nonwsq — push NON-WSQ courseware to Google Drive

Push this non-WSQ course repo's current courseware to the user's Google Drive course folder. Superseded Drive copies are **moved to `archive/`** (only when the file actually changed); unchanged files are skipped; **nothing on Drive is ever deleted**.

**Folder link (required, user-supplied):** `$ARGUMENTS`

## HARD RULES

1. **Never push without the user's folder link.** If `$ARGUMENTS` is empty or is not a Drive folder link/ID, **ask (AskUserQuestion) and stop** until it is given. Never fall back to a default or remembered folder. Unlike the WSQ flow there is **no LMS Courseware-Link cross-check** to catch a wrong folder — non-WSQ courses aren't tracked on LMS-TMS — so the explicit link is the only safeguard. The link is `https://drive.google.com/drive/folders/<FOLDER_ID>` — any `/u/N/` only selects a browser profile and is **not** part of the ID.
2. **Never upload an assessment.** A non-WSQ course has **no assessment**. If an `assessment/` folder exists locally the script reports it and skips it — do not work around this.
3. **QA must pass first.** Run the prohibited-content scan. **Do not push on a failing scan** — stop, report, fix, re-scan:
   ```bash
   python3 ~/.claude/skills/non-wsq-courseware-qa/scan_prohibited.py .
   ```
4. **Push the current build.** Drive stores only *links*, so whatever lands there is what learners get. Build the PPT/LG/LP **PDFs** first:
   ```bash
   bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
   ```
5. **Dry-run first, always.** Show the plan, then push for real.
6. **Never delete on Drive.** Superseded files are *moved* into each folder's lowercase `archive/` subfolder.

## Transport — rclone, not the MCP connector

The Google Drive **MCP connector cannot move or delete files**, so it cannot archive-and-replace — it would only pile up duplicates. Use **rclone**, which supports server-side move, MD5 change-detection (`--checksum`) and folder scoping (`--drive-root-folder-id`). The MCP connector may still be used read-only to verify.

One-time setup if missing: `brew install rclone`, then `rclone config create gdrive drive scope=drive` and complete the Google sign-in **as the account that owns (or has Editor on) the destination folder**.

## The archive convention (created automatically)

Each destination folder gets a lowercase **`archive/`** subfolder, **created automatically on first push** — you never need to make it by hand. Before new files are uploaded, every pre-existing file that is not identical to one being pushed is moved into it server-side.

Handled automatically as well: an `Archive`/`archives` variant is renamed to the canonical lowercase `archive`; an `old versions/`-style folder is merged into `archive/` and the emptied folder removed; and — under `--mirror` only — changed or removed lab files are moved to `Activities/archive/` by rclone's `--backup-dir`. The additive default never archives anything in Activities.

**rclone will not archive into a subfolder of the destination** — `--backup-dir` inside the destination fails with *"destination and parameter to --backup-dir mustn't overlap"*. So the script archives each superseded file with an explicit `moveto` **first**, then uploads. Do not reach for `--backup-dir` for the courseware folders.

Watch for folder names with a **trailing space** — quote every remote path.

## Steps

1. **Sweep local junk** so it can't be pushed:
   ```bash
   find . -name ".DS_Store" -type f -delete
   find . -name '~$*'       -type f -delete   # Word/PowerPoint lock files
   ```
2. **Run the pusher** from the course repo root — the script lives in `.claude/scripts/` (project) or `~/.claude/skills/gdrive-push-nonwsq/`:
   ```bash
   python3 <scripts-dir>/gdrive_push_nonwsq.py "<folder-link>" --dry-run   # preview — always
   python3 <scripts-dir>/gdrive_push_nonwsq.py "<folder-link>"             # real push
   ```
3. **Show the dry-run plan** per Drive folder — Trainer Slides / Learner Slides / Learner Guide / Lesson Plan / Activities — naming what is archived, what is uploaded, and what is skipped as unchanged. Then do the real push.
4. **Report** per folder: files archived → `archive/`, files uploaded, and each file's **anyone-with-link viewer link**.

## What goes where

| Drive folder | Contents |
|---|---|
| Trainer Slides | the slide deck **PPT** |
| Learner Slides | the slide deck **PDF** |
| Learner Guide | the **LG** DOCX + PDF |
| Lesson Plan | the **LP** DOCX + PDF |
| Activities | the **`labs/`** tree — **additive**, see below |

A `Trainer Resources` folder, if present, is left untouched — the trainer manages it by hand.

**Activities is additive.** That folder also holds the trainer's working material — Excel datasets and `.xlsx` templates with no counterpart in the repo — so labs are pushed with `rclone copy`: lab files are uploaded and updated, and everything else is left in place. A mirroring sync would archive all of it on the first push. Pass `--mirror` when you really do want Activities to match `labs/` exactly (extras move to `Activities/archive/`, never deleted); the cost of the default is that a locally deleted lab lingers on Drive until you mirror or remove it.

There is deliberately **no Assessment row**: non-WSQ courses have no assessment, so there is nothing to upload and no answer key to protect.

## Then

Nothing further. Unlike the WSQ flow there is no `/tms-push` step — non-WSQ courses are not tracked on lms-tms.tertiaryinfotech.com, so the emitted links are for the trainer to share directly.
