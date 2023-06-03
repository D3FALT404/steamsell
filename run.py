import pyautogui
from steam_seller import UserMocker, SteamSeller
cards = int(input("ile kart: "))
seller = SteamSeller(cards)
seller.sell_all_cards()