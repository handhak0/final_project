'''모듈 불러오기'''

from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests

import uvicorn
import os
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
    home_img = os.listdir("./static/output")
    img_src = "./static/output/" + home_img[img_num]
    return FileResponse(img_src)



@app.get('/write', response_class = HTMLResponse)
async def write(request : Request) :

    return templates.TemplateResponse("write.html", context={"request": request})


@app.post("/runmodel/", response_class = HTMLResponse)
async def runmodel(request : Request, files: UploadFile = File(...)):
    global file_location
    file_location = f"./static/input/{files.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(files.file.read())

    # file_path = './output/covid19.csv'
    return templates.TemplateResponse("output.html", context={"request": request})



@app.get('/output', response_class = HTMLResponse)
async def output(request : Request) :

    return templates.TemplateResponse("output.html", context={"request": request})

@app.get('/output_img')
async def home_img() :
    output_src = file_location
    return FileResponse(output_src)


@app.get('/download')
async def download() :
    file_path = './static/output/20211119_101611_12.png'
    return FileResponse(path = file_location, filename='character.png')


uvicorn.run(app, port=8000)

