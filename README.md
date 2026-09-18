# Lightweight Network Recon Engine

A Python-based CLI tool designed for automated network reconnaissance, service fingerprinting, and security audit logging.

## Features
- **DNS Resolution:** Resolves target domain names to IPv4 addresses.
- **Port Scanning:** Audits common service ports (21, 22, 80, 443, 8080).
- **Banner Grabbing:** Extracts service version banners from open ports.
- **Audit Summary Logging:** Automatically generates clean, time-stamped text logs (`audit_<target>.txt`).

## Requirements
- Python 3.x
- No third-party dependencies required (built using core libraries: `socket`, `json`, `datetime`).

## Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/evil-hack944/recon-security-engine.git](https://github.com/evil-hack944/recon-security-engine.git)
   cd recon-security-engine