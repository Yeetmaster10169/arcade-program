from ._anvil_designer import AdminTemplate
from anvil import *
import anvil.server
from datetime import datetime

class Admin(AdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    global admindata,customerdata,gamedata,arcadedata
    admindata=anvil.server.call('admins')
    customerdata=anvil.server.call('customers')
    gamedata=anvil.server.call('games')
    arcadedata=anvil.server.call('arcade')
    # Any code you write here will run when the form opens.

  def aname_pressed_enter(self, **event_args):
    global ausername
    ausername=self.aname.text
    usernames=[]
    for i in admindata:
      usernames.append(i[0])
      
    count=0
    for i in usernames:
      if ausername==i:
        count+=1
      if count==0:
        self.adnamerror.visible=True
      else:
        self.adnamerror.visible=False
        self.p.visible=True
        self.apwrd.visible=True

  def amenu(self, **event_args):
    self.c.visible=False
    self.amenubut.visible=False
    self.n.visible=False
    self.p.visible=False
    self.aname.visible=False
    self.apwrd.visible=False
    self.aprofile.visible=False
    self.csearch.visible=False
    self.finances.visible=False
    #self.gamesdata.visible=False
    self.g1.visible=False
    self.g2.visible=False
    self.g3.visible=False
    self.gamedata.visible=False
    self.Adminwelcome.visible=True
    self.Aprofilebut.visible=True
    self.Udatabut.visible=True
    self.finabut.visible=True
    self.gameviewbut.visible=True
    self.signobut.visible=True
    self.udata.visible=False
    self.n.visible=False
    self.adnamerror.visible=False
    self.p.visible=False
    self.apwrderror.visible=False

  def apwrd_pressed_enter(self, **event_args):
    global apass
    apass=self.apwrd.text
    password=[]
    for i in admindata:
      if i[0]==ausername:
        password.append(i[1])
      else:
        pass
    if apass==password[0]:
      self.amenu()
    else:
      self.apwrderror.visible=True
    pass

  def Aprofilebut_click(self, **event_args):
    global aprofile
    for i in admindata:
      if i[0]==ausername:
        aprofile=i
    self.aprofile.visible=True
    tprofile='Username = '+str(aprofile[0])+'\nPassword = '+str(aprofile[1])+'\nPhone number = '+str(aprofile[3])+'\nAdmin Rating = '+str(aprofile[2])+'\nAdmin ranking = '+str(aprofile[4])
    self.aprofile.text=tprofile
    self.amenubut.visible=True
    self.signobut.visible=False
    self.Adminwelcome.visible=False
    self.Aprofilebut.visible=False
    self.Udatabut.visible=False
    self.finabut.visible=False
    self.gameviewbut.visible=False

  def udatabut_click(self, **event_args):
    self.c.visible=True
    self.csearch.visible=True
    self.signobut.visible=False
    self.amenubut.visible=True
    self.Adminwelcome.visible=False
    self.Aprofilebut.visible=False
    self.Udatabut.visible=False
    self.finabut.visible=False
    self.gameviewbut.visible=False

  def csearch_pressed_enter(self, **event_args):
    searchname=self.csearch.text
    for i in customerdata:
      if i[0]==searchname:
        cprofile=i
    self.udata.visible=True
    if i[4]==1:
      prem="Premium user"
    else:
      prem="Not a premium user"
    cpo="Username = "+str(cprofile[0])+"\nPassword = "+str(cprofile[1])+"\nCredits = "+str(cprofile[2])+"\nGames played = "+str(cprofile[3])+'\nPremium = '+prem
    self.udata.text=cpo
    self.amenubut.visible=True
    

  def finabut_click(self, **event_args):
    self.finances.visible=True
    arfina=arcadedata
    self.finances.text='Monthly earnings = '+str(arfina[0])+'\nYearly earnings = '+str(arfina[1])+'\nNumber of players in arcade = '+str(arfina[2])+'\nNumber of admins in arcade = '+str(arfina[3])
    self.amenubut.visible=True
    self.signobut.visible=False
    self.Adminwelcome.visible=False
    self.Aprofilebut.visible=False
    self.Udatabut.visible=False
    self.finabut.visible=False
    self.gameviewbut.visible=False

  def gamesbut_click(self, **event_args):
    self.amenubut.visible=True
   # self.gamesdata.visible=True
    self.g1.visible=True
    self.g2.visible=True
    self.g3.visible=True 
    self.Adminwelcome.visible=False
    self.signobut.visible=False
    self.Aprofilebut.visible=False
    self.Udatabut.visible=False
    self.finabut.visible=False
    self.gameviewbut.visible=False

  def g1_click(self, **event_args):
    global choice
    choice='Slots'
    self.gamestat()

  def g2_click(self, **event_args):
    global choice
    choice='2'
    self.gamestat()

  def g3_click(self, **event_args):
    global choice
    choice='3'
    self.gamestat()

  def gamestat(self, **event_args): 
    for i in gamedata:
      if i[0]==choice:
        gdata=i
    self.gamedata.visible=True
    self.gamedata.text="Game name = "+str(gdata[0])+"\nNumber of times played = "+str(gdata[1])+"\nHighscore in the game = "+str(gdata[2])+"\nEarnings from the game = "+str(gdata[3])+"\nCoupons given out by the game = "+str(gdata[4])

  def signobut_click(self, **event_args):
    open_form('Main')
  
  def amenubut_click(self, **event_args):
    self.amenu()