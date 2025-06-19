from pydantic import BaseModel

class User(BaseModel):
    login: str
    id: int
    avatar_url: str
    created_at: str
    bio: str | None
