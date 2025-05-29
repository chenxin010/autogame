# import win32helper
# import rapidocrhelper
# import win32gui
# import win32ui
# import win32con
# import pyautogui

# handle=win32helper.GetHandle('向僵尸开炮')

# winX,winY,winWidth,winHeight=win32helper.GetWin(handle)

# screenshot = pyautogui.screenshot(region=(winX+int(winWidth/2)-70, int(winY+winHeight*0.65), 140, 100))#PC适配和无适配的高度不一样
# # 保存截图
# screenshot.save(".\cache\shot.png")

# # level=paddingocrhelper.GetByPath("./images/xx.jpg")
# # print(level['限时礼包'])

# pyautogui.click(winX+winWidth*0.81, winY+winHeight*0.24)

# from datetime import datetime
# now = datetime.now()
# formatted_time = now.strftime("%H:%M")
# if(formatted_time>'00:00' and formatted_time<'00:10'):
