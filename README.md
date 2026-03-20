# Production Style Reverse Proxy

## Overview
This project simulates a production-style reverse proxy environment using Linux virtual machines. It demonstrates how a proxy server securely exposes an internal application server while separating roles across different systems.

## Objectives
- Build a reverse proxy architecture using Linux
- Publish an internal web application through Nginx
- Practice SSH administration and network validation
- Simulate real-world infrastructure concepts used in DevOps and SRE environments

## Architecture
The environment contains three Linux virtual machines:

- **client-vm**: used to test access to the application
- **proxy-vm**: runs Nginx as the reverse proxy
- **app-vm**: runs the backend Python application

Traffic flow:
Client → Proxy (Nginx) → App Server (Python app)

## Technologies Used
- Ubuntu Server
- Nginx
- Python 3
- SSH
- Netplan
- Linux systemd
- VirtualBox

## Project Structure

production-style-reverse-proxy/
├── README.md
├── docs/
├── screenshots/
├── configs/
├── scripts/
└── app/
