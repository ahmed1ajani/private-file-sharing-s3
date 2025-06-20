# 🔐 Private File Sharing using S3 and Pre-Signed URLs

This project demonstrates **secure file sharing** using AWS S3 (Simple Storage Service) and **pre-signed URLs**.

## ✅ What It Does

- Uploads a file to a private S3 bucket
- Generates a **pre-signed URL** to share the file securely
- Enforces time-limited access (e.g. 60 minutes)

---

## 🧪 Two Versions of This Project

### 1. Real AWS S3 (Cloud-Based)
- Script: `generate_url.py`
- Requires real AWS credentials
- Needs AWS S3 bucket set up in the cloud

### 2. LocalStack S3 (Offline Testing)
- Script: `generate_local_url.py`
- Runs fully **offline** using Docker + LocalStack
- Great for **learning and simulation** without cost

---

## 🖼️ Architecture Diagram

![Architecture](diagram.png)

---

## 🚀 How to Run the Local Version

### Prerequisites:
- Python 3
- Docker installed
- LocalStack running locally

### 1. Start LocalStack:
```bash
docker run --rm -it -p 4566:4566 -p 4571:4571 localstack/localstack
