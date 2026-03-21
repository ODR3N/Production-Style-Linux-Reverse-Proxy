# Setup Guide — Production Style Reverse Proxy

# System Guide — Linux & Networking Foundations Capstone

## Overview

This document describes the full setup of a multi-node Linux environment simulating a production-style service architecture.

### Architecture

```
[ client-vm ] ---> [ proxy-vm ] ---> [ app-vm ]
```

* **client-vm**: testing, SSH control, Git repository
* **proxy-vm**: reverse proxy (Nginx), TLS, rate limiting
* **app-vm**: backend Python application (systemd service)

---

# Phase 1 — Base System Setup (ALL VMs)

Run on:

* client-vm
* proxy-vm
* app-vm

## Set hostname

```bash
sudo hostnamectl set-hostname client-vm   # change per VM
```

## Create admin user

```bash
sudo adduser adrian
sudo usermod -aG sudo adrian
```

---

# Phase 2 — Networking (ALL VMs)

## Inspect interfaces

```bash
ip addr
ip route
```

## Configure static IP (Netplan)

```bash
sudo nano /etc/netplan/*.yaml
```

Example:

```yaml
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: no
      addresses:
        - 192.168.56.X/24
```

Apply:

```bash
sudo netplan apply
```

---

## Configure hostname resolution

Run on ALL VMs:

```bash
sudo nano /etc/hosts
```

Add:

```
192.168.56.10 client-vm
192.168.56.20 proxy-vm
192.168.56.30 app-vm
```

---

## Test connectivity

### From client-vm

```bash
ping -c 4 proxy-vm
ping -c 4 app-vm
```

### From proxy-vm

```bash
ping -c 4 app-vm
```

---

# Phase 3 — Application Setup (app-vm ONLY)

## Create service user

```bash
sudo useradd --system --create-home --shell /usr/sbin/nologin appsvc
```

## Create directories

```bash
sudo mkdir -p /opt/demoapp
sudo mkdir -p /var/log/demoapp
```

## Set permissions

```bash
sudo chown -R appsvc:appsvc /opt/demoapp /var/log/demoapp
sudo chmod 755 /opt/demoapp
```

## Install Python

```bash
sudo apt update
sudo apt install -y python3
```

## Create application

```bash
sudo nano /opt/demoapp/app.py
```

## Test manually

```bash
sudo -u appsvc python3 /opt/demoapp/app.py
```

```bash
curl http://127.0.0.1:8080
```

---

## Create systemd service

```bash
sudo nano /etc/systemd/system/demoapp.service
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable demoapp
sudo systemctl start demoapp
```

Check:

```bash
sudo systemctl status demoapp
```

---

# Phase 4 — Reverse Proxy (proxy-vm ONLY)

## Install Nginx

```bash
sudo apt update
sudo apt install -y nginx
```

## Create config

```bash
sudo nano /etc/nginx/sites-available/demoapp
```

## Enable site

```bash
sudo ln -s /etc/nginx/sites-available/demoapp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

## Test from client-vm

```bash
curl http://proxy-vm
```

---

# Phase 5 — TLS Setup (proxy-vm ONLY)

## Create certificate

```bash
sudo mkdir -p /etc/nginx/ssl

sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/nginx/ssl/demoapp.key \
  -out /etc/nginx/ssl/demoapp.crt
```

## Reload Nginx

```bash
sudo nginx -t
sudo systemctl reload nginx
```

## Test

```bash
curl -k https://proxy-vm
```

---

# Phase 6 — Rate Limiting (proxy-vm ONLY)

Edit Nginx config and reload:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

Test from client-vm:

```bash
for i in {1..20}; do curl -k https://proxy-vm; done
```

---

# Phase 7 — Logging

## Proxy logs (proxy-vm)

```bash
sudo tail -f /var/log/nginx/demoapp_access.log
```

## App logs (app-vm)

```bash
sudo journalctl -u demoapp -f
```

---

# Phase 8 — SSH Configuration

## Generate key (client-vm)

```bash
ssh-keygen -t ed25519
```

## Copy keys

```bash
ssh-copy-id adrian@proxy-vm
ssh-copy-id adrian@app-vm
```

## Disable password login (proxy-vm & app-vm)

```bash
sudo nano /etc/ssh/sshd_config
```

Restart SSH:

```bash
sudo systemctl restart ssh
```

---

# Phase 9 — Firewall

## proxy-vm

```bash
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

## app-vm

```bash
sudo ufw allow ssh
sudo ufw allow from 192.168.56.20 to any port 8080
sudo ufw enable
```

---

# Phase 10 — Repository Setup (client-vm ONLY)

## Create project

```bash
mkdir month1-linux-network-foundations-capstone
cd month1-linux-network-foundations-capstone
```

## Create structure

```bash
mkdir app proxy docs scripts screenshots architecture
```

## Create files

```bash
touch README.md .gitignore
touch docs/system-guide.md
```

---

## Copy files from app-vm

```bash
scp adrian@app-vm:/opt/demoapp/app.py ./app/
scp adrian@app-vm:/etc/systemd/system/demoapp.service ./app/
```

## Copy from proxy-vm

```bash
scp adrian@proxy-vm:/etc/nginx/sites-available/demoapp ./proxy/demoapp-nginx.conf
```

---

## Initialize Git

```bash
git init
git add .
git commit -m "Initial commit: Linux networking capstone"
```

## Connect to GitHub

```bash
git remote add origin https://github.com/YOUR-USERNAME/month1-linux-network-foundations-capstone.git
git branch -M main
git push -u origin main
```

---

# Key Learnings

* Difference between process, service, and systemd
* Networking fundamentals: IP, routing, ports
* Reverse proxy and traffic flow
* TLS termination
* Linux permissions and ownership
* SSH key-based authentication
* Firewall restrictions
* Logging and troubleshooting methodology

---

# Troubleshooting Model

Always debug in this order:

1. Service running → `systemctl status`
2. Port listening → `ss -tulpen`
3. Local access → `curl localhost`
4. Network access → `ping`
5. Proxy config → `nginx -t`
6. Logs → `journalctl`, `tail`
7. Firewall → `ufw status`

---

# Final Result

A working multi-node Linux system that simulates:

* application deployment
* traffic routing
* secure exposure
* operational observability
