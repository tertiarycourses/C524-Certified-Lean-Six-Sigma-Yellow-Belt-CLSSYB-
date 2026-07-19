---
description: Write this NON-WSQ course's Google Drive courseware links into its course record on the tertiarycourses.com.sg storefront admin — Trainer Slides (PPT), Learner Slides (PPT PDF), Lesson Plan, Learner Guide and the Lab/Activities folder.
argument-hint: [course-sku, e.g. C524]
---

# /lms-push-nonwsq — publish courseware links to tertiarycourses.com.sg

Write this non-WSQ course's Drive links onto its course record in the storefront
admin. Run **after** `/gdrive-push-nonwsq` — that publishes the files, this publishes
the links to them.

**Course SKU:** `$ARGUMENTS`

## HARD RULES

1. **The SKU is required.** If `$ARGUMENTS` is empty, derive it from the course repo's
   `course_data.py` (`COURSE_CODE`) and confirm it; if that is unavailable, **ask
   (AskUserQuestion) and stop**. Never guess a SKU — writing to the wrong course
   silently republishes another course's material.
2. **Push the files first.** The links are read from Drive, so run
   `/gdrive-push-nonwsq` before this. A file that isn't on Drive can't be linked.
3. **Dry-run first, always.** Show the resolved links, then write.
4. **Never write a blank over a good link.** A missing Drive file is reported and
   skipped, leaving the existing value alone.
5. **Non-WSQ only.** WSQ (TGS-) courses go to LMS-TMS via `/lms-push` and `/tms-push`
   instead — this endpoint targets the storefront catalog.

## Credentials

`TC_API_KEY` must be exported (the storefront's `X-API-Key` shared secret, Magento
config `courses/general/wsq_schedule_api_key`). Keep it in your shell profile —
**never** in a course repo, which is pushed to public GitHub.

```bash
export TC_API_KEY='…'
```

To read the live value:

```bash
docker exec ai-mms-web-1 php -r 'require_once "/var/www/html/app/Mage.php"; Mage::app();
  echo Mage::getStoreConfig("courses/general/wsq_schedule_api_key");'
```

## Steps

1. **Run the pusher** — the script lives in `.claude/scripts/` (project) or
   `~/.claude/skills/lms-push-nonwsq/`:
   ```bash
   python3 <scripts-dir>/lms_push_nonwsq.py --sku <SKU> --dry-run   # preview — always
   python3 <scripts-dir>/lms_push_nonwsq.py --sku <SKU>             # write
   ```
2. **Show the resolved links** — one line per field, naming the Drive file each came
   from — then do the real write.
3. **Report** which fields were written, which were already current, and any that
   could not be resolved on Drive.

## What goes where

| Storefront field | Source on Drive |
|---|---|
| Trainer Slides URL | the **`.pptx`** in `Trainer Slides` |
| Learner Slides URL | the **`.pdf`** in `Learner Slides` |
| Lesson Plan URL | the **`LP-*.pdf`** in `Lesson Plan` |
| Learner Guide URL | the **`LG-*.pdf`** in `Learner Guide` |
| Lab URL | the **`Activities` folder** itself, not a file inside it |

The Drive folder is read from the course's **Courseware Link** on the storefront, so
the SKU alone is enough. Pass `--drive-folder <link>` when that field is not set yet.

Only changed fields are written, so re-running on unchanged courseware reports
"nothing to write" rather than churning the record.

## Backend

The API endpoint, the `Learner Guide URL` form field and the `lab_url` column all live
in the **ai-mms** repo (`~/projects/tertiary/ai-mms`):

- `app/code/local/MMD/Courses/controllers/Api/CoursewareController.php` — the endpoint
- `migrations/611-course-courseware-lab-url.sql` — the `lab_url` column
- `app/design/adminhtml/.../dashboard/index.phtml` — the two added form fields

If the endpoint 404s, that repo has not been deployed yet.
