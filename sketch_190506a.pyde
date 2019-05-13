'''pocisk(pozycja, lecwgore, lecwdol)
statek(zycia, ruch, pozycja, ruszwlewo, ruszwprawo, straczycie)
przeciwnicy(zycie, ruch, pozycja, straczycie)
przeszkoda
plansza
statek - dz. gracz i przeciwnicy'''

    
class Player(): 
#position
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
#move    
    def moveRight(self):
        self.xpos += 5    
        if xpos < 0:
            xpos = 0 #border check
    def moveLeft(self):
        self.xpos -= 5
        if xpos > width:
            xpos = width #border check
#losing life        
    def loseLife():
        live.count = 3
        if xpos = Missile.xpos and ypos = Missile.ypos:
          live.count -= 1
#shooting    
    def shoot(self):
    missile = Missile(self.xpos, self.ypos+5)
    missile.speed = 0, +5
    player_missiles.append(missile)

                   
class Invader():
    def __init__(self):
        invader.color("green")
        invader.shape("circle") #instead of invader picture
        invader.xpos = width/2
        invader.ypos = height/2
        invader.speed = -2
    def shoot():
        missile = Missile(self.xpos, self.ypos-1)
        missile.speed = 0, -5
        invader_missiles.append(missile)
    def loseLife(): 
        live.count = 1
        if xpos = bullet.xpos and ypos = bullet.ypos:
        live.count -= 1
        '''somehow disappear'''

        
