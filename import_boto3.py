import boto3
import json
from pprint import pprint

# ---------- AWS Clients ----------
# S3 is mostly global for listing buckets
s3 = boto3.client("s3")

# EC2 is region-specific (N. Virginia)
ec2 = boto3.client("ec2", region_name="us-east-1")

# ---------- Report Structure ----------
report = {
    "s3_buckets": [],
    "ec2_instances": []
}

# ---------- S3: List Buckets ----------
s3_response = s3.list_buckets()

print("S3 Buckets:")
for bucket in s3_response.get("Buckets", []):
    name = bucket.get("Name")
    report["s3_buckets"].append(name)
    print(f"- {name}")

print()  # empty line for readability

# ---------- EC2: List Instances ----------
ec2_response = ec2.describe_instances()

print("EC2 Instances (InstanceId : State):")
for reservation in ec2_response.get("Reservations", []):
    for instance in reservation.get("Instances", []):
        instance_id = instance.get("InstanceId")
        state = instance.get("State", {}).get("Name")
        report["ec2_instances"].append({
            "instance_id": instance_id,
            "state": state
        })
        print(f"- {instance_id} : {state}")

print("\nFull Report (Beautified):")
pprint(report)

# ---------- Save to JSON ----------
with open("aws_report.json", "w") as f:
    json.dump(report, f, indent=4)

print("\nSaved report to aws_report.json")
