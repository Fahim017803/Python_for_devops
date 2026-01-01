from fastapi import APIRouter, HTTPException
from services.metrics_service import get_system_metrics

router = APIRouter()


@router.get("/metrics", status_code=200)
def get_metrics():
    try:
        return get_system_metrics()

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Metrics collection failed: {str(e)}"
        )
