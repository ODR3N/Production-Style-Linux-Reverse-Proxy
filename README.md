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

Main Components
Client VM

The Client VM is used to simulate a user or external requester.

It is used for:

Testing DNS or host resolution
Sending HTTP requests using curl
Validating access to the reverse proxy
Confirming that the backend application is not directly exposed when firewall rules are applied
Proxy VM

The Proxy VM runs Nginx and acts as the public-facing entry point.

It is responsible for:

Receiving requests from the client
Forwarding traffic to the backend application server
Applying reverse proxy rules
Handling logging
Supporting TLS termination
Applying rate limiting
Restricting direct backend exposure
App VM

The App VM runs a simple Python web application.

It includes:

A basic web endpoint
A /health endpoint for health checks
A service managed with systemd
Application logs for troubleshooting
Technologies Used
Ubuntu Server
Linux CLI
Bash
SSH
SSH key-based authentication
Nginx
Python
systemd
UFW / firewall basics
Netplan
TCP/IP networking
DNS / host resolution
HTTP / HTTPS
VirtualBox
Git and GitHub
Skills Demonstrated

This project demonstrates hands-on skills in:

Linux system administration
User and permission management
File system navigation and ownership
SSH access and key-based authentication
Static IP configuration
Hostname and local DNS resolution
Network troubleshooting
Process and service management
Nginx reverse proxy configuration
Backend application deployment
Health check implementation
Firewall configuration
Log analysis
Troubleshooting methodology
Technical documentation
Repository Structure
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

Recommended documentation files:

File	Purpose
README.md	Main project overview
docs/architecture.md	Architecture explanation and network design
docs/setup-guide.md	Step-by-step setup instructions
docs/system-guide.md	Linux concepts and commands used
docs/troubleshooting.md	Common issues and fixes
docs/screenshots/	Screenshots of commands, services, and tests
app/app.py	Python backend application
nginx/reverse-proxy.conf	Nginx reverse proxy configuration
systemd/app.service	systemd unit file for the Python app
scripts/health-check.sh	Basic health check script
Network Design

Example network configuration:

VM	Role	Example IP
Client VM	Test requester	192.168.136.10
Proxy VM	Nginx reverse proxy	192.168.136.20
App VM	Python backend app	192.168.136.30

Example local host resolution:

192.168.136.20 linux-lab.local
192.168.136.30 app.internal

The client should access the application through the proxy:

curl http://linux-lab.local

The proxy forwards the request to the backend app server.

Key Linux Concepts Practiced
Users, Groups, and Permissions

The lab includes practice with:

Creating users
Managing groups
Assigning file ownership
Setting permissions
Understanding least privilege access

Example commands:

sudo adduser deployer
sudo usermod -aG sudo deployer
sudo chown -R deployer:deployer /opt/app
chmod 750 /opt/app
SSH Key-Based Access

SSH keys are used to avoid password-based authentication and simulate a more secure administration workflow.

Example:

ssh-keygen
ssh-copy-id deployer@192.168.56.30
ssh deployer@192.168.56.30
Static Networking

Static IP addresses are configured to keep the environment predictable.

Example Netplan concept:

network:
  version: 2
  ethernets:
    enp0s8:
      addresses:
        - 192.168.136.30/24

Apply changes:

sudo netplan apply
Service Management with systemd

The Python application is managed as a Linux service.

Common commands:

sudo systemctl daemon-reload
sudo systemctl enable app.service
sudo systemctl start app.service
sudo systemctl status app.service

Logs can be reviewed with:

journalctl -u app.service
journalctl -u app.service -f
Nginx Reverse Proxy

Nginx is configured to forward requests from the proxy server to the backend application.

Example concept:

server {
    listen 80;
    server_name linux-lab.local;

    location / {
        proxy_pass http://192.168.56.30:8000;
    }

    location /health {
        proxy_pass http://192.168.56.30:8000/health;
    }
}

Test and reload Nginx:

sudo nginx -t
sudo systemctl reload nginx
Health Checks

The backend application includes a /health endpoint.

Example test:

curl http://linux-lab.local/health

Expected result:

OK

This simulates a basic production health check used in cloud, DevOps, and SRE environments.

Firewall Basics

Firewall rules are used to control access between systems.

Example goals:

Allow SSH only where needed
Allow HTTP/HTTPS to the proxy
Restrict direct access to the backend app
Allow the proxy to reach the app internally

Example commands:

sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw enable
sudo ufw status verbose
Troubleshooting Practice

This lab includes troubleshooting scenarios such as:

Nginx not forwarding traffic
Backend app service not running
Incorrect firewall rules
Wrong IP address or hostname
Permission errors
SSH connection failures
Port conflicts
Misconfigured systemd service
Invalid Nginx configuration

Useful commands:

ip a
ip route
ping <host>
ss -tulnp
curl -v http://linux-lab.local
systemctl status nginx
systemctl status app.service
journalctl -xe
journalctl -u nginx
journalctl -u app.service
sudo nginx -t
sudo ufw status verbose
Example Validation Checklist

Use this checklist to confirm that the environment is working correctly.

[ ] Client VM can reach Proxy VM
[ ] Proxy VM can reach App VM
[ ] SSH key-based access works
[ ] Python app starts successfully
[ ] Python app is managed by systemd
[ ] Nginx configuration test passes
[ ] Nginx reverse proxy forwards traffic correctly
[ ] /health endpoint responds correctly
[ ] Firewall rules allow required traffic
[ ] Backend app is not unnecessarily exposed
[ ] Logs can be reviewed for troubleshooting
What I Learned

Through this project, I practiced how to design, configure, and troubleshoot a small Linux-based infrastructure environment.

Key learning outcomes include:

How Linux servers communicate across a local network
How to configure and validate static IP addresses
How to use SSH keys for secure administration
How systemd manages long-running services
How Nginx works as a reverse proxy
How to expose an application through a controlled entry point
How to use logs to investigate service issues
How firewall rules affect connectivity
How to document technical systems clearly
Why This Project Matters

This project is relevant to real-world roles such as:

Technical Support Engineer
Cloud Support Engineer
Linux System Administrator
DevOps Engineer
Site Reliability Engineer
Infrastructure Support Engineer

It demonstrates practical skills used when supporting production systems, investigating service issues, reviewing logs, validating connectivity, and documenting operational procedures.

Future Improvements

Planned improvements include:

Add TLS certificates for HTTPS
Add stronger Nginx security headers
Add centralized logging
Add monitoring with Prometheus and Grafana
Add Docker-based deployment
Add GitHub Actions for validation
Add automated provisioning with Terraform or Ansible
Add diagrams and screenshots for each major step
Add more LFCS-style practice scenarios
Screenshots

Recommended screenshots to include:

docs/screenshots/
├── vm-network-design.png
├── client-curl-test.png
├── nginx-status.png
├── app-service-status.png
├── health-check-response.png
├── firewall-status.png
└── journalctl-logs.png

Example Markdown:

![Nginx status](docs/screenshots/nginx-status.png)

![Health check](docs/screenshots/health-check-response.png)
Status

Project status: Active / In Progress

This lab is being continuously improved as part of a broader Cloud, DevOps, SRE, and DevSecOps learning roadmap.

Author

Adrian Fonseca Coto
Technical Support & Cloud Support professional focused on Linux, Azure, troubleshooting, networking, and DevOps/SRE growth.

GitHub: ODR3N
LinkedIn: Adrian Fonseca Coto
