# Recon Engine - Automated Network Footprinting Tool

A fast, lightweight Python CLI tool for network reconnaissance, banner grabbing, and subdomain discovery. Built for security auditing and preliminary foot-printing.

## Features
- **Open Port Scanning:** Checks critical infrastructure ports (FTP, SSH, HTTP, HTTPS, etc.).
- **Banner Grabbing:** Extracts service versions via direct socket interaction.
- **Subdomain Enumeration:** Uses multi-threaded HTTP requests to detect active subdomains.
- **Automated Logging:** Exports structured scan reports in `.json` format.

## Usage
```bash
python recon.


## 2. Web Vulnerability Scanner (`web_scanner.py`)
An automated web vulnerability scanner built in Python to audit web forms for security flaws like XSS and SQL Injection.

### Features
- Parses HTML forms using `BeautifulSoup4`.
- Tests input parameters against XSS payloads and SQL error signatures.
- Evaluates both `GET` and `POST` request methods.

### Usage
```bash
python web_scanner.py