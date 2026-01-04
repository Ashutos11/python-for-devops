from fastapi import APIRouter, HTTPException
from services.health_metrics import get_system_health

router = APIRouter()

@router.get("/health")
def get_health():
    try:
        health = get_system_health()
        return health
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )