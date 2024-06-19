from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    _id: Optional[str] = None
    name: str
    email: str
    password: str
