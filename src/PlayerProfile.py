from Dice import Dice
import Variables
import pygame
from pygame.locals import *


class PlayerProfile(object):
    
    
    def __init__(self):
        self.wallet=1500
        self.d1=Dice()
        self.d2=Dice()
        self.house=[]
        self.tripleDouble=0
    
    
    def getWallet(self):
        return self.wallet
    
    def deposit(self, amount):
        self.wallet+=amount
        
    def withdraw(self, amount):    
        if(self.wallet<amount):
            self.wallet=0
        else:
            self.wallet-=amount

    def displayProperties(self):
        print("Properties owned",self.house)
            

    def addProperty(self, property):
        self.house.append(property)
            
    def arrowMoveChaz(self, p1):
        global ChazX
        global ChazY
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if(event.key == K_LEFT):
                    Variables.ChazX-=10
                if(event.key == K_RIGHT):
                    Variables.ChazX+=10
                if(event.key == K_UP):
                    Variables.ChazY-=10
                if(event.key == K_DOWN):
                    Variables.ChazX+=10
                if (event.key == K_SPACE):
                    Variables.turn+=1 
                    Variables.start+=1
                    print(Variables.turn)
                Variables.screen.blit(p1,[Variables.ChazX, Variables.ChazY])
    
    def arrowMoveBart(self, p1):
        global BartX
        global BartY
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if(event.key == K_LEFT):
                    Variables.BartX-=10
                if(event.key == K_RIGHT):
                    Variables.BartX+=10
                if(event.key == K_UP):
                    Variables.BartY-=10
                if(event.key == K_DOWN):
                    Variables.BartX+=10
                if (event.key == K_SPACE):
                    Variables.turn+=1 
                    Variables.start+=1
                    print(Variables.turn)
                Variables.screen.blit(p1,[Variables.BartX, Variables.BartY])
                    
    def arrowMoveSeth(self, p1):
        global SethX
        global SethY
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if(event.key == K_LEFT):
                    Variables.SethX-=10
                if(event.key == K_RIGHT):
                    Variables.SethX+=10
                if(event.key == K_UP):
                    Variables.SethY-=10
                if(event.key == K_DOWN):
                    Variables.SethX+=10
                if (event.key == K_SPACE):
                    Variables.turn+=1 
                    Variables.start+=1
                    print(Variables.turn)
                Variables.screen.blit(p1,[Variables.SethX, Variables.SethY])
    
    def arrowMoveTrevor(self, p1):
        global TrevorX
        global TrevorY
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if(event.key == K_LEFT):
                    Variables.TrevorX-=10
                if(event.key == K_RIGHT):
                    Variables.TrevorX+=10
                if(event.key == K_UP):
                    Variables.TrevorY-=10
                if(event.key == K_DOWN):
                    Variables.TrevorX+=10
                if (event.key == K_SPACE):
                    Variables.turn+=1 
                    Variables.start+=1
                    print(Variables.turn)
                Variables.screen.blit(p1,[Variables.TrevorX, Variables.TrevorY])
            
    def rollDice(self):
        self.die1=self.d1.roll()
        self.die2=self.d2.roll()
        return self.die1, self.die2