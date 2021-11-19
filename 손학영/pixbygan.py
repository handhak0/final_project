'''모듈 불러오기'''

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import uvicorn
import os
'''프로그램 시작'''

app = FastAPI()

# src 연결
app.mount("/static", StaticFiles(directory="static"), name="static") # 첨부 이미지
templates = Jinja2Templates(directory = "templates") # html 파일

# root 연결
@app.get('/', response_class= HTMLResponse)
async def home(request : Request) :
    # base_url = '../img_data/'
    # path = os.listdir('./img_data')[:8]
    # img1 = base_url + path[0]
    # img2 = base_url + path[1]
    # img3 = base_url + path[2]
    # img4 = base_url + path[3]
    # img5 = base_url + path[4]
    # img6 = base_url + path[5]
    # img7 = base_url + path[6]
    # img8 = base_url + path[7]
    # return templates.TemplateResponse("home.html", context={"request": request, "img1" : img1, "img2" : img2, "img3" : img3,
    #                                                         "img4" : img4, "img5" : img5, "img6" : img6,"img7" : img7,
    #                                                         "img8" : img8})

    return templates.TemplateResponse("home.html", context={"request": request})

uvicorn.run(app, port=8000)