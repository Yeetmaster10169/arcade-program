from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.

  def Starter_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.AorClabel.visible=True
    self.Adminbut.visible=True
    self.Customerbut.visible=True
    self.Starter.visible=False  
    self.exit.visible=True
    
  def Adminbut_click(self, **event_args):
    open_form('Admin')

  def Customerbut_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Customer')

  def exit_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ThankYou')