import pyautogui
from pyperclip import copy

class autoOpt(object):

    optDic = {'moveTo','dragTo','click','doubleClick','scroll','write','press','hotkey'}
    operate = ''
    optItem = []
    keyWord = ''
    cycle = 1

    def moveTo(self):
        x = int(self.optItem[1])
        y = int(self.optItem[2])
        interval = float(self.optItem[3])
        for i in range(self.cycle):
            pyautogui.moveTo(x, y,interval)

    def dragTo(self):
        x = int(self.optItem[1])
        y = int(self.optItem[2])
        interval = float(self.optItem[3])
        for i in range(self.cycle):
            pyautogui.dragTo(x, y, interval, button='left')

    def click(self):
        x = int(self.optItem[1])
        y = int(self.optItem[2])
        for i in range(self.cycle):
            pyautogui.click(x, y)

    def doubleClick(self):
        x = int(self.optItem[1])
        y = int(self.optItem[2])
        for i in range(self.cycle):
            pyautogui.doubleClick(x, y)

    def scroll(self):
        distance = int(self.optItem[1])
        for i in range(self.cycle):
            pyautogui.scroll(distance)
    
    def write(self):
        start = len(self.keyWord) + 1
        end = len(self.operate) - len(str(self.cycle)) - 1
        msg = self.operate[start: end]
        for i in range(self.cycle):
            copy(msg)
            pyautogui.hotkey('ctrl','v')

    def press(self):
        key = self.optItem[1]
        for i in range(self.cycle):
            pyautogui.press(keys)
    
    def hotkey(self):
        keys = self.optItem[1]
        for i in range(self.cycle):
            eval('pyautogui.hotkey('+ keys +')')

    def selectOpt(self,operate):
        self.operate = operate.strip()
        self.optItem = self.operate.split(' ')
        self.keyWord = self.optItem[0]
        self.cycle = int(self.optItem[-1])
        if self.keyWord not in self.optDic:
            print('[error] no such keyWord "' +self.keyWord +'"')
        else:
            print(operate)
            if self.keyWord == 'moveTo':
                self.moveTo()
            if self.keyWord == 'dragTo':
                self.dragTo()
            if self.keyWord == 'click':
                self.click()
            if self.keyWord == 'doubleClick':
                self.doubleClick()
            if self.keyWord == 'scroll':
                self.scroll() 
            if self.keyWord == 'write':
                self.write() 
            if self.keyWord == 'press':
                self.press() 
            if self.keyWord == 'hotkey':
                self.hotkey() 
