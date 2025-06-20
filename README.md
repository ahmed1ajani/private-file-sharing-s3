# Private File Sharing Using S3 (Simple Storage Service) + Pre-Signed URLs

This project demonstrates how to securely share files stored in Amazon S3 using pre-signed URLs. It simulates best practices for secure access control.

## 🔧 Technologies Used
- **Amazon S3** – for file storage
- **Pre-Signed URLs** – to allow temporary access to private files
- **IAM (Identity and Access Management)** – to control permissions
- **Python + boto3** – to generate and test secure download links

## 📁 File Structure

| File | Description |
|------|-------------|
| `generate_url.py` | Python script to generate a pre-signed URL |
| `sample-iam-policy.json` | Example policy for S3 read-only access |
| `bucket-policy.json` | Bucket policy to deny public & HTTP access |
| `diagram.png` | Visual diagram of architecture (see below) |

## 🔒 Security Highlights
- No public access to S3 bucket
- HTTPS enforced
- Temporary links only (auto-expire)
- IAM permissions follow the least privilege principle

## 🔗 Sample Output

```bash
$ python generate_url.py
🔗 Pre-signed URL: https://your-bucket.s3.amazonaws.com/example.pdf?... (valid for 1 hour)
