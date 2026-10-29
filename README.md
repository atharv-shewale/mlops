# MLOps UAT Environment - Internal POE Dry Run

**Repository:** `https://github.com/atharv-shewale/mlops.git`  
**Team Structure:** Developer 1 (DevOps Lead) & Developer 2 (MLOps Lead)

---

## 1. Quick Start Commands

### Push Project Structure to GitHub
In your VS Code PowerShell terminal, run:
```powershell
git push -u origin main
```
*(If prompted by Windows Git Credential Manager, authorize via browser/GitHub token).*

---

### Run Pytest Unit Verification (Item 11)
```powershell
python -m pip install pytest
python -m pytest -v test_hello.py -s
```

---

### Run Evidently AI Drift Monitoring (Item 12)
```powershell
python -m pip install -r requirements.txt
python evidently_monitor.py
```
Outputs: `evidently_report.html` (interactive HTML dashboard).

---

### Docker Build & Container Run (Items 8, 9, 10)
Make sure Docker Desktop is running:
```powershell
# 1. Pull lightweight python base image
docker pull python:3.10-slim

# 2. Build local container image
docker build -t mlops-hello-uat:latest .

# 3. Run container
docker run --rm mlops-hello-uat:latest
```

---

### Jenkins Pipeline Setup (Items 5, 6, 7)
1. Open Jenkins at `http://localhost:8080`.
2. Create **New Item** -> Name: `mlops-uat-dryrun` -> Type: **Pipeline**.
3. Under **Pipeline script from SCM**:
   - **SCM**: Git
   - **Repository URL**: `https://github.com/atharv-shewale/mlops.git`
   - **Branch Specifier**: `*/main`
   - **Script Path**: `Jenkinsfile`
4. Click **Save** and select **Build Now**.
