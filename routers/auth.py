from schemas.user import User
from fastapi import APIRouter 
from fastapi.responses import JSONResponse
from  utils.jwt_manager import create_token 

auth= APIRouter()

@auth.post("/login", tags=['auth'], response_model=dict, status_code=200)
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = create_token(data=user.model_dump())
        result = JSONResponse(content={"token": token},
                              status_code=200)
    else:
        result = JSONResponse(content={"message":"Invalid credentials"}, status_code=401)
    return result