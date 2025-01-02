from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from db.database import engine
from db import models, admin_permission, guest_permission
from router import register_user, login, delete_user, statistic, search_accounts, add, create_group, statistic_user
from pathlib import Path


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


# Route cho trang index
@app.get("/", response_class=HTMLResponse)
async def read_index():
    file_path = Path("static/index.html")
    if file_path.is_file():
        return file_path.read_text(encoding='utf-8')
    return HTMLResponse("<h1>File not found</h1>", status_code=404)

# Route rút gọn cho trang home
@app.get("/home", response_class=HTMLResponse)
async def read_home():
    file_path = Path("static/html/homemain.html")
    if file_path.is_file():
        return file_path.read_text(encoding='utf-8')
    return HTMLResponse("<h1>File not found</h1>", status_code=404)

# Route rút gọn cho trang login
@app.get("/login", response_class=HTMLResponse)
async def read_login():
    file_path = Path("static/html/login.html")
    if file_path.is_file():
        return file_path.read_text(encoding='utf-8')
    return HTMLResponse("<h1>File not found</h1>", status_code=404)

# Route rút gọn cho trang accountinfo
@app.get("/accountinfo", response_class=HTMLResponse)
async def read_accountinfo():
    file_path = Path("static/html/accountinfo.html")
    if file_path.is_file():
        return file_path.read_text(encoding='utf-8')
    return HTMLResponse("<h1>File not found</h1>", status_code=404)

# Route rút gọn cho trang admin_user
@app.get("/admin_user", response_class=HTMLResponse)
async def read_admin_user():
    file_path = Path("static/html/admin_user.html")
    if file_path.is_file():
        return file_path.read_text(encoding='utf-8')
    return HTMLResponse("<h1>File not found</h1>", status_code=404)

# Route rút gọn cho trang forgotpass
@app.get("/login/forgotpass", response_class=HTMLResponse)
async def read_forgotpass():
    file_path = Path("static/html/forgotpass.html")
    if file_path.is_file():
        return file_path.read_text(encoding='utf-8')
    return HTMLResponse("<h1>File not found</h1>", status_code=404)

# Route rút gọn cho trang test
@app.get("/test", response_class=HTMLResponse)
async def read_test():
    file_path = Path("static/html/test.html")
    if file_path.is_file():
        return file_path.read_text(encoding='utf-8')
    return HTMLResponse("<h1>File not found</h1>", status_code=404)

# Route rút gọn cho trang test2
@app.get("/test2", response_class=HTMLResponse)
async def read_test2():
    file_path = Path("static/html/test2.html")
    if file_path.is_file():
        return file_path.read_text(encoding='utf-8')
    return HTMLResponse("<h1>File not found</h1>", status_code=404)




# Add routers
app.include_router(register_user.router)
app.include_router(login.router)
app.include_router(delete_user.router)
app.include_router(statistic.router)
app.include_router(statistic_user.router)
app.include_router(search_accounts.router)
app.include_router(add.router)
app.include_router(create_group.router)





models.Base.metadata.create_all(engine)


