# Production Style Reverse Proxy

## Overview
This project simulates a production-style reverse proxy architecture using Linux virtual machines.

It demonstrates how an internal application is securely exposed through a proxy layer, replicating real-world infrastructure used in DevOps and Site Reliability Engineering environments.

---

## Objectives
- Build a multi-node Linux environment
- Configure a reverse proxy using Nginx
- Publish an internal backend application securely
- Practice Linux networking and SSH access
- Validate connectivity between segmented systems

---

## Architecture

This project uses three virtual machines:

| VM        | Role              | IP Address        |
|----------|------------------|------------------|
| client-vm | Client machine    | 192.168.56.10    |
| proxy-vm  | Reverse proxy     | 192.168.56.20    |
| app-vm    | Backend server    | 192.168.56.30    |

### Traffic Flow
Client → Proxy (Nginx) → App Server

---

## Technologies Used
- Ubuntu Server
- Nginx
- Python 3
- SSH
- Netplan
- systemd
- VirtualBox

---

## Project Structure
```text
production-style-reverse-proxy/
├── docs/
├── configs/
├── app/
├── screenshots/
