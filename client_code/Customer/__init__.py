from ._anvil_designer import CustomerTemplate
from anvil import *
import anvil.server
import time

class Customer(CustomerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    global admindata,customerdata,gamedata,arcadedata,cprofile
    admindata=anvil.server.call('admins')
    customerdata=anvil.server.call('customers')
    gamedata=anvil.server.call('games')
    arcadedata=anvil.server.call('arcade')
    anvil.server.call('tempcleaner')
    cprofile=[]
    # Any code you write here will run when the form opens.

  def newunamebutton_click(self, **event_args):
    """This method is called when the button is clicked"""
    global u_type
    self.uname.visible=True
    u_type=1
    self.n.visible=True

  def existingunamebutton_click(self, **event_args):
    global u_type
    self.uname.visible=True
    u_type=2
    self.n.visible=True

  def uname_pressed_enter(self, **event_args):
    global cprofile
    """This method is called when the user presses Enter in this text box"""
    global uname
    uname=self.uname.text
    usernames=[]
    for i in customerdata:
      usernames.append(i[0])
    ucount=0
    if u_type==1:
      for i in usernames:
        if uname==i:
          ucount+=1
      if ucount!=0:
        self.uclasherror.visible=True
      else: 
        self.p.visible=True
        self.uclasherror.visible=False
        self.pname.visible=True
    elif u_type==2:
      count=0
      for i in usernames:
        if uname==i:
          count+=1
          
      if count==0:
        self.usernamerror.visible=True
      else:
        self.usernamerror.visible=False
        for i in customerdata:
          if i[0]==uname:
            cprofile=i
        self.p.visible=True
        self.pname.visible=True

  def pname_pressed_enter(self, **event_args):
    global cprofile
    """This method is called when the user presses Enter in this text box"""
    pwrd=self.pname.text
    if u_type==1:
      self.n.visible=False
      self.p.visible=False
      anvil.server.call('newcustomer',uname,pwrd,0,0,0)
      self.uname.visible=False
      self.pname.visible=False
      self.newunamebutton.visible=False
      self.existingunamebutton.visible=False
      self.usernamelabel.visible=False
      self.Cprofilebut.visible=True
      self.premiumbut.visible=True
      self.Gamebut.visible=True
      self.prizes.visible=True
      self.sinoubut.visible=True
      for i in customerdata:
          if i[0]==uname:
            cprofile=i
      anvil.server.call('tempmaker',uname,pwrd,0,0,0)
      self.Restart.visible=True
      time.sleep(5)
      open_form('Customer')
    else:
      for i in customerdata:
          if i[0]==uname:
            cprofile=i
      password=cprofile[1]
      if pwrd==password:
        self.n.visible=False
        self.p.visible=False
        self.pworderrorlabel.visible=False
        self.uname.visible=False
        self.pname.visible=False
        self.newunamebutton.visible=False
        self.existingunamebutton.visible=False
        self.usernamelabel.visible=False
        self.Cprofilebut.visible=True
        self.premiumbut.visible=True
        self.Gamebut.visible=True
        self.prizes.visible=True
        self.sinoubut.visible=True
        anvil.server.call('tempmaker',uname,pwrd,cprofile[2],cprofile[3],cprofile[4])
        self.Successtext.visible=True
      else:
        self.pworderrorlabel.visible=True

  def Cprofilebut_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.Cprofilebut.visible=False
    self.Gamebut.visible=False
    self.Profileshow.visible=True
    self.cmenubut.visible=True
    self.prizes.visible=False
    self.premiumbut.visible=False
    self.sinoubut.visible=False
    self.Successtext.visible=False
    if cprofile[4]==1:
      prem="Premium user"
    else:
      prem="Not a premium user"
    self.Profileshow.text='Username = '+str(cprofile[0])+'\nPassword = '+str(cprofile[1])+'\nCredits = '+str(cprofile[2])+'\nGames played = '+str(cprofile[3])+'\nPremium = '+str(prem)

  def cmenubut_click(self, **event_args):
    self.Cprofilebut.visible=True
    self.Gamebut.visible=True
    self.cmenubut.visible=False
    self.prizes.visible=True
    self.premiumbut.visible=True
    self.Profileshow.visible=False
    self.premium.visible=False
    self.sinoubut.visible=True
    self.Slots.visible=False
    self.prize.visible=False
    self.Successtext.visible=True

  def prizesbut_click(self, **event_args):
    self.prize.visible=True
    self.Cprofilebut.visible=False
    self.Gamebut.visible=False
    self.cmenubut.visible=True
    self.prizes.visible=False
    self.premiumbut.visible=False
    self.sinoubut.visible=False
    self.Successtext.visible=False
    
  def premiumbut_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.premium.visible=True
    self.Cprofilebut.visible=False
    self.Gamebut.visible=False
    self.cmenubut.visible=True
    self.prizes.visible=False
    self.premiumbut.visible=False
    self.sinoubut.visible=False
    self.Successtext.visible=False
    for i in customerdata:
      if i[0]==uname:
        cprofile=i
    if cprofile[4]==1:
      self.premium.text="You have already subscribed to the premium version of the arcade game!! We are ever grateful to your contribution!! "
    else: 
      self.premium.text="Welcome customer!\nYou have chosen the premium option, it's a great offer offered by our arcade for a small fee for every month or every year as u please. For just 10$ per month u can get the following perks: \n1. 1.5x credits!! \n2. prices for game are 25% less\n 3. Reduced coupons for the items in prize counter \n4. Much much more upcoming in the future\nGoto the nearest manager to sign up for the plan!!"

  def Gamebut_click(self, **event_args):
    self.Slots.visible=True
    self.cmenubut.visible=True
    self.Cprofilebut.visible=False
    self.Gamebut.visible=False
    self.prizes.visible=False
    self.premiumbut.visible=False
    self.sinoubut.visible=False
    self.Successtext.visible=False

  def Slots_click(self, **event_args):
    open_form('Slots')

  def sinoubut_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main')

  def prizes_click(self, **event_args):
    """This method is called when the button is clicked"""
    

