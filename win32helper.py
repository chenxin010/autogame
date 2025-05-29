import win32gui
import win32ui
import win32con
import pyautogui

# 获取窗口位置
def GetWin(handle):
    handle = GetHandle('向僵尸开炮')
    if handle:
        # 获取窗口位置
        left, top, right, bottom = win32gui.GetWindowRect(handle)
        x=left
        y=top
        width=right-left
        height=bottom-top
        # print(f"Window found at: ({x}, {y}), width: {width}, height: {height}")
        return (x,y,width,height)
    else:
        print("Window not found.")
        return

# 获取窗口句柄
def GetHandle(title):
    return win32gui.FindWindow(None, title)

# 获取窗口DC
def GetDc(handle):
    return win32gui.GetWindowDC(handle)

# 截取全图
def ShotAll(handle):
    left, top, width, height = GetWin(handle)
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    # 保存截图
    screenshot.save(".\cache\shot.png")

# 技能截图
def ShotSkill(handle):
    left, top, width, height = GetWin(handle)
    screenshot = pyautogui.screenshot(region=(left, int(top+height*0.36), width, 100))#PC适配和无适配的高度不一样
    # 保存截图
    screenshot.save(".\cache\shot.png")

def ShotElite(handle):
    left, top, width, height = GetWin(handle)
    screenshot = pyautogui.screenshot(region=(left+int(width/2)-70, int(top+height*0.65), 140, 100))
    screenshot.save(".\cache\shot.png")

# # 创建一个位图DC，并将其与窗口DC相关联(我的win10截到的图片是全黑的，所以弃用)
# def Shot(handle):
#     hdc=GetDc(handle)
#     print(hdc)
#     win32gui.InvalidateRect(handle,None,True)
#     win32gui.UpdateWindow(handle)
#     left, top, width, height = GetWin(handle)
#     bmp_dc = win32ui.CreateDCFromHandle(hdc)
#     mem_dc = bmp_dc.CreateCompatibleDC()
#     bitmap = win32ui.CreateBitmap()
#     # bitmap.CreateCompatibleBitmap(bmp_dc, right - left, bottom - top)
#     bitmap.CreateCompatibleBitmap(bmp_dc, width, height)
#     mem_dc.SelectObject(bitmap)
    
#     # 将窗口内容复制到位图DC中
#     mem_dc.BitBlt((0, 0), (width, height), bmp_dc, (0, 0), win32con.SRCCOPY)#
    
#     # 保存位图到文件
#     bitmap.SaveBitmapFile(mem_dc, '.\cache\shot.png')
    
#     # 释放资源
#     mem_dc.DeleteDC()
#     win32gui.ReleaseDC(handle, hdc)
#     win32gui.DeleteObject(bitmap.GetHandle())