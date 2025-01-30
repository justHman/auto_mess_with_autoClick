import pyautogui as a 
from time import sleep  
import pyperclip   

def send(user, mess):
    # Clik seeking
    a.leftClick(x=202, y=140)

    # Write user
    pyperclip.copy(user)
    sleep(1)
    a.hotkey("ctrl", "v")
    a.press('enter')
    sleep(3)

    # Click x
    a.leftClick(x=1782, y=483)

    # Click everyone 
    a.leftClick(x=206, y=458)
    sleep(3)

    # Click message
    a.leftClick(x=1544, y=285)
    sleep(3)

    # Click message box 
    a.leftClick(x=1636, y=986)

    # # Write message
    pyperclip.copy(mess)
    sleep(1)
    a.hotkey("ctrl", "v")
    a.press('enter')
    
    # Notion
    print(f"Sent to {user} with message: {mess}")


# Open coc coccoc
a.leftClick(x=937, y=1044)

# Open fb
a.leftClick(x=547, y=74)
a.write('f')
a.press('enter')
sleep(3)

users = open('user.txt', 'r', encoding='utf-8')
users = users.read().split('\n')

mess = open('mess.txt', 'r', encoding='utf-8')
mess = mess.read().split('\n')

for i in range(len(users)):
    send(users[i], mess[i])
    sleep(3)