import time
import GameControl
import keyboard

# skills1=['子弹爆炸','连发+','分裂子弹四射']
# skills2=['冰爆伤害','冰系缩减','连环冰暴','破裂小冰弹']
# skills3=['干冰弹连发']
# skills3=['热能爆炸']
runFlag=True

def stop_program():
    print("暂停程序...")
    global runFlag
    runFlag = False

keyboard.add_hotkey('ctrl+q', stop_program)

while(runFlag):
    backFlag=False
    GameControl.SkipGift()
    GameControl.StartGame()

    while(backFlag==False and runFlag):
        if(GameControl.Elite()==1):
            continue

        backFlag=GameControl.Reback()

        if(backFlag): 
            time.sleep(2)
            break
        else:
            GameControl.SelectSkill()