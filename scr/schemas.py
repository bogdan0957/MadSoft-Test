from pydantic import BaseModel


class MemesCreate(BaseModel):
    id: int
    meme: str
    description: str

class MemesUpdate(BaseModel):
    meme: str
    description: str