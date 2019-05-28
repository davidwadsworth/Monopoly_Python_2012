from abc import ABCMeta, abstractmethod
import pygame
import random


ChazX=592
ChazY=610

BartX=592
BartY=610

SethX=592
SethY=610

TrevorX=592
TrevorY=610

turn=1
start=0
diceRoll1=0
diceRoll2=0
diceRoll3=0
diceRoll4=0

Chazrow=1
Bartrow=1
Sethrow=1
Trevorrow=1

ONE_SPACE=55

spaces = 0
playerMove = 0

screen=pygame.display.set_mode([700,700])

rectX = 56.1
rectY = 96

rect1 = pygame.Rect((545,604),(rectX,rectY))
rect2 = pygame.Rect((545-(rectX),604),(rectX,rectY))
rect3 = pygame.Rect((545-(2*rectX),604),(rectX,rectY))
rect4 = pygame.Rect((545-(3*rectX),604),(rectX,rectY))
rect5 = pygame.Rect((545-(4*rectX),604),(rectX,rectY))
rect6 = pygame.Rect((545-(5*rectX),604),(rectX,rectY))
rect7 = pygame.Rect((545-(6*rectX),604),(rectX,rectY))
rect8 = pygame.Rect((545-(7*rectX),604),(rectX,rectY))
rect9 = pygame.Rect((545-(8*rectX),604),(rectX,rectY))

rect10 = pygame.Rect((0,548),(rectY,rectX))
rect11 = pygame.Rect((0,548-(rectX)),(rectY,rectX))
rect12 = pygame.Rect((0,548-(2*rectX)),(rectY,rectX))
rect13 = pygame.Rect((0,548-(3*rectX)),(rectY,rectX))
rect14 = pygame.Rect((0,548-(4*rectX)),(rectY,rectX))
rect15 = pygame.Rect((0,548-(5*rectX)),(rectY,rectX))
rect16 = pygame.Rect((0,548-(6*rectX)),(rectY,rectX))
rect17 = pygame.Rect((0,548-(7*rectX)),(rectY,rectX))
rect18 = pygame.Rect((0,548-(8*rectX)),(rectY,rectX))

rect19 = pygame.Rect((96,0),(rectX,rectY))
rect20 = pygame.Rect((96+(rectX),0),(rectX,rectY))
rect21 = pygame.Rect((96+(2*rectX),0),(rectX,rectY))
rect22 = pygame.Rect((96+(3*rectX),0),(rectX,rectY))
rect23 = pygame.Rect((96+(4*rectX),0),(rectX,rectY))
rect24 = pygame.Rect((96+(5*rectX),0),(rectX,rectY))
rect25 = pygame.Rect((96+(6*rectX),0),(rectX,rectY))
rect26 = pygame.Rect((96+(7*rectX),0),(rectX,rectY))
rect27 = pygame.Rect((96+(8*rectX),0),(rectX,rectY))

rect28 = pygame.Rect((604,96),(rectY,rectX))
rect29 = pygame.Rect((604,96+(rectX)),(rectY,rectX))
rect30 = pygame.Rect((604,96+(2*rectX)),(rectY,rectX))
rect31 = pygame.Rect((604,96+(3*rectX)),(rectY,rectX))
rect32 = pygame.Rect((604,96+(4*rectX)),(rectY,rectX))
rect33 = pygame.Rect((604,96+(5*rectX)),(rectY,rectX))
rect34 = pygame.Rect((604,96+(6*rectX)),(rectY,rectX))
rect35 = pygame.Rect((604,96+(7*rectX)),(rectY,rectX))
rect36 = pygame.Rect((604,96+(8*rectX)),(rectY,rectX))

jail = pygame.Rect((0,604),(rectY,rectY))
go = pygame.Rect((604,604),(rectY,rectY))
paidParking = pygame.Rect((0,0),(rectY,rectY))
funishment = pygame.Rect((604,0),(rectY,rectY))

rectangles=[rect1,rect2,rect3,rect4,rect5,rect6,rect7,rect8,rect9,rect10,rect11,
            rect12,rect13,rect14,rect15,rect16,rect17,rect18,rect19,rect20,rect21,
            rect22,rect23,rect24,rect25,rect26,rect27,rect28,rect29,rect30,rect31,rect32,rect33,
            rect34,rect35,rect36,jail,go,paidParking,funishment]


SpeedLawn = True
BonfireField = True
BlumbergHall = True
MeesHall = True
ScharpenbergHall = True
DemingHall = True
BSBHall = True
SpeedHall = True
MoenchHall = True
CookStadium = True
ChauncysHall = True
OlinHall = True
CrapoHall = True
MyersHall = True
ApartmentsHall = True
PercopoHall = True
LakesideHall = True
HatfieldHall = True
SkinnerHall = True
HadleyHall = True
LoganLibrary = True
WhiteChapel = True
ChiOmegaFrat = True
TriDelta = True
Facillities = True
SpeedLake = True
AlphaTauOmega = True
SigmaNu = True

p1SpeedLawn = False
p1BonfireField = False
p1BlumbergHall = False
p1MeesHall = False
p1ScharpenbergHall = False
p1DemingHall = False
p1BSBHall = False
p1SpeedHall = False
p1MoenchHall = False
p1CookStadium = False
p1ChauncysHall = False
p1OlinHall = False
p1CrapoHall = False
p1MyersHall = False
p1ApartmentsHall = False
p1PercopoHall = False
p1LakesideHall = False
p1HatfieldHall = False
p1SkinnerHall = False
p1HadleyHall = False
p1LoganLibrary = False
p1WhiteChapel = False
p1ChiOmegaFrat = False
p1TriDelta = False
p1Facillities = False
p1SpeedLake = False
p1AlphaTauOmega = False
p1SigmaNu = False

p2SpeedLawn = False
p2BonfireField = False
p2BlumbergHall = False
p2MeesHall = False
p2ScharpenbergHall = False
p2DemingHall = False
p2BSBHall = False
p2SpeedHall = False
p2MoenchHall = False
p2CookStadium = False
p2ChauncysHall = False
p2OlinHall = False
p2CrapoHall = False
p2MyersHall = False
p2ApartmentsHall = False
p2PercopoHall = False
p2LakesideHall = False
p2HatfieldHall = False
p2SkinnerHall = False
p2HadleyHall = False
p2LoganLibrary = False
p2WhiteChapel = False
p2ChiOmegaFrat = False
p2TriDelta = False
p2Facillities = False
p2SpeedLake = False
p2AlphaTauOmega = False
p2SigmaNu = False

p3SpeedLawn = False
p3BonfireField = False
p3BlumbergHall = False
p3MeesHall = False
p3ScharpenbergHall = False
p3DemingHall = False
p3BSBHall = False
p3SpeedHall = False
p3MoenchHall = False
p3CookStadium = False
p3ChauncysHall = False
p3OlinHall = False
p3CrapoHall = False
p3MyersHall = False
p3ApartmentsHall = False
p3PercopoHall = False
p3LakesideHall = False
p3HatfieldHall = False
p3SkinnerHall = False
p3HadleyHall = False
p3LoganLibrary = False
p3WhiteChapel = False
p3ChiOmegaFrat = False
p3TriDelta = False
p3Facillities = False
p3SpeedLake = False
p3AlphaTauOmega = False
p3SigmaNu = False

p4SpeedLawn = False
p4BonfireField = False
p4BlumbergHall = False
p4MeesHall = False
p4ScharpenbergHall = False
p4DemingHall = False
p4BSBHall = False
p4SpeedHall = False
p4MoenchHall = False
p4CookStadium = False
p4ChauncysHall = False
p4OlinHall = False
p4CrapoHall = False
p4MyersHall = False
p4ApartmentsHall = False
p4PercopoHall = False
p4LakesideHall = False
p4HatfieldHall = False
p4SkinnerHall = False
p4HadleyHall = False
p4LoganLibrary = False
p4WhiteChapel = False
p4ChiOmegaFrat = False
p4TriDelta = False
p4Facillities = False
p4SpeedLake = False
p4AlphaTauOmega = False
p4SigmaNu = False

Roll1 = True
Roll2 = True
Roll3 = True
Roll4 = True

buy = pygame.Rect((114,464),(150,125))
no = pygame.Rect((214,550),(40,30))
yes = pygame.Rect((124,550),(40,30))
okay = pygame.Rect((169,550),(40,30))
Card = pygame.Rect((114,499),(400,100))
specOkay = pygame.Rect((300,550),(40,30))

Railroad = 200

p1RailroadCount = 0
p2RailroadCount = 0
p3RailroadCount = 0
p4RailroadCount = 0

p1RailroadRent = p1RailroadCount*50
p2RailroadRent = p2RailroadCount*50
p3RailroadRent = p3RailroadCount*50
p4RailroadRent = p4RailroadCount*50

p1UtilityCount = 0
p2UtilityCount = 0
p3UtilityCount = 0
p4UtilityCount = 0

p1UtilityRent1 = 10*random.randrange(1,12)
p1UtilityRent2 = 15*random.randrange(1,12)
p2UtilityRent1 = 10*random.randrange(1,12)
p2UtilityRent2 = 15*random.randrange(1,12)
p3UtilityRent1 = 10*random.randrange(1,12)
p3UtilityRent2 = 15*random.randrange(1,12)
p4UtilityRent1 = 10*random.randrange(1,12)
p4UtilityRent2 = 15*random.randrange(1,12)

Player1inGame = True
Player2inGame = True
Player3inGame = True
Player4inGame = True

dis1 = 0
dis2 = 0
dis3 = 0
dis4 = 0


        
Utility = 150

name = ["Speed Lawn","Bonfire Field", "Blumberg Hall","Mees Hall","Scharpenberg Hall", "Deming Hall","BSB Hall",    
                "Speed Hall","Moench Hall", "Cook Stadium", "Chauncy's Hall","Olin Hall","Crapo Hall","Myer's Hall", "Apartments Hall",
                "Percopo Hall","Lakeside Hall", "Hatfield Hall", "Skinner Hall", "Hadley Hall", "Logan Library", "White Chapel","Chi Omega Frat", "Facilities",
                 "Speed Lake", "Tri Delta", "Alpha Tau Omega", "Sigma Nu"]
price = [60,60,100,100,120,140,140,140,160,160,180,220,220,240,260,260,280,300,300,320,350,400,0,150,150]
rent = [20,40,60,60,80,100,100,120,140,140,160,180,180,200,220,220,240,240,260,300,350,400]
houseRent = [20,40,60,60,80,100,100,120,140,140,160,180,180,200,220,220,240,240,260,300,350,400]
CommunityChest =["WIN A BET WITH A FRIEND COLLECT M100","YOU INHERIT M100",
                           "YOU SELL YOUR BOOKS COLLECT M200","PAY HOSPITAL M100",
                           "BOOK FEE M50","PICK UP A TEACHER'S DRYCLEADING COLLECT M25","PAY SCHOOL TAX OF M150",
                           "YOU HAVE WON SECOND PRIZE IN A BEAUTY CONTEST COLLECT M10",
                           "YOU'RE MOM GIVES YOU MONEY COLLECT M100", "YOU ARE CAUGHT HOLDING HANDS AND ARE NOW FUNISHED",
                           "FIND M20.00 ON THE GROUND COLLECT M20.00"]
Chance = ["Advance to Go", "Care Package from Your Parents, Collect M100.00", "Go Back Three Spaces", 
                       "Student Loan fines, pay M150.00", "Parking Fine M15.00", "You Are Late to Class and Are Funished", 
                        "You need money for new socks M12.00", "You Pulled an All-Nighter and Require M35.00 Worth of Coffee"]

ccM = [-100,-100,-200,100,50,-25,150,-10,-100,0,-20]
cM = [0,-100,0,150,15,0,12,35]
# buyFont = txtText, Textfont, Textsize , Textx, Texty, Textcolor
# trade = pygame.Rect((249,539),(100,50))

