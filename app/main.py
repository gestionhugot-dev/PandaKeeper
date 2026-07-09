from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routers.home import router as home_router
from fastapi import FastAPI

from app.database.database import Base, engine
import app.models
from app.routers import guilds

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PandaKeeper",
    version="0.1.0"
)

templates = Jinja2Templates(directory="app/templates")
app.include_router(guilds.router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(home_router)