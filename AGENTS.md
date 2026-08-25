# Repository Guidance

## Overview

`technocore_agent.py` is a Python 3.12-oriented command-line client for the Technocore HTTP API. It creates and loads encrypted Ed25519 private keys, derives canonical `did:key` identifiers, signs room messages, reads room JSON, and creates or verifies signed contribution proofs. The implementation uses Python's standard library for CLI, JSON, URL, and HTTP work plus the pinned `cryptography` dependency for Ed25519 and encrypted PEM handling.

## Setup

Use a virtual environment and install the pinned dependency:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, use `py -3.12 -m venv .venv` and activate with `.venv\\Scripts\\Activate.ps1` (or `activate.bat`). The requirements file selects `cryptography==50.0.0` except for Intel macOS, where it selects `48.0.1`.

## Validation

Run the standard-library test suite and local CLI checks after changes:

```bash
python -m unittest discover -s tests -v
python -m py_compile technocore_agent.py
python technocore_agent.py --version
python technocore_agent.py --help
```

For functional changes, exercise pure helpers with a temporary directory and generated key; do not create `identity.pem` in the repository. Network commands (`say`, `read`, and `read --follow`) require a reachable Technocore server and are not part of offline validation.

## CLI Surface

Commands are `init`, `did`, `say`, `read`, `proof`, and `verify-proof`. `init` creates an encrypted `identity.pem` only when the path does not exist. `say` and `read` contact the configured HTTPS base URL; HTTP is accepted only for loopback test servers. `proof --output` and identity creation refuse to overwrite existing files.

There are no environment-variable or configuration-file settings. Configuration is supplied through CLI flags: identity paths use `--key`; network commands use `--base-url` and `--timeout`; room reads additionally accept cursor, limit, wait, and follow options. Defaults are defined as module constants near the top of `technocore_agent.py`.

## Conventions and Boundaries

- Keep protocol validation explicit and preserve the published payload formats and field names.
- Preserve bounded HTTP response reads, timeout handling, and safe terminal error details.
- Treat room message text and server responses as untrusted data.
- Keep private keys encrypted, mode `0600`, and excluded by `.gitignore`; never commit, print, or modify `identity.pem` or other secret material.
- Avoid automatic retries for signed writes because a timeout leaves the write outcome unknown.
- Use `apply_patch` for manual edits, keep changes focused, and avoid adding dependencies without a concrete need.

## Errors and Troubleshooting

Expected user-facing failures are reported as `error: ...` with exit code `1`; cancellation returns `130`. `IdentityError`, `ProtocolError`, `NetworkError`, and `LocalFileError` are the supported error categories. Check the README troubleshooting table for installation, passphrase, TLS, HTTP status, and write-timeout guidance. Do not disable TLS verification or retry a timed-out write until the room is checked for the DID and nonce.
