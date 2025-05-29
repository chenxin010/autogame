import win32helper
import rapidocrhelper
import win32gui
import win32ui
import win32con
import pyautogui

handle=win32helper.GetHandle('向僵尸开炮')

winX,winY,winWidth,winHeight=win32helper.GetWin(handle)

screenshot = pyautogui.screenshot(region=(winX+int(winWidth/2)-70, int(winY+winHeight*0.65), 140, 100))#PC适配和无适配的高度不一样
# 保存截图
screenshot.save(".\cache\shot.png")