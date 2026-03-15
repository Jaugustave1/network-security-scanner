# Network Security Scanner

A Python-based tool that scans a target system for open ports and identifies potential security vulnerabilities.

## Overview

This project demonstrates fundamental cybersecurity and networking concepts by implementing a simple port scanning tool using Python socket programming.

The scanner checks common ports on a target system and reports whether they are open or closed.

## Features

- Scans common network ports
- Identifies open vs closed ports
- Uses Python socket programming
- Demonstrates basic network security analysis

## Technologies Used

- Python
- Socket Programming
- Networking Fundamentals

## Example Usage

When the program runs, the user enters a target IP address.

Example:

```
Enter target IP address: 192.168.1.1

Scanning target: 192.168.1.1

Port 21 is closed
Port 22 is OPEN
Port 80 is OPEN
Port 443 is OPEN
```

## How to Run

1. Install Python on your system.

2. Clone the repository:

```
git clone https://github.com/Jaugustave1/network-security-scanner.git
```

3. Navigate into the project folder:

```
cd network-security-scanner
```

4. Run the scanner:

```
python scanner.py
```

5. Enter the target IP address when prompted.
