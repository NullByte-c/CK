# Cookie Clicker Python background module

This module sends a Discord webhook message when the app opens, every 10
iterations, and on a normal shutdown.

## Setup

1. Copy `config.example.py` to `config.py`.
2. Put a newly generated Discord webhook URL in `config.py`.
3. Install `requests` in the Python environment used by the app.

Do not commit `config.py`. The repository ignores it via `.gitignore`.

`run_once()` is intended to be called by the Android Java worker once per
iteration. If that worker calls it once per second, periodic messages are sent
about every 10 seconds.

`shutdown()` sends OFFLINE only when it is called during a normal shutdown.
Android force-stops, crashes, or process termination cannot reliably run it.
