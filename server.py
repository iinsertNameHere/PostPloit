from sanic import Sanic, Request, response, redirect
from sanic.exceptions import SanicException
from bcrypt import checkpw
import json
from lib.models import init_db, SessionLocal, User

from lib.blueprints.ui import ui_bp
from lib.blueprints.auth import auth_bp
from lib.blueprints.api import api_bp

init_db()

app = Sanic("Pilotica")
app.config["OAS_UI_DEFAULT"] = "swagger"
app.static("/static", "./static")

app.blueprint(ui_bp)
app.blueprint(auth_bp)
app.blueprint(api_bp)

@app.get("/")
async def index(request: Request):
    return redirect(app.url_for("ui.dashboard"))
