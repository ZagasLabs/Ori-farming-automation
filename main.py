from pynput.keyboard import Controller, Key
import time
import win32gui
import win32con

#bring window to front
def windowEnumHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def bringToFront(window_name):
    top_windows = []
    win32gui.EnumWindows(windowEnumHandler, top_windows)
    for i in top_windows:
        if window_name.lower() in i[1].lower():
            win32gui.ShowWindow(i[0], win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(i[0])
            break

winName = "Ori And The Blind Forest: Definitive Edition"
bringToFront(winName)
#create keyboard controller
keyboard = Controller()

while(True):
    #move left
    keyboard.press(Key.left)
    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)
    time.sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)
    time.sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)
    time.sleep(1)
    keyboard.release(Key.left)
    time.sleep(0.5)

    #climb
    keyboard.press(Key.shift)
    keyboard.press("w")
    time.sleep(1.5)
    keyboard.release("w")
    keyboard.release(Key.shift)

    time.sleep(0.5)

    #jump right
    keyboard.press(Key.right)
    keyboard.press(Key.space)
    time.sleep(0.2)
    keyboard.release(Key.space)
    time.sleep(0.3)
    keyboard.press(Key.space)
    time.sleep(0.5)
    keyboard.release(Key.space)
    keyboard.release(Key.right)


    #dash right and left
    keyboard.press(Key.right)
    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)
    time.sleep(0.5)
    keyboard.release(Key.right)
    keyboard.press(Key.left)
    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)
    time.sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)
    time.sleep(0.2)
    keyboard.press(Key.space)
    time.sleep(0.2)
    keyboard.release(Key.space)
    time.sleep(1)
    keyboard.release(Key.left)
    time.sleep(1.5)

    #move right to kill red enemy

    keyboard.press(Key.right)
    time.sleep(1)
    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)
    time.sleep(0.5)
    keyboard.press('w')
    time.sleep(0.6)
    keyboard.press(Key.space)
    time.sleep(0.3)
    keyboard.release(Key.space)
    keyboard.release('w')
    keyboard.release(Key.right)
    time.sleep(1)


