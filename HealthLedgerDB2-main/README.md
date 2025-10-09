HealthLedger (Django)

Quickstart (Windows PowerShell)

1. Open PowerShell and change to the project folder that contains `manage.py`:

```powershell
cd "C:\Users\VICTUS\Downloads\HealthLedgerDB2-main\HealthLedgerDB2-main\HealthLedger"
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
# Activate (PowerShell)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force  # only if activation is blocked by policy
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r ..\requirements.txt
```

Notes on `ibm_db` (optional)
- `ibm_db` is only needed if you plan to use `DB2Query.py` to connect to an IBM DB2 server.
- On Windows, installing `ibm_db` may require the IBM Data Server Runtime client or Visual C++ Build Tools. See https://pypi.org/project/ibm_db/ for platform-specific guidance.

4. Apply Django migrations and run the dev server:

```powershell
python manage.py migrate
python manage.py createsuperuser   # optional
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

Troubleshooting
- ModuleNotFoundError: No module named 'django' — ensure virtualenv is activated and dependencies installed.
- ibm_db install errors — consult IBM docs or skip installing `ibm_db` if you don't need DB2 connectivity.

Files of interest
- `HealthLedger/manage.py` — Django CLI entrypoint
- `HealthLedger/HealthLedger/settings.py` — Django settings (uses SQLite by default)
- `DB2Query.py` — helper to connect to DB2 with `ibm_db` (separate from Django DB)

If you'd like, I can:
- run the setup here and paste any error output,
- pin exact dependency versions into `requirements.txt`, or
- add a small script to run the server on a fixed port and open the browser automatically.
