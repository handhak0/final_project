'''모듈 불러오기'''

from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests

import uvicorn
import os

import sys
sys.path.append("C:/Users/sonso/Desktop/Git/멀티캠퍼스/04.FinalProject/손학영/Face_segmentation")

import random

# 모델 모듈불러오기
import segmentation


'''프로그램 시작'''

app = FastAPI()

# src 연결
app.mount("/static", StaticFiles(directory="static"), name="static") # css 파일
templates = Jinja2Templates(directory = "templates") # html 파일

# root 연결
@app.get('/')
async def root() :
    return {"hello" : "world"}


@app.get('/home', response_class = HTMLResponse)
async def home(request : Request) :
    return templates.TemplateResponse("home.html", context={"request": request})

@app.get('/home_img/{img_num}')
async def home_img(img_num : int) :
    homeImg = os.listdir("./static/output")
    img_src = "./static/output/" + homeImg[img_num]
    return FileResponse(img_src)


# @app.get('/home_imgshow/{img_num}', response_class = HTMLResponse)
# async def home_imgshow(img_num : int) :
#     img_src = "./static/output/" + homeImg[img_num]
#     return templates.TemplateResponse("homeImg.html", context={"request": request})



@app.get('/login', response_class = HTMLResponse)
async def login(request : Request) :
    return templates.TemplateResponse("login.html", context={"request": request})

@app.post('/login_check/', response_class= HTMLResponse)
async def login_check(request : Request):
    return templates.TemplateResponse("home.html", context={"request":request})


@app.get('/write', response_class = HTMLResponse)
async def write(request : Request) :

    return templates.TemplateResponse("write.html", context={"request": request})


@app.post("/runmodel/", response_class = HTMLResponse)
async def runmodel(request : Request, files: UploadFile = File(...)):
    global fnm
    fnm = files.filename
    file_location = f"./static/input/{fnm}"
    with open(file_location, "wb+") as file_object:
        file_object.write(files.file.read())
    # face segmentation 실행
    segmentation.segmentation(fnm)
    return templates.TemplateResponse("output.html", context={"request": request})



@app.get('/output', response_class = HTMLResponse)
async def output(request : Request) :

    return templates.TemplateResponse("output.html", context={"request": request})

@app.get('/output_img')
async def home_img() :
    global output_src
    output_src = f"./static/output/{fnm}"
    return FileResponse(output_src)


@app.get('/download')
async def download() :
    # file_path = './static/output/20211119_101611_12.png'
    return FileResponse(path = output_src, filename='character.png')


uvicorn.run(app, port=8000)

