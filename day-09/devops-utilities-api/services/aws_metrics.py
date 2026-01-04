import boto3

def get_bucket_info():
    s3_client = boto3.client("s3")

    bucket_list = []
    buckets = s3_client.list_buckets()["Buckets"]

    for bucket in buckets:
        bucket_list.append(bucket["Name"])

    return {
        'buckets': bucket_list
    }

def get_instance_info():
    ec2_client = boto3.client("ec2")

    instances = []

    response = ec2_client.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_name = instance["Tags"]

    return {
        'instance': instance_name[0].get("Value")
    }
