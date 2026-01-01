import boto3
from datetime import datetime, timezone, timedelta

def aws_buckets_info(days: int = 90):
    s3_client = boto3.client("s3")
    tmp = s3_client.list_buckets()
    buckets = tmp["Buckets"]

    old = []

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days)

    for b in buckets:
        if b["CreationDate"] < cutoff:
            old.append(b["Name"])

    return {
    "total buckets": len(buckets),
    "all buckets": [b["Name"] for b in buckets],
    "old count": len(old),
    "days": days,
    "scanned at": now.isoformat(),
    "old buckets": old
}

