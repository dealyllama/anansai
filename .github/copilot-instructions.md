# anansai – Copilot Instructions

A CLI-centric AI agent toolchain built to run on local hardware (Windows/WSL/Linux) using FOSS tools and models.

## Environment

- **Target platforms**: Windows, WSL, and Linux. Code must be cross-platform compatible.
- **Python**: 3.13 in a `.venv`. Always activate before running:
  - Linux/WSL: `source .venv/bin/activate`
  - Windows: `.venv\Scripts\activate`
- **Node.js**: Available globally; `node-pty` is installed globally for PTY operations.
- **PTY on Windows**: `node-pty` handles cross-platform PTY; prefer it over Python's `pty` stdlib (Linux-only).

## Running the App

```bash
source .venv/bin/activate
python main.py
```

- `Ctrl+C` is trapped and prints a message; use `Ctrl+D` (EOFError) to exit the REPL loop.

## Dependencies

```bash
# Install / sync Python deps
pip install -r requirements.txt
```

Key libraries: `prompt_toolkit` (interactive REPL), `rich` (terminal rendering), `click` (CLI framework), `annotated-doc`, `markdown-it-py`, `Pygments`, `shellingham`.

## Architecture

`main.py` is the sole entry point — a `prompt_toolkit`-based REPL loop. The project is early-stage; the loop is the scaffold onto which CLI commands, agent tool calls, and model integrations will be layered.

Intended direction (from README): local-first, FOSS models, CLI agent toolchain.

## Conventions

- Linter: `flake8`, formatter: `black`, import sorter: `isort` (all pure-Python; configured in `.flake8` and `pyproject.toml`).
  - `flake8 .` — lint
  - `black .` — format
  - `isort .` — sort imports
- `main.py~` is an Emacs backup file — ignore it.
- New CLI commands should be encorporated in to `prompt_toolkit`.
- When adding features that require PTY subprocess management, use `node-pty` (cross-platform) — avoid Python's `pty` stdlib (Linux-only).
- Use only FOSS dependencies or alert where propriatary dependencies are needed
- Tag all generated content with #danger-will-robinson-generated-content

