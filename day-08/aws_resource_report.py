import boto3
import json

s3 = boto3.client("s3")
ec2 = boto3.client("ec2", region_name="us-east-1")

report = {
    "s3_buckets": [],
    "ec2_instances": []
}


s3_response = s3.list_buckets()
for i in s3_response["Buckets"]:
    report["s3_buckets"].append(i["Name"])

ec2_response = ec2.describe_instances()

for reservation in ec2_response["Reservations"]:
    for instance in reservation["Instances"]:
        report["ec2_instances"].append(
            {"id": instance["InstanceId"], "state": instance["State"]["Name"]}
        )
print(report)

with open("aws_report.json", "w") as f:
    json.dump(report, f, indent=4)
