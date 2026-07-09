from pydantic import BaseModel


class GuildCreate(BaseModel):
    name: str
    server: str
    region: str


class GuildResponse(GuildCreate):
    id: int

    class Config:
        from_attributes = True