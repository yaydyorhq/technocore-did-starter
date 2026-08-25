# Technocore DID Starter

Read `AGENTS.md` before changing this repository; it is the authoritative contributor guidance. In brief, this is a small Python CLI centered on `technocore_agent.py`, with a pinned conditional `cryptography` dependency in `requirements.txt` and standard-library tests under `tests/`.

Use Python 3.12 where available, a local `.venv`, and `python -m pip install -r requirements.txt`. Offline validation is `python -m unittest discover -s tests -v`, `python -m py_compile technocore_agent.py`, `python technocore_agent.py --version`, and `python technocore_agent.py --help`. Exercise network commands only deliberately against an approved endpoint; do not publish or send external requests during repository maintenance.

Do not create, overwrite, expose, or commit `identity.pem` (or any private key). Preserve encrypted-key safeguards, HTTPS requirements, bounded responses, timeout semantics, signed payload formats, and the existing error categories. Keep edits narrow and update `README.md` when user-facing commands or behavior change.
