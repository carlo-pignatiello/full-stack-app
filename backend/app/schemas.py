from pydantic import BaseModel

class TokenRequest(BaseModel):
    username: str
    password: str

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str