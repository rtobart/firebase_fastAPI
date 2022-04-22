from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    lastName: str
    born: int 