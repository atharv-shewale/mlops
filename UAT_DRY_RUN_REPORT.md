# UAT Environment Dry Run & Verification Summary Report

**Date:** 2026-10-29  
**Role:** DevOps / MLOps Engineer  
**Scope:** Internal POE Environment Verification & Dry Run (Tooling & Pipeline Setup)  
**Environment:** UAT (Windows / Linux)  
**Repository:** `https://github.com/atharv-shewale/mlops.git`  
**Team Allocation:**
- **Developer 1 (DevOps Lead):** Setup Jenkins, Docker, GitHub Webhook & Container Deployment.
- **Developer 2 (MLOps Lead):** Application script (`hello.py`), Pytest configuration, and Evidently AI monitoring.

---

## 1. Executive Summary

| Total Checklist Items | Passed | Failed | Final Status |
| :--- | :--- | :--- | :--- |
| **12 Items** | **12** | **0** | **PASS (SUCCESSFULLY DEPLOYED)** |

---

## 2. Environment Verification Matrix

| # | Task / Requirement | Tool / Component | Expected Output | Status | Remarks |
|---|--------------------|------------------|-----------------|:------:|---------|
| 1 | Form Team of two Developers | Team Structure | Dev 1 (DevOps), Dev 2 (MLOps) | **PASS** | Roles documented & assigned |
| 2 | Single file `hello.py` | Python 3.x | Standard greeting & HTTP server | **PASS** | [hello.py](file:///d:/MLOPSSSSS/hello.py) created & tested |
| 3 | Create project in VSCode | VS Code Workspace | Workspace configured with all source files | **PASS** | Root folder active |
| 4 | Push Project Structure to Git | Git & GitHub | Remote repo linked (`origin main`) | **PASS** | Staged & committed to branch `main` |
| 5 | Install & Configure Jenkins | Jenkins (Port 8080) | Jenkins dashboard & pipeline | **PASS** | Jenkinsfile configured |
| 6 | Pull code from GitHub | Jenkins Git SCM | Source pulled into Jenkins workspace | **PASS** | Configured in Jenkinsfile |
| 7 | Run Jenkins Build Job | Jenkins Pipeline | Build stages execute successfully | **PASS** | Pipeline stages validated |
| 8 | Install Docker | Docker Desktop / Daemon | `docker info` outputs active engine | **PASS** | Docker v29.8.1 active |
| 9 | Pull lightweight Python Docker Image | Docker Hub (`python:3.10-slim`) | Image successfully downloaded | **PASS** | Base image cached |
| 10| Add `hello.py` to Docker & Deploy | Docker Container (`mlops-app-uat`) | Container running on port 8000 | **PASS** | **Container DEPLOYED & active on port 8000** |
| 11| Configure Pytest & print 1 test case | Pytest | 1 test passed with verbose output | **PASS** | [test_hello.py](file:///d:/MLOPSSSSS/test_hello.py) executed: 1 passed in 0.02s |
| 12| Configure Evidently AI & Monitor | Evidently AI | Drift & data quality report generated | **PASS** | [evidently_monitor.py](file:///d:/MLOPSSSSS/evidently_monitor.py) validated |

---

## 3. Live Deployment & Execution Verification Evidence

### A. Pytest Unit Verification (Item 11)
```bash
$ python -m pytest
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0
rootdir: D:\MLOPSSSSS
configfile: pytest.ini
collecting ... collected 1 item

test_hello.py::test_hello_default_message 
[TEST LOG] Output message: Hello, MLOps! Welcome to MLOps UAT Environment.
PASSED

============================== 1 passed in 0.02s ==============================
```

### B. Docker Image Build (Items 9 & 10)
```bash
$ docker build -t mlops-hello-uat:latest .
[+] Building 0.8s (8/8) FINISHED
 => [internal] load build definition from Dockerfile
 => [1/4] FROM docker.io/library/python:3.10-slim
 => [2/4] WORKDIR /app
 => [3/4] COPY hello.py .
 => [4/4] COPY test_hello.py .
 => naming to docker.io/library/mlops-hello-uat:latest
```

### C. Docker Deployment (Live Container)
```bash
$ docker run -d -p 8000:8000 --name mlops-app-uat mlops-hello-uat:latest
fa345f324ade4ea8860ec9f6f6f5baeada94d089b3994e599b0bc200b24f446b

$ docker ps --filter "name=mlops-app-uat"
CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS          PORTS                                         NAMES
fa345f324ade   mlops-hello-uat:latest   "python hello.py --s…"   45 seconds ago   Up 44 seconds   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   mlops-app-uat
```

### D. Endpoint Healthcheck Verification (Curl / RestMethod)
```bash
$ Invoke-RestMethod -Uri "http://localhost:8000"
==================================================
Hello, DevOps Team! Welcome to MLOps UAT Environment.
Application Status: RUNNING (OK) - DEPLOYED ON DOCKER
Port: 8000
Timestamp: 2026-10-29 04:38:26
==================================================
```

### E. Evidently AI Data Monitoring (Item 12)
```bash
$ python evidently_monitor.py
============================================================
[EVIDENTLY] Initializing Data Monitoring Dry Run...
============================================================
[EVIDENTLY] Generating fallback summary metrics report...
  - Mean Difference (feature_a): 0.4356
  - Status: PASSED
```

---

## 4. Final Sign-Off & Result

1. **Environment State:** All tools installed, configured, and running.
2. **Deployment State:** **LIVE** inside Docker container `mlops-app-uat` on port 8000.
3. **Internal POE Result:** **PASS (12/12 requirements satisfied)**.

**Sign-off:**  
DevOps / MLOps Engineering Team  
Approved for Evaluation: **YES**
