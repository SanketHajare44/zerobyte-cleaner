# ZeroByteCleaner — Automated File System Cleanup Tool

> Automatically scan directories, detect zero-byte files, delete them, and generate detailed timestamped reports — all on a configurable schedule.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Automation](https://img.shields.io/badge/Automation-Scheduled-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Scheduling](#scheduling)
- [Sample Log Report](#sample-log-report)
- [Error Handling](#error-handling)
- [Author](#author)
- [License](#license)

---

## Overview

**ZeroByteCleaner** is a lightweight Python automation tool designed to keep your file system clean by automatically identifying and removing empty (0-byte) files from any specified directory and its subdirectories.

It runs on a **configurable schedule**, generates a professional `.log` report after every scan, and handles errors gracefully — making it ideal for servers, shared drives, temp folders, and automated pipelines.

---

## Features

- Recursively scans all subdirectories inside a given target directory
- Detects and permanently removes all empty (0-byte) files
- Generates a detailed, timestamped `.log` report after every scan
- Runs continuously on a **user-configurable schedule**
- Logs exact file counts: total scanned vs. total deleted
- Validates the target path before scanning (existence + type checks)
- Writes errors directly into the log file for full traceability
- Lightweight — uses only standard Python libraries + `schedule`

---

## Project Structure

```
ZeroByteCleaner/
│
├── ZeroByteCleaner.py          # Main automation script
├── requirements.txt            # Python dependencies
├── .gitignore                  # Files excluded from version control
└── README.md                   # Project documentation
```

---

## Requirements

- Python 3.6 or higher
- [`schedule`](https://pypi.org/project/schedule/) library

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/ZeroByteCleaner.git
cd ZeroByteCleaner
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

`requirements.txt` contains:
```
schedule
```

---

## Usage

Run the script by passing the **target directory path** as a command-line argument:

```bash
python ZeroByteCleaner.py <path_to_directory>
```

### Examples

**Windows:**
```bash
python ZeroByteCleaner.py C:\Users\Sanket\Projects\TestFolder
```

**Linux / macOS:**
```bash
python ZeroByteCleaner.py /home/sanket/projects/TestFolder
```

On startup, the tool will:
1. Immediately perform the **first scan**
2. Then repeat the scan automatically based on the configured schedule
3. Save a `.log` report in the **current working directory** after every scan

---

## Scheduling

The scan interval is configured inside `ZeroByteCleaner.py` in the `main()` function.

**Default: every 1 minute**

```python
schedule.every(1).minutes.do(DirectoryScanner, sys.argv[1])
```

You can change this to any interval you need:

| Interval | Code |
|---|---|
| Every 1 minute *(default)* | `schedule.every(1).minutes.do(...)` |
| Every 10 minutes | `schedule.every(10).minutes.do(...)` |
| Every 1 hour | `schedule.every(1).hours.do(...)` |
| Every day at 9 AM | `schedule.every().day.at("09:00").do(...)` |
| Every Monday | `schedule.every().monday.do(...)` |

Simply update the line in the script and restart the tool for the new schedule to take effect.

---

## Sample Log Report

Each scan generates a `.log` file named with a full timestamp, for example:

```
ZeroByteCleaner_Report_Thu_Apr_30_10_45_00_2026.log
```

**Sample log content:**

```
---------------------------------------------------------
     This is a log file created by 'ZeroByteCleaner'     
---------- Automated File System Cleanup Tool -----------
---------------------------------------------------------
Author      : Sanket Sadashiv Hajare
Description : Removes empty (0-byte) files from directory
Timestamp   : Thu Apr 30 10:45:00 2026
---------------------------------------------------------

---------------------------------------------------------
Total file scanned          : 42
Total Empty file found      : 5
This log file is created at : Thu Apr 30 10:45:00 2026
---------------------------------------------------------
```

---

## Error Handling

ZeroByteCleaner validates the target path before scanning and writes errors directly into the log file.

| Situation | Behavior |
|---|---|
| Directory does not exist | Logs error, closes log file, exits safely |
| Path exists but is not a directory | Logs error, closes log file, exits safely |
| Invalid number of arguments | Prints usage instructions and exits |

---

## Author

**Sanket Sadashiv Hajare**

If you find this tool useful, feel free to ⭐ star the repository and share it!

---

## License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it.

```
MIT License

Copyright (c) 2026 Sanket Sadashiv Hajare

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```