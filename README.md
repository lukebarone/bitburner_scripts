# Bitburner Scripts
Scripts to use inside Bitburner (in ns2 / Netscript / Javascript), or alongside (in Python3)

## Python Scripts (solvers)

- bb_mpsiat.py
- bb_sms.py
- bb_twts.py
- bb_upig1.py

### Testing / Running / Requirements

- Python3 (tested with 3.8 on WSL2 Ubuntu 20.04)
- Run doctests: `python3 -m doctest FILENAME.py` (should return no output on success)
  - Optionally, combine with the `find` command:
    ```bash
    find . -iname "*.py" -exec python3 -m doctest {} \;
    ```
- Run linter: `python3 -m pylint FILENAME.py` (all code should be rated 10/10)
  - Optionally, combine with the `find` command:
    ```bash
    find . -iname "*.py" -exec python3 -m pylint {} \;
    ```

## In-game scripts

- hackAll.ns
- sleeves.js
- stanek.js
- deepScan.ns
- spendHashes.script
- checkFulcrum.script
- blade.js

## Contributing

- Merge requests welcome if they enhance what is currently available. Please create an issue first to discuss.
- **All Python code must pass linting and have unit tests that pass!**
- Use descriptive names for variables (i.e. don't use "var" or "x" for names!)
