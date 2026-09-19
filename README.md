# Recon Engine - Automated Network Footprinting Tool

A fast, lightweight Python CLI tool for network reconnaissance, banner grabbing, and subdomain discovery. Built for security auditing and preliminary foot-printing.

## Features
- **Open Port Scanning:** Checks critical infrastructure ports (FTP, SSH, HTTP, HTTPS, etc.).
- **Banner Grabbing:** Extracts service versions via direct socket interaction.
- **Subdomain Enumeration:** Uses multi-threaded HTTP requests to detect active subdomains.
- **Automated Logging:** Exports structured scan reports in `.json` format.

## Usage
```bash
python recon.py