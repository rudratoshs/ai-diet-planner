#src/api/middleware/auth.py
from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ...utils.security import decode_jwt
from ...config.environment import env

oauth2_scheme = HTTPBearer(auto_error=True)

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme)):
    try:
        payload = decode_jwt(credentials.credentials)
        return payload
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials"
        )

async def get_current_user(token: dict = Depends(verify_token)):
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials"
        )
    return token