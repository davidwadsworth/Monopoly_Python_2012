from Dice import Dice
from PlayerProfile import PlayerProfile
import pygame
class Monopoly():
    
    tripleDouble=0
    
    def __init__(self):
        self.p1=PlayerProfile()
        self.p2=PlayerProfile()
        self.p3=PlayerProfile()
        self.p4=PlayerProfile()
        
        
    def tradeMoney(self, Player1, Player2, tradeValue):
        if Player1.getWallet()>tradeValue:
            Player1.withdraw(tradeValue)
            Player2.deposit(tradeValue)
        else:
            Player2.deposit(Player1.getWallet())
            Player1.withdraw(Player1.getWallet())
            
        print("Done Trading: M", tradeValue)
    
    def playerMoney(self):
        print("Chaz's Balance:", self.p1.getWallet())
        print("Bart's Balance:", self.p2.getWallet())
        print("Seth's Balance:", self.p3.getWallet())
        print("Trevor's 4 Balance:", self.p4.getWallet())    
        print("")   
    
    