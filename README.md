# Log Analytics Automation

This repository contains Python scripts for automating log file analysis. The scripts process log files to detect patterns like `ERROR` and `EXCEPTION` while generating reports and visualizations to aid understanding. 

---

## Project Overview

The two scripts serve different purposes:
1. **`test.py`**: A comprehensive log analytics tool that provides:
   - Counting of log levels (`ERROR`, `WARN`, `INFO`).
   - Timestamps extraction for time-based analysis.
   - Visualizations of log frequencies (bar charts).
   - Reports in PDF and TXT formats specifically for `ERROR` entries.

2. **`automatePY.py`**: A lightweight script designed to:
   - Focus solely on extracting lines with `ERROR` and `EXCEPTION`.
   - Save the extracted logs into a TXT file for quick review.

---

## Features

### `test.py`
- Performs **detailed log analytics**.
- Counts log entries for `ERROR`, `WARN`, and `INFO`.
- Generates a **visualization** (bar chart) for log frequencies.
- Extracts and saves `ERROR` messages into:
  - A PDF report (`error_logs.pdf`).
  - A TXT file (`error_logs.txt`).

### `automatePY.py`
- Simplifies analysis by focusing only on `ERROR` and `EXCEPTION` logs.
- Saves the extracted logs into a single TXT file (`log_analysis.txt`).

---

## Project Structure

### Directories
- **`dataset/`**: Contains the sample log file (`Hadoop_2k.log`) used for analysis.
- **`result/`**: Output directory for storing generated visualizations and reports.

### Scripts
- **`test.py`**: Comprehensive analytics with visualizations and detailed reports.
- **`automatePY.py`**: Quick extraction of `ERROR` and `EXCEPTION` logs.

---

## How to Use

### Prerequisites
- **Python 3.x**
- Install required libraries:
  ```bash
  pip install matplotlib reportlab
