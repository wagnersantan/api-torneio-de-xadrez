from pydantic import BaseModel, Field

class UserLogin(BaseModel):
    username: str = Field(..., example="usuario123")
    password: str = Field(..., example="senhaSegura!")

class UserResponse(BaseModel):
    id: str
    username: str
