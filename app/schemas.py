from pydantic import BaseModel, EmailStr

class TextInput(BaseModel):
    text: str

class URLInput(BaseModel):
    url: str

class SummaryOutput(BaseModel):
    summary: str
    
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    identifier: str
    password: str

class SummaryRequest(BaseModel):
    text: str
    username: str  # So we can track user
