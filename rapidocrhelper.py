from rapidocr import RapidOCR

# import pyautogui

engine = RapidOCR()


def GetPoint(txt):
    img_path = './cache/shot.png'
    response = engine(img_path)
    x,y=0,0
    if(response.txts==None):
        return (x,y)
    for index,val in enumerate(response.txts):
        if(val==txt):
            for v in response.boxes[index]:
                x=x+v[0]
                y=y+v[1]
            # result.boxes[index]
    return (x/4,y/4)

def GetAll():
    img_path = './cache/shot.png'
    response = engine(img_path)
    result={}
    if(response.txts==None): return
    
    for index,val in enumerate(response.txts):
        x,y=0,0
        for v in response.boxes[index]:
            x=x+v[0]
            y=y+v[1]
        result[val]=(x/4,y/4)
    return result

def GetAllSkill():
    list=GetAll()


