from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.guild import Guild
from app.schemas.guild import GuildCreate, GuildResponse

router = APIRouter(
    prefix="/guilds",
    tags=["Guilds"]
)


@router.post("/", response_model=GuildResponse)
def create_guild(guild: GuildCreate, db: Session = Depends(get_db)):

    db_guild = Guild(
        name=guild.name,
        server=guild.server,
        region=guild.region
    )

    db.add(db_guild)
    db.commit()
    db.refresh(db_guild)

    return db_guild


@router.get("/", response_model=list[GuildResponse])
def list_guilds(db: Session = Depends(get_db)):

    return db.query(Guild).all()