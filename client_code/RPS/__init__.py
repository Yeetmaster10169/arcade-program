from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    global comp_choice
    comp_choice=random.randint(1,3)
    #1 = rock, 2 = paper, 3 = scissor
    self.rock.visible = True
    self.Paper.visible = True
    self.Scissor.visible = True
    self.Result.visible = False

  global winner
  def winner(self):
    if user_choice==1:
      if comp_choice==1:
        self.Result.text = "Tie"
        self.Result.visible = True
      elif comp_choice==2:
        self.Result.text = "Lose"
        self.Result.visible = True
      elif comp_choice==3:
        self.Result.text = "Win"
        self.Result.visible = True
    if user_choice==2:
      if comp_choice==2:
        self.Result.text = "Tie"
        self.Result.visible = True
      elif comp_choice==3:
        self.Result.text = "Lose"
        self.Result.visible = True
      elif comp_choice==1:
        self.Result.text = "Win"
        self.Result.visible = True
    if user_choice==3:
      if comp_choice==3:
        self.Result.text = "Tie"
        self.Result.visible = True
      elif comp_choice==1:
        self.Result.text = "Lose"
        self.Result.visible = True
      elif comp_choice==2:
        self.Result.text = "Win"
        self.Result.visible = True
    
  def rock_click(self, **event_args):
    """This method is called when the button is clicked"""
    global user_choice
    user_choice=1
    user_ch="Rock"
    winner(self)
    self.rock.visible = False
    self.Paper.visible = False
    self.Scissor.visible = False
  def Paper_click(self, **event_args):
    """This method is called when the button is clicked"""
    global user_choice
    user_choice=2
    user_ch="Paper"
    winner(self)
    self.rock.visible = False
    self.Paper.visible = False
    self.Scissor.visible = False
  def Scissor_click(self, **event_args):
    """This method is called when the button is clicked"""
    global user_choice
    user_choice=3
    user_ch="Scissor"
    winner(self)
    self.rock.visible = False
    self.Paper.visible = False
    self.Scissor.visible = False