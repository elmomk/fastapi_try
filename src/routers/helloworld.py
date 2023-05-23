from fastapi import APIRouter #, Depends, HTTPException, Query, status
# from src.main import testing

# from streamfinity_fastapi.db import get_session
# from streamfinity_fastapi.schemas.user_schema import User, UserInput
# from streamfinity_fastapi.security.hashing import get_password_hash

router = APIRouter(prefix="/api")


@router.get("/hello")
def hello():
    return {"message": "Hello World!"}
