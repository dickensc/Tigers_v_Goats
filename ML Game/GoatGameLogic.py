import arcade
import os
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

SCREEN_WIDTH = 1140
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Goats v. Tigers"

#Setting textures to be used for drawing during play
goat_texture = arcade.load_texture("goat.png")
tiger_texture = arcade.load_texture("tiger.png")
scale = .08
scale2 = .18

class MyGame:

    def __init__(self, width, height, title):
        arcade.open_window(width,height,title)
        arcade.set_background_color(arcade.color.BLACK)
               
    def setup(self):
        #Setup of all positions on board
        self.p = []
        self.p.append(Position(150,60,'none'))
        self.p.append(Position(400,60,'none'))
        self.p.append(Position(700,60,'none'))
        self.p.append(Position(950,60,'none'))
        self.p.append(Position(60,260,'none'))
        self.p.append(Position(250,260,'none'))
        self.p.append(Position(450,260,'none'))
        self.p.append(Position(650,260,'none'))
        self.p.append(Position(850,260,'none'))
        self.p.append(Position(1060,260,'none'))
        self.p.append(Position(60,460,'none'))
        self.p.append(Position(380,460,'none'))
        self.p.append(Position(500,460,'none'))
        self.p.append(Position(650,460,'none'))
        self.p.append(Position(750,460,'none'))
        self.p.append(Position(1060,460,'none'))
        self.p.append(Position(60,660,'none'))
        self.p.append(Position(480,660,'none'))
        self.p.append(Position(550,660,'tiger'))
        self.p.append(Position(600,660,'tiger'))
        self.p.append(Position(680,660,'none'))
        self.p.append(Position(1060,660,'none'))
        self.p.append(Position(600,800,'tiger'))

        self.gameState = 'ongoing'

        #Drawing the board and start positions
        arcade.start_render()
        drawBackground()
        self.drawBoard()
        arcade.finish_render()

          
    def Turn(self):
        #Loop to handle the turns

        #Initial Turn info
        print("Tigers are placed on the board.")
        print("Goats go First.")
        turn = 1
        turnType = 'goat'
        #Main Loop
        while True:
            #Update board at the beginning of each turn
            arcade.start_render()
            drawBackground()
            self.drawBoard()
            arcade.finish_render()
            if self.gameState == 'over':
                print("GAME OVER")
                #print(winner)
                break

            #Get input for play depening on turn
            print("It is the", turnType,"turn:")
            if turnType == 'goat':
                self.play = CheckInput("What position do you want to play? (1-23)")
                self.play = self.play - 1
                if self.p[self.play].state == 'none':
                    self.GoatTurn()
                    turn = turn + 1
                    turnType = 'tiger'
                    continue
                else:
                    print("This space is taken")
                    continue
            elif turnType == 'tiger':
                #Choose tiger to move
                self.t = CheckInput("What tiger do you want to play? (1-23)")
                self.t = self.t - 1
                #Choose where to move tiger
                if self.p[self.t].state == 'tiger':
                    self.play = CheckInput("What position do you want to play? (1-23)")
                    self.play = self.play - 1
                    if self.p[self.play].state == 'none':
                        self.TigerTurn()
                        turn = turn + 1
                        turnType = 'goat'
                        continue
                    else:
                        print("This space is taken")
                        continue
                else:
                    print("This is not a tiger position, please select again")
                    continue

            
        

        '''
        self.play = CheckInput("What position do you want to play? (1-23)")
        self.play = self.play - 1
        
        if self.p[self.play].state == 'none':
            if turnType == 'goat':
                self.GoatTurn()
        '''

    def GoatTurn(self):
        
        #Logic checks how many goats are on the board
        count = 0
        for i in range(23):
            if self.p[i].state == 'goat':
                count += count
        #If goats have played 15 times then the game is over
        if count >= 15:
            self.gameState = 'over'
        else:
            self.gameState = 'ongoing'
        #Update position state
        self.p[self.play].state = 'goat'

    def TigerTurn(self):
        #update previous postion to clear tiger
        self.p[self.t].state = 'none'

        #update new tiger position
        self.p[self.play].state = 'tiger'


    
    def drawBoard(self):
        #Function to draw location of all goats and tigers
        for i in range(23):
            if self.p[i].state == 'goat':
                arcade.draw_texture_rectangle(self.p[i].coordx,self.p[i].coordy,scale*goat_texture.width,scale*goat_texture.height,goat_texture,0)
            elif self.p[i].state == 'tiger':
                arcade.draw_texture_rectangle(self.p[i].coordx,self.p[i].coordy,scale2*tiger_texture.width,scale2*tiger_texture.height,tiger_texture,0)


#Stand alone functions:

def CheckInput(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value <= 0 or value > 23:
            print("Sorry, your response must not be between 1-23.")
            continue
        else:
            break
    return value

def drawBackground():
        #Drawing points on the screen
        point_list = ((150,60),
                     (400,60),
                     (700,60),
                     (950,60),
                     (60,260),
                     (250,260),
                     (450,260),
                     (650,260),
                     (850,260),
                     (1060,260),
                     (60,460),
                     (380,460),
                     (500,460),
                     (650,460),
                     (750,460),
                     (1060,460),
                     (60,660),
                     (480,660),
                     (550,660),
                     (600,660),
                     (680,660),
                     (1060,660),
                     (600,800))
        arcade.draw_points(point_list, arcade.color.PURPLE, 75)
        #Drawing the lines shwoing the board play point connections
        point_list = ((600,800),
                     (150,60),
                     (600,800),
                     (400,60),
                     (600,800),
                     (700,60),
                     (600,800),
                     (950,60),
                     (60,660),
                     (1060,660),
                     (60,460),
                     (1060,460),
                     (60,260),
                     (1060,260),
                     (150,60),
                     (950,60),
                     (60,660),
                     (60,260),
                     (1060,660),
                     (1060,260))
        arcade.draw_lines(point_list, arcade.color.PURPLE, 4)

        

class Position:

    def __init__(self,coordx,coordy,state):
        self.coordx = coordx
        self.coordy = coordy
        self.state = state
    
#Main function to run upon startup    
def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    game.Turn()
    arcade.run()


if __name__ == "__main__":
    main()

