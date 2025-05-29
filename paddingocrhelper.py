import cv2

from rapidocr_paddle import RapidOCR

# import pyautogui

engine = RapidOCR()


def GetPoint(txt):
    img_path = './cache/shot.png'
    response = engine(img_path)
    x,y=0,0
    for val in response[0]:
        text=val[1]
        point=val[0]
        if(text==txt):
            for v in point:
                x=x+v[0]
                y=y+v[1]
    return (x/4,y/4)

def GetAll():
    img_path = './cache/shot.png'
    response = engine(img_path)
    result={}
    if(response[0]==None): return
    
    for val in response[0]:
        x,y=0,0
        text=val[1]
        point=val[0]
        for v in point:
            x=x+v[0]
            y=y+v[1]
        result[text]=(x/4,y/4)
    return result

def GetByPath(path):
    img_path = path
    response = engine(img_path)
    result={}
    if(response[0]==None): return
    
    for val in response[0]:
        x,y=0,0
        text=val[1]
        point=val[0]
        for v in point:
            x=x+v[0]
            y=y+v[1]
        result[text]=(x/4,y/4)
    return result