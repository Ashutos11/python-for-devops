from fastapi import APIRouter, HTTPException
from services.log_analyzer import analyze_logs

router = APIRouter()

@router.get("/logs")
def get_loginfo():
    try:
        loginfo = analyze_logs()
        return loginfo
    except:
        raise HTTPException(
            status_code= 500,
            detail= "Internal server error"
        )
    