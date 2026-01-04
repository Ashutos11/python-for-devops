from fastapi import APIRouter
from services.aws_metrics import get_bucket_info,get_instance_info 

router = APIRouter(
    prefix="/aws"
)

@router.get("/s3")
def get_buckets():
    list_buckets = get_bucket_info()
    return list_buckets

@router.get("/ec2")
def get_instances():
    list_instances = get_instance_info()
    return list_instances