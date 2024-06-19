from pydantic import BaseModel


class Ping(BaseModel):
    hello: str
