# IP & Phone Tools

Small collection of scripts for inspecting IP and phone number information and for masking a machine's IP address.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Notes & Caveats](#notes--caveats)
- [Contributing](#contributing)
- [License](#license)

## Overview
This repository contains a few small Python scripts:

- `ip_mask.py` — Mask the machine's IP address by generating a random 'masked' IP.
- `my_ip.py` — Retrieve hostname and network interface IP details using `psutil`.
- `phno_info.py` — Parse a phone number and return country, carrier and timezone info using the `phonenumbers` library.
- `main.py` — A simple CLI that exposes the above functions as subcommands (see Usage).

## Requirements
- Python 3.8 or newer
- See `requirements.txt` for third-party modules used.

Dependencies used in the codebase:
- psutil
- phonenumbers

## Installation
1. Clone or copy the project to your machine.
2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Quick setup aliases (optional)

Add these alias lines to your shell (e.g., `~/.bashrc` or `~/.zshrc`) to simplify commonly-used steps:

```bash
# Setup virtualenv and run tests
alias atlassetup='bash scripts/setup_env.sh'

# Create and push a new repo from the project folder (interactive)
alias atlasupload='bash scripts/git_upload.sh'
```

Use `atlassetup` to quickly create a `.venv`, install dependencies, and run the test suite.
Use `atlasupload` to interactively create a new Git repo from this folder and push it to a remote GitHub repo.


## Usage

Each script can be run directly using Python, or you can use the central `main.py` CLI.
Run scripts directly:

```bash
python ip_mask.py
python my_ip.py
python phno_info.py "+14155552671"
```

Run the CLI (`main.py`) with subcommands:

The included modules follow underscore-style module names (`ip_mask`, `my_ip`, `phno_info`) and the repository contains the matching filenames.

Then run the CLI:

```bash
python main.py mask_ip
python main.py ip_details
python main.py phone_info "+14155552671"
```

Example output when running `python main.py ip_details`:

```
{'hostname': 'my-machine', 'ip_address': '192.168.1.100', 'network_interfaces': {...}}
```

Example output when running `python phno_info.py "+14155552671"`:

```
{'formatted_number': '+1 415-555-2671', 'country': 'United States', 'carrier': 'AT&T', 'time_zones': ['America/Los_Angeles']}
```

## Notes & Caveats
- On some Linux distributions, `socket.gethostbyname(socket.gethostname())` may return `127.0.1.1` or a loopback address. You may need to check network configurations to get the external IP.
- `ip_mask.py` simply generates a random IPv4 address for 'masking' and does not modify the real networking settings. It is purely a demonstration.
- Validate that your input phone numbers include the country code (e.g., +1 for the US) to ensure correct parsing.

## Contributing
Enhancements, bug fixes, and improvements are welcome. Please open an issue or a PR if you'd like to change behavior (for example, to actually apply system-level IP masking or to fix the `main.py` import names).

If you'd like to contribute, please follow our [Code of Conduct](./CODE_OF_CONDUCT.md) and use respectful collaboration practices. See [CONTRIBUTING.md](./CONTRIBUTING.md) for contribution instructions and PR guidelines.

## License
This project is licensed under the MIT License — see the bundled `LICENSE` file for details.
