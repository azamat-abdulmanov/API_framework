# API Framework

This API framework utilizes `pytest` for testing and `Allure` for reporting. It provides a structured way to run automated tests and generate detailed reports.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Start Test](#start-test)
- [Open in Default Browser](#open-in-default-browser)
- [Logging](#logging)
- [Project Structure](#project-structure)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/api_framework.git
   cd api_framework
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Allure**:
   - You can install Allure using Scoop:
     ```bash
     scoop install allure
     ```

## Usage

### Start Test

To run the tests, use the following command:

```bash
python pytest_run.py
```

### Open in Default Browser

You can generate Allure reports and open them in your default browser using the following command:

```bash
python pytest_run.py --open
```

### Logging

Logging levels can be adjusted using the `--log_level` argument. For example:

```bash
python pytest_run.py --log_level DEBUG
```
