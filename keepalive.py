import pyautogui
import time
import sys

def main():
    while True:
        pyautogui.press('f15')
        print(time.ctime(), ':', 'F15 pressed')
        time.sleep(60*5)
if __name__ == '__main__':
    main()