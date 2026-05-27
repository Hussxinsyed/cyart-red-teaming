# Cloud Attack Notes

Cloud environments such as AWS, Azure, and GCP can contain security misconfigurations.

Common risks include:
- Public S3 buckets
- Weak IAM permissions
- Overprivileged accounts

Attackers may attempt cloud reconnaissance to identify exposed resources.

MITRE ATT&CK:
T1580 - Cloud Infrastructure Discovery

IAM privilege escalation occurs when excessive permissions allow a user to gain higher access levels.

Security best practices include:
- Least privilege access
- MFA enforcement
- Logging and monitoring
- Restricting public storage access
