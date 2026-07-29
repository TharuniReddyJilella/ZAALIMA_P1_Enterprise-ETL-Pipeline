from pydantic import BaseModel, EmailStr

class Customer(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr