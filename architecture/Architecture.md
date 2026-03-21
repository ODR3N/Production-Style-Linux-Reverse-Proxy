# Architecture — Production Style Reverse Proxy

## Overview

This architecture simulates a production-style system where access to a backend application is controlled through a reverse proxy.

The design separates responsibilities across multiple nodes to improve security, scalability, and manageability.

---

## System Components

### client-vm

* Acts as the external user
* Sends HTTP requests to the proxy
* Does not communicate directly with the backend

---

### proxy-vm

* Entry point to the system
* Runs Nginx as a reverse proxy
* Forwards incoming requests to the backend server

---

### app-vm

* Hosts the backend application
* Processes requests and returns responses
* Not exposed directly to the client

---

## Network Layout

| VM        | Role           | IP Address    |
| --------- | -------------- | ------------- |
| client-vm | Client         | 192.168.56.10 |
| proxy-vm  | Reverse Proxy  | 192.168.56.20 |
| app-vm    | Backend Server | 192.168.56.30 |

---

## Traffic Flow

```text
Client (192.168.56.10)
        ↓
Proxy (192.168.56.20) — Nginx
        ↓
Backend (192.168.56.30) — Python App
        ↓
Response flows back the same path
```

---

## Request Lifecycle

1. Client sends HTTP request to proxy (port 80)
2. Proxy receives request
3. Nginx routes request using `proxy_pass`
4. Request is forwarded to backend (port 5000)
5. Backend processes request
6. Response is sent back to proxy
7. Proxy returns response to client

---

## Reverse Proxy Role

The reverse proxy is responsible for:

* Routing incoming requests to backend services
* Acting as a single entry point
* Abstracting backend infrastructure from clients

---

## Key Design Principles

### Separation of Concerns

* Client handles requests
* Proxy handles routing
* Backend handles processing

---

### Network Isolation

* Backend is not directly accessible from client
* All traffic flows through proxy

---

### Centralized Access Control

* Proxy acts as control layer
* Enables future additions like:

  * TLS termination
  * Authentication
  * Rate limiting

---

## Nginx Role in Architecture

Nginx is configured to:

* Listen on port 80
* Forward all traffic to backend server
* Preserve request headers

---

## Security Considerations

* Backend is isolated from direct access
* Only proxy communicates with backend
* Reduces attack surface

---

## Scalability Considerations

This architecture can be extended to:

* Multiple backend servers
* Load balancing
* Container orchestration (Docker, Kubernetes)

---

## Diagram (Conceptual)

```text
+------------+        +------------+        +------------+
|  client-vm | -----> |  proxy-vm  | -----> |   app-vm   |
|            |        |   Nginx    |        |  Python    |
+------------+        +------------+        +------------+
       ↑                     ↓                     ↓
       +---------------------+---------------------+
                   Response Flow
```

---

## Result

* Reverse proxy architecture implemented
* Backend isolated from direct access
* Controlled traffic flow through proxy layer
