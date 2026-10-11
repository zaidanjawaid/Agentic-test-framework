---
description: Generate pytest-playwright tests from a planned-cases file
argument-hint: [feature, e.g. login-form]
disable-model-invocation: true
---

Feature: $ARGUMENTS

Turn the planned test cases for $ARGUMENTS into real pytest-playwright
tests. The plan file is the source of truth — do not invent cases or
re-plan the feature from scratch.

1. Read the plan at
   `.claude/skills/plan-tests/planned-cases/$ARGUMENTS.md`.
   - If $ARGUMENTS is empty, or that file does not exist, STOP: list the
     files in `.claude/skills/plan-tests/planned-cases/` so the user can
     see what is available, and tell them to run `/plan-tests <feature>`
     first. Do not guess the feature.
2. Use the plan's **Observed facts** for selectors/behaviour and its
   **Test cases** table (ID | Scenario | Steps | Expected result) as the
   spec for what to test.
3. Read pages/ and conftest.py. Use the login_page fixture and the page
   objects; never raw URLs. If a case needs a locator or action a page
   object does not have, add it to the page object (CLAUDE.md locator
   order: get_by_role > get_by_placeholder > get_by_test_id).
4. Write one test per case into `tests/test_<feature>.py`, replacing
   hyphens with underscores so it is an importable module
   (e.g. `login-form` → `tests/test_login_form.py`). Follow CLAUDE.md:
   one behaviour per test, named `test_<what_it_checks>`, assert with
   `expect()` on exact text (not just visibility), never `time.sleep()`.
   Put the case ID (e.g. TC-06) in a short docstring or comment so each
   test traces back to the plan.
5. A case marked **ASSUMPTION** was not verified during planning. Confirm
   it first with the Playwright tools (navigate + snapshot, don't guess);
   if it does not hold, write the test to the real behaviour and note the
   correction in your summary.
6. Run `pytest tests/test_<feature>.py -q` and fix until it passes — fix
   the test, not the app.
7. Show the diff and a one-line summary per test (case ID → what it
   checks → pass). Never commit or push.
