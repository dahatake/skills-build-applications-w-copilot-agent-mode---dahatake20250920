---
mode: 'agent'
model: GPT-4.1
description: 'Update OctoFit Tracker Django app to reflect MongoDB setup, CORS config, and API root exposure.'
---

# Django App Updates

All Django project files are in the `octofit-tracker/backend/octofit_tracker` directory.

## Required Changes

1. Update `settings.py` for MongoDB (`djongo`) connection and full CORS allowance (development):
   - Database `octofit_db`
   - `ENGINE = djongo`
   - Allow all hosts and CORS origins
2. Update / verify the app layer files to support the following collections/entities:
   - `users`, `teams`, `activities`, `leaderboard`, `workouts`
   - Files to review/update: `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py`, `admin.py`
3. Ensure the root path `/` points to the API and an `api_root` is present/returned in `urls.py` so that hitting `/` (or `/api/`) provides a discoverable entry (e.g. DRF router or custom API root view).

## Acceptance Criteria
- MongoDB configuration active (no sqlite fallback)
- CORS fully enabled for development
- CRUD endpoints available for all five collections
- Root `/` returns API entry (links or simple JSON) and does not 404
- Tests scaffold (even minimal) referencing the main viewsets

## Notes
- Do not create a new virtual environment; reuse `octofit-tracker/backend/venv`.
- Use Django REST Framework viewsets & router for consistency.
- Keep changes focused; no production hardening yet.
