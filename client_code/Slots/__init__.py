from ._anvil_designer import SlotsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import time

class Slots(SlotsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    global admindata,customerdata,gamedata,arcadedata,tempdata
    admindata=anvil.server.call('admins')
    customerdata=anvil.server.call('customers')
    gamedata=anvil.server.call('games')
    arcadedata=anvil.server.call('arcade')
    tempdata=anvil.server.call('temps')
    # Any code you write here will run when the form opens.

  def start_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.spin.visible=True
    self.hint.visible=True
    self.start.visible=False
    self.back.visible=False
    self.exit.visible=True

  def hint_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.help.visible=True
    self.back.visible=True    
    self.spin.visible=False
    self.exit.visible=False

  def randomiser(self, **event_args):
    global a,b,c
    global prize
    r1=random.randint(1,5)
    r2=random.randint(1,5)
    r3=random.randint(1,5)
    a="r"+str(r1)+'1'
    b="r"+str(r2)+'2'
    c='r'+str(r3)+'3'  
    if a=='r11':
      self.r11.visible=True
    elif a=='r21':
      self.r21.visible=True
    elif a=='r31':
      self.r31.visible=True
    elif a=='r41':
      self.r41.visible=True
    else:
      self.r51.visible=True
      
    if b=='r12':
      self.r12.visible=True
    elif b=='r22':
      self.r22.visible=True
    elif b=='r32':
      self.r32.visible=True
    elif b=='r42':
      self.r42.visible=True
    else:
      self.r52.visible=True
      
    if c=='r13':
      self.r13.visible=True
    elif c=='r23':
      self.r23.visible=True
    elif c=='r33':
      self.r33.visible=True
    elif c=='r43':
      self.r43.visible=True
    else:
      self.r53.visible=True
    if a=='r11' and b=='r12' and c=='r13':
      prize=500
      self.winnings.visible=True
      self.winnings.text="Congrats!! \nYou got 500 credits!!"
    elif a=='r21' and b=='r22' and c=='r23':
      prize=250
      self.winnings.visible=True
      self.winnings.text="Congrats!! \nYou got 250 credits!!"
    elif a=='r31' and b=='r32' and c=='r33':
      prize=50
      self.winnings.visible=True
      self.winnings.text="Congrats!! \nYou got 50 credits!!"
    elif a=='41' and b=='r42' and c=='r43':
      prize=777
      self.winnings.visible=True
      self.winnings.text="Congrats!! \nYou got 777 credits!!"
    elif a=='51' and b=='r52' and c=='r53':
      prize=100
      self.winnings.visible=True
      self.winnings.text="Congrats!! \nYou got 100 credits!!"
    else:
      prize=0
      self.winnings.visible=True
      self.winnings.text="OOF!! \nYou won nothing, better luck next time!"
    self.prizes()
  
  def spin_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.spin.visible=False
    self.hint.visible=False
    self.back.visible=True
    self.exit.visible=False
    for j in range(1,3):
      for i in range(1,6):
        if i ==1:
          self.r11.visible=True
          self.r12.visible=True
          self.r13.visible=True
          time.sleep(1)
          self.r11.visible=False
          self.r12.visible=False
          self.r13.visible=False
        elif i==2:
          self.r21.visible=True
          self.r22.visible=True
          self.r23.visible=True
          time.sleep(1)
          self.r21.visible=False
          self.r22.visible=False
          self.r23.visible=False
        elif i==3:
          self.r31.visible=True
          self.r32.visible=True
          self.r33.visible=True
          time.sleep(1)
          self.r31.visible=False
          self.r32.visible=False
          self.r33.visible=False
        elif i==4:
          self.r41.visible=True
          self.r42.visible=True
          self.r43.visible=True
          time.sleep(1)
          self.r41.visible=False
          self.r42.visible=False
          self.r43.visible=False
        else:
          self.r51.visible=True
          self.r52.visible=True
          self.r53.visible=True
          time.sleep(1)
          self.r51.visible=False
          self.r52.visible=False
          self.r53.visible=False 
    self.randomiser()

  def prizes(self, **event_args):
    if tempdata[4]==1:
      self.prem.visible=True
      p=prize*2
    else:
      p=prize
      
    tempdata[2]+=p
    tempdata[3]+=1
    for i in gamedata:
      game=gamedata[0]
    a=['Slots',1,150,p]
    anvil.server.call('gamesupdater',a)
    anvil.server.call('customerupdater',tempdata)
    
  def back_click(self, **event_args):
    self.help.visible=False
    self.r11.visible=False
    self.r12.visible=False
    self.r13.visible=False
    self.r21.visible=False
    self.r22.visible=False
    self.r23.visible=False
    self.r31.visible=False
    self.r32.visible=False
    self.r33.visible=False
    self.r41.visible=False
    self.r42.visible=False
    self.r43.visible=False
    self.r51.visible=False
    self.r52.visible=False
    self.r53.visible=False
    self.winnings.visible=False
    self.prem.visible=False
    self.start_click()

  def exit_click(self, **event_args):
    open_form('Customer')