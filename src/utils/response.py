from fastapi import HTTPException
from src.utils.translator import translate

def success_response(data, message_key, lang="en", status_code=200, **kwargs):
    return {
        "status": "success",
        "code": status_code,
        "message": translate(message_key, lang, **kwargs),
        "data": data
    }

def error_response(message_key, lang="en", status_code=400, **kwargs):
    raise HTTPException(
        status_code=status_code,
        detail={
            "status": "error",
            "code": status_code,
            "message": translate(message_key, lang, **kwargs)
        }
    )