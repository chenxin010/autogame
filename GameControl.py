import win32helper
import pyautogui
import rapidocrhelper
from loguru import logger
from datetime import datetime

pyautogui.FAILSAFE = False
logger.add("file_{time}.log")

handle=win32helper.GetHandle('向僵尸开炮')

winX,winY,winWidth,winHeight=win32helper.GetWin(handle)

# 开始游戏
def StartGame():
    win32helper.ShotAll(handle)
    x,y=rapidocrhelper.GetPoint('开始游戏')#返回的是文字基于图片的相对坐标,还需要加上窗口坐标
    if(x>0 and y>0): 
        pyautogui.click(winX+x, winY+y)
        return True

# 返回
def Reback():
    win32helper.ShotAll(handle)
    x,y=rapidocrhelper.GetPoint('返回')#返回的是文字基于图片的相对坐标,还需要加上窗口坐标
    if(x>0 and y>0): 
        pyautogui.click(winX+x, winY+y)
        return True

# 获取全部技能
def GetSkill():
    win32helper.ShotSkill(handle)
    list=rapidocrhelper.GetAll()
    return list

# 精英掉落
def Elite():
    win32helper.ShotElite(handle)
    x,y=rapidocrhelper.GetPoint('精英掉落')#返回的是文字基于图片的相对坐标,还需要加上窗口坐标
    if(x>0 and y>0): 
        pyautogui.click(winX+ winWidth*0.5,winY+ winHeight*0.5) #点击中间空白关闭转盘
        return 1
    return 0
    
# 选择技能
def SelectSkill():
    currentSkills= GetSkill()
    if(currentSkills==None):return
    for key,value in currentSkills.items():
        logger.info(key)
        x,y=value
        if('连' in key or '齐' in key):
            pyautogui.click(winX+x, winY+winHeight/2)
            break
        elif('子弹' in key and '电磁' not in key and '火焰' not in key and '急冻' not in key): 
            pyautogui.click(winX+x, winY+winHeight/2)
            break
    pyautogui.click(winX+winWidth/2,winY+winHeight/2)#点中间的

# 处理0点的限时礼包
def SkipGift():
    now = datetime.now()
    formatted_time = now.strftime("%H:%M")
    if(formatted_time>'00:00' and formatted_time<'00:10'):
        win32helper.ShotAll(handle)
        list=rapidocrhelper.GetAll()
        if(list.get('限时礼包','限时礼包')!='限时礼包'):
            pyautogui.click(winX+winWidth*0.81, winY+winHeight*0.24)