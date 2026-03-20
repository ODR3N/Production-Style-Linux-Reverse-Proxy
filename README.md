## Overview
This is a project I built to demonstrate Linux and networking knowledge in a DevOps-aligned environment.

The project simulates a production-style traffic flow using multiple Ubuntu Server virtual machines:

- Client VM
- Proxy VM
- App VM

The project covers:
- Linux user and permission management
- static network configuration
- SSH key-based authentication
- process and service management with systemd
- reverse proxying with Nginx
- TLS termination
- rate limiting
- firewall configuration with UFW
- logging and troubleshooting

---

## Architecture

[client-vm] ---> [proxy-vm: Nginx] ---> [app-vm: Python app]

## Traffic Flow

-Client VM sends a request to Proxy VM
-Proxy VM receives traffic on port 80/443
-Nginx forwards the request to the backend app on port 8080
-App VM responds
-Logs are generated on both proxy and backend

## Technologies Used

-Ubuntu Server
-Linux CLI
-Python 3
-systemd
-Nginx
-OpenSSL
-UFW
-SSH
