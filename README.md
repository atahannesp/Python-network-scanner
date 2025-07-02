# Simple Network Scanner

A lightweight Python script I wrote to practice basic network discovery with ARP requests.  
It scans a target IP or subnet on the local network and prints each active device’s IP and MAC address.

---

## Technologies

- **Python**
- **Scapy** (packet‑crafting library)

---

## Features

- Accepts a single IP (e.g. `192.168.1.10`) **or** an entire range (`192.168.1.0/24`)
- Sends ARP requests to find devices on the LAN
- Outputs results as an easy‑to‑read table
- Minimal dependencies and just one file (`network_scanner.py`)

---

## Installation

```bash
# 1) Clone this repository
git clone https://github.com/atahannesp/simple-network-scanner.git
cd simple-network-scanner

# 2) Install Scapy
pip install scapy
