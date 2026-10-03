# From Zero to CI: Building an Agentic Test Automation Framework

Workshop code for the 3-hour session (8:30–11:30 AM). Python · pytest · Playwright · Claude agents · GitHub Actions.

## Setup (do this before the session)

```bash
python --version                  # 3.10 or newer
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

Only needed from 10:25 (agents part):

```bash
export ANTHROPIC_API_KEY="sk-..."    # Windows (cmd): set ANTHROPIC_API_KEY=sk-...
```

## Checkpoint branches

Every step of the workshop has a branch. Fell behind? Jump to the next checkpoint:

```bash
git stash -u                 # put your own changes aside (get them back with: git stash pop)
git checkout step-2-ui       # jump to a checkpoint
```

| Branch | Time | What it contains |
| --- | --- | --- |
| `main` | 9:05 | Starting point: `discount.py` with a hidden bug |
| `step-1-pytest` | 9:18 | Bug fixed, unit tests (core + stretch) |
| `step-2-ui` | 9:45 | First Playwright UI tests + locked-out exercise |
| `step-3-framework` | 10:25 | Page objects, fixtures, config, pytest.ini |
| `step-4-agents` | 11:05 | Planner, generator and triage agents |
| `step-5-ci` | 11:22 | GitHub Actions workflow (final version) |
| `take-home-solution` | after | Inventory page, cart test, API test |

## Useful commands

```bash
pytest                                   # run everything
pytest -m smoke                          # only smoke tests
pytest -k errors --headed --slowmo 500   # watch matching tests in a browser
playwright codegen https://www.saucedemo.com
python agents/planner.py "Login form on saucedemo.com"
python agents/generator.py "A locked-out user should see an error"
```

Test site: https://www.saucedemo.com (users: `standard_user`, `locked_out_user`; password: `secret_sauce`).
