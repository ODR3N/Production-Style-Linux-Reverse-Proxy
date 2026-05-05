# Linux Reverse Proxy Infrastructure Lab

Production-style Linux infrastructure lab focused on system administration, networking, reverse proxy configuration, service management, security hardening, logging, and troubleshooting.

This project started as a foundational Linux and networking lab and evolved into a more complete infrastructure practice environment designed to simulate real-world support, DevOps, and SRE scenarios using multiple Linux virtual machines.

---

## Overview

The goal of this project is to build, document, and troubleshoot a small production-style Linux environment using Ubuntu Server virtual machines.

The lab demonstrates how different infrastructure components interact in a controlled environment:

- A client machine used to test connectivity and application access
- A reverse proxy server using Nginx
- A backend application server running a simple Python web service
- Optional logging and monitoring extensions
- Network segmentation and controlled access between nodes

This project focuses on practical infrastructure skills instead of only theoretical concepts. It is designed to show hands-on experience with Linux administration, networking, service configuration, and operational troubleshooting.

---

## Project Objectives

The main objectives of this lab are to:

- Build a multi-node Linux environment using virtual machines
- Configure static networking and host resolution
- Secure remote access using SSH keys
- Deploy a backend Python web application
- Configure Nginx as a reverse proxy
- Add a `/health` endpoint for service health checks
- Manage Linux services using `systemd`
- Apply basic firewall rules
- Configure logging and review service logs
- Practice troubleshooting using real Linux commands
- Document the architecture and operational procedures clearly

---

## Architecture

The lab uses a multi-VM architecture.

```text
+----------------+
| Client VM      |
| Test requester |
+-------+--------+
        |
        | HTTP / HTTPS request
        v
+----------------+
| Proxy VM       |
| Nginx          |
| Reverse Proxy  |
| TLS / Logging  |
+-------+--------+
        |
        | Internal HTTP traffic
        v
+----------------+
| App VM         |
| Python App     |
| /health        |
+----------------+
```

## Main Components

### Client VM

The Client VM simulates an external requester or user machine.

It is used for:

- Testing DNS or local host resolution
- Sending HTTP requests with `curl`
- Validating access to the reverse proxy
- Confirming whether backend services are properly exposed or restricted

---

### Proxy VM

The Proxy VM runs Nginx and acts as the public-facing entry point.

It is responsible for:

- Receiving requests from the client
- Forwarding traffic to the backend application server
- Applying reverse proxy rules
- Supporting logging
- Preparing the environment for TLS termination
- Applying rate limiting
- Reducing direct exposure of the backend application

---

### App VM

The App VM runs a simple Python web application.

It includes:

- A basic web endpoint
- A `/health` endpoint for health checks
- A service managed with `systemd`
- Application logs for troubleshooting

---

### Optional Log VM

The optional Log VM can be used as a future extension for centralized logging.

Potential use cases:

- Store logs from the proxy and application servers
- Practice log forwarding
- Simulate operational log review
- Prepare the lab for monitoring and observability improvements

---

## Technologies Used

- Ubuntu Server
- Linux CLI
- Bash
- SSH
- SSH key-based authentication
- Nginx
- Python
- systemd
- UFW / firewall basics
- Netplan
- TCP/IP networking
- DNS / host resolution
- HTTP / HTTPS
- VirtualBox
- Git
- GitHub

---

## Skills Demonstrated

This project demonstrates hands-on skills in:

- Linux system administration
- User and permission management
- File system navigation and ownership
- SSH access and key-based authentication
- Static IP configuration
- Hostname and local DNS resolution
- Network troubleshooting
- Process and service management
- Nginx reverse proxy configuration
- Backend application deployment
- Health check implementation
- Firewall configuration
- Log analysis
- Troubleshooting methodology
- Technical documentation

---

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── architecture.md
│   ├── setup-guide.md
│   ├── system-guide.md
│   ├── troubleshooting.md
│   └── screenshots/
├── app/
│   └── app.py
├── nginx/
│   └── reverse-proxy.conf
├── systemd/
│   └── app.service
└── scripts/
    └── health-check.sh
