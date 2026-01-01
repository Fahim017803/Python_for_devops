from fastapi import APIRouter, HTTPException
from services.aws_service import aws_buckets_info

router = APIRouter(prefix="/aws", tags=["AWS Utilities"])


@router.get("/s3", status_code=200)
def old_buckets():
    try:
        return aws_buckets_info()
    except Exception:
        raise HTTPException(
            status_code=500, detail="Internal error while scanning S3 buckets"
        )
