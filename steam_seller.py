import random
import pyautogui
import pyperclip
import time


class SteamSeller():
    def __init__(self, cards):
        self.cards = cards
        self.autogui = UserMocker(0.9)

    def sell_all_cards(self):
        time.sleep(2)
        n = 1
        while n <= self.cards:
            self.find_card()
            price = self.find_cheapest_price()
            self.find_card()
            self.finalize_payment(price)
            n += 1

    def finalize_payment(self, price):
        self.autogui.clik_image('sell.png')
        time.sleep(1)
        self.autogui.clik_image('block.png')
        self.autogui.type(price)
        self.autogui.clik_image('accept.png', False)
        self.autogui.clik_image('sell_1.png')
        time.sleep(2)
        self.autogui.clik_image('ok.png')

    def find_card(self):
        x, y = self.autogui.locate_image('gems.png')
        x += 103
        self.autogui.move_to(x, y)
        self.autogui.click()
        self.autogui.scroll()
        time.sleep(2)

    def find_cheapest_price(self):
        self.autogui.clik_image('shop.png')
        time.sleep(4)
        self.autogui.copy_text_image('cheapest.png')
        text = self.autogui.text
        words = text.split()
        self.autogui.clik_image('back.png')
        time.sleep(2)
        return words[-1]


class UserMocker():
    def __init__(self, confidence=0.9):
        self.text = ""
        self.confidence = confidence

    def copy_text_image(self, button_name):
        self.move_to_image(button_name)
        pyautogui.tripleClick()
        pyautogui.hotkey('ctrl', 'c')
        self.text = pyperclip.paste()

    def clik_image(self, button_name, restart=True):
        self.move_to_image(button_name, restart)
        pyautogui.click()

    def move_to_image(self, button_name, restart=True):
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen(button_name, confidence=self.confidence)
            except TypeError:
                if not restart:
                    break
                continue
            self.move_to(x, y)
            break
    def locate_image(self, button_name, restart=True):
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen(button_name, confidence=self.confidence)
            except TypeError:
                if not restart:
                    break
                continue
            return x, y
            break

    def click(self):
        pyautogui.click()

    def scroll(self, how=-1000):
        pyautogui.vscroll(how)

    def move_to(self, x, y):
        num = random.uniform(1, 3)
        pyautogui.moveTo(x, y, num, pyautogui.easeInOutQuad)

    def type(self, text):
        pyautogui.write(text, interval=0.25)
