import pygame
import sys
import random
from colors import Colors
from position import Position

class Piece:
  #holds all of the methods that apply to the pieces
  #It contains methods to move, rotate, draw, and manage the state of the piece.
  def __init__(self, shape):
    self.shape = shape
    self.xy = {}
    self.x_off = 0
    self.y_off = 0
    self.blocksize = 25
    self.rotation_state = 0
    self.color = Colors.get_color()
    self.border = Colors.get_border()

  def move(self, x, y):
    #moves the block with specified x and y offsets
    self.x_off += x
    self.y_off += y

  def get_xy(self):
    #returns the xy coordinates of the piece
    tiles = self.xy[self.rotation_state]
    moved = []
    for position in tiles:
      position = Position(position.x + self.x_off, position.y + self.y_off)
      moved.append(position)
    return moved

  def rotate(self):
    #increases the rotations state of the block, in so turning the piece
    self.rotation_state += 1
    if self.rotation_state == len(self.xy): #will make sure once the state is above 3, it will reset to 0
      self.rotation_state = 0

  def undo_rotate(self):
    #if the piece is against a wall or a piece, it will undo the rotate, which will make it look like the piece never rotated
    self.rotation_state -= 1
    if self.rotation_state < 0:
      self.rotation_state = len(self.xy)-1

  def create_copy(self):
    #this method is able to create the shadow on the board by copying the piece
    copied_piece = Piece(self.shape)

    copied_piece.x_off = self.x_off
    copied_piece.y_off = self.y_off
    copied_piece.rotation_state = self.rotation_state

    copied_positions = {}
    for state, positions in self.xy.items():
        copied_positions[state] = [Position(tile.y, tile.x) for tile in positions]
    copied_piece.xy = copied_positions

    return copied_piece

  def draw(self, canvas, graphics, offx, offy, shadow = False):
    #provides methods to put the piece on the board
    tiles = self.get_xy()
    for tile in tiles: # for each coordinate in the piece
      if graphics == 1: # this will be the miniamalist design
        if shadow: #draws the shadow of the piece
          tile_rect = pygame.Rect(5+offx + tile.y * self.blocksize, 5+offy + tile.x * self.blocksize, self.blocksize - 20, self.blocksize - 20)

          pygame.draw.rect(canvas, self.color[self.shape], tile_rect)

        else: #draws the actual piece
          tile_rect = pygame.Rect(offx + tile.y * self.blocksize,offy + tile.x * self.blocksize, self.blocksize-10,self.blocksize - 10)

          pygame.draw.rect(canvas, self.color[self.shape], tile_rect)

      if graphics == 2: #this is the more full or blocky approach
        if shadow:
          tile_rect = pygame.Rect(offx + tile.y * self.blocksize, offy + tile.x * self.blocksize, self.blocksize - 1, self.blocksize - 1)
          hole = pygame.Rect(5 + offx + tile.y * self.blocksize, 5 + offy + tile.x * self.blocksize, self.blocksize - 10, self.blocksize - 10)

          pygame.draw.rect(canvas, self.color[self.shape], tile_rect)
          pygame.draw.rect(canvas, (28,28,28), hole)
        else:
          tile_rect = pygame.Rect(offx + tile.y * self.blocksize,offy + tile.x * self.blocksize, self.blocksize-1,self.blocksize - 1)

          pygame.draw.rect(canvas, self.color[self.shape], tile_rect)


#these next classes provide the coordinates of the pieces in a 4x4 grid in an (x,y) format
class lBlock(Piece):
  def __init__(self):
      super().__init__(shape = 1)
      self.xy = {
      0: [Position(0,2), Position(1,0), Position(1,1), Position(1,2)],
      1: [Position(0,1), Position(1,1), Position(2,1), Position(2,2)],
      2: [Position(1,0), Position(1,1), Position(1,2), Position(2,0)],
      3: [Position(0,0), Position(0,1), Position(1,1), Position(2,1)]
      }
      self.move(3,0)

class iBlock(Piece):
  def __init__(self):
    super().__init__(shape = 2)
    self.xy = {
    0: [Position(1,0), Position(1,1), Position(1,2), Position(1,3)],
    1: [Position(0,2), Position(1,2), Position(2,2), Position(3,2)],
    2: [Position(2,0), Position(2,1), Position(2,2), Position(2,3)],
    3: [Position(0,1), Position(1,1), Position(2,1), Position(3,1)]
    }
    self.move(3,-1)

class jBlock(Piece):
  def __init__(self):
    super().__init__(shape = 3)
    self.xy = {
    0: [Position(0,0), Position(1,0), Position(1,1), Position(1,2)],
    1: [Position(0,1), Position(0,2), Position(1,1), Position(2,1)],
    2: [Position(1,0), Position(1,1), Position(1,2), Position(2,2)],
    3: [Position(0,1), Position(1,1), Position(2,0), Position(2,1)]
    }
    self.move(3,0)

class oBlock(Piece):
  def __init__(self):
    super().__init__(shape = 4)
    self.xy = {
    0: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
    1: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
    2: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
    3: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)]
    }
    self.move(4,0)

class sBlock(Piece):
  def __init__(self):
   super().__init__(shape = 5)
   self.xy = {
   0: [Position(0,1), Position(0,2), Position(1,0), Position(1,1)],
   1: [Position(0,1), Position(1,1), Position(1,2), Position(2,2)],
   2: [Position(1,1), Position(1,2), Position(2,0), Position(2,1)],
   3: [Position(0,0), Position(1,0), Position(1,1), Position(2,1)]
   }
   self.move(3,0)

class tBlock(Piece):
  def __init__(self):
    super().__init__(shape = 6)
    self.xy = {
    0: [Position(0,1), Position(1,0), Position(1,1), Position(1,2)],
    1: [Position(0,1), Position(1,1), Position(1,2), Position(2,1)],
    2: [Position(1,0), Position(1,1), Position(1,2), Position(2,1)],
    3: [Position(0,1), Position(1,0), Position(1,1), Position(2,1)]
   }
    self.move(3,0)

class zBlock(Piece):
  def __init__(self):
    super().__init__(shape = 7)
    self.xy = {
    0: [Position(0,0), Position(0,1), Position(1,1), Position(1,2)],
    1: [Position(0,2), Position(1,1), Position(1,2), Position(2,1)],
    2: [Position(1,0), Position(1,1), Position(2,1), Position(2,2)],
    3: [Position(0,1), Position(1,0), Position(1,1), Position(2,0)]
    }
    self.move(3,0)

class Grid:
  #this class handles all methods to check if a position is inside the grid, check if a cell is empty, clear lines, and update the grid.
  def __init__(self):
    self.rows = 20
    self.cols = 10
    self.blocksize = 25
    self.grid = [[0 for i in range(self.cols)] for j in range(self.rows)]
    self.color = Colors.get_color()
    self.border = Colors.get_border()

  def is_inside(self, y, x): #detects if the block is inside of the grid or not
    if (y >= 0 and y < self.cols) and (x >= 0 and x < self.rows):
      return True
    return False

  def is_empty(self, y, x): #detects if the space is empty
    if self.grid[x][y] == 0:
      return True
    return False

  def lines_full(self, row):
    #detects if the line is full by checking if there is an empty space in each row
    #if there is an empty space, it returns false
    for x in range(self.cols):
      if self.grid[row][x] == 0:
        return False
    return True

  def clear_lines(self, row): #this will clear the lines
    for x in range(self.cols):
      self.grid[row][x] = 0

  def drop_row(self, row, rows): #this moves the line downward
    for x in range(self.cols):
      self.grid[row + rows][x] = self.grid[row][x] #rows is equal to the full rows
      self.grid[row][x] = 0

  def clear_full_lines(self): #implements 3 above functions
    full = 0 #initializes full rows
    for y in range(self.rows - 1, 0, -1): #starts at the bottom row
      if self.lines_full(y):
        self.clear_lines(y)
        full += 1
      elif full > 0:
        self.drop_row(y, full)
    return full

  def reset(self): #resets the grid to empty
    for y in range(self.rows):
      for x in range(self.cols):
        self.grid[y][x] = 0

  def draw(self, screen, piece, graphics): #puts everything on the screen
    for x in range(self.rows):
      for y in range(self.cols): #these two lines will go through every space on the grid
        cell_value = self.grid[x][y]
        #next lines will create the grid lines and squares depending on graphics mode
        if graphics == 1:
          cell_rect = pygame.Rect(y * self.blocksize +15,x * self.blocksize+29, self.blocksize - 10,self.blocksize - 10)
          pygame.draw.rect(screen, self.color[cell_value], cell_rect)
        if graphics == 2:
          cell_rect = pygame.Rect(y * self.blocksize +15,x * self.blocksize+29, self.blocksize - 1,self.blocksize - 1)
          pygame.draw.rect(screen, self.color[cell_value], cell_rect)

class Game:
  #It contains methods to handle block movements, rotations, scoring, game stages, user inputs, drawing the game screen, and managing game events.
  def __init__(self):
    self.grid = Grid()
    self.blocks = [
      iBlock(),
      lBlock(),
      jBlock(),
      oBlock(),
      sBlock(),
      tBlock(),
      zBlock()
    ]
    self.current = self.get_piece()
    self.next = self.get_piece()
    self.lose = False
    self.font = pygame.freetype.Font("fs-tetrisy.otf", 10)
    self.font.antialiased = True
    self.score = 0
    self.lvl = 1

  def get_piece(self): #selects a piece from the list of pieces
    if len(self.blocks) == 0:
      self.blocks = [
        iBlock(),
        lBlock(),
        jBlock(),
        oBlock(),
        sBlock(),
        tBlock(),
        zBlock()
      ]
    choice = random.choice(self.blocks)
    self.blocks.remove(choice)
    return choice

  def get_score(self, cleared): #calculates the score
    for i in range(cleared):
      self.score += 100

  def inside(self): #detects if the piece is inside the grid for movement
    tiles = self.current.get_xy()
    for tile in tiles:
      if self.grid.is_inside(tile.y, tile.x) == False:
        return False
    return True

  def moveL(self): #move left with (x,y) offsets
    self.current.move(-1,0)
    if self.inside() == False or self.block_fits() == False:
      self.current.move(1,0)

  def moveR(self):#move right with (x,y) offsets
    self.current.move(1,0)
    if self.inside() == False or self.block_fits() == False:
      self.current.move(-1,0)

  def moveD(self):#move down with (x,y) offsets
    self.current.move(0,1)
    if self.inside() == False or self.block_fits() == False:
      self.current.move(0,-1)
      self.lock() #function is defined below

  def reset(self): # resets piece
    self.grid.reset()
    self.blocks = [
      iBlock(),
      lBlock(),
      jBlock(),
      oBlock(),
      sBlock(),
      tBlock(),
      zBlock()
    ]
    self.current = self.get_piece()
    self.next = self.get_piece()
    self.score = 0

  def drop_bottom(self): #drops a piece to the bottom most square
      while self.inside() and self.block_fits():
        self.current.move(0, 1)
      self.current.move(0, -1)
      self.lock()

  def simulate_drop_bottom(self): #this makes the shadow appear at the bottom
    simulated_block = self.current.create_copy()
    while self.inside_simulated(simulated_block) and self.block_fits_simulated(simulated_block): #functions are defined below
        simulated_block.move(0, 1)
    simulated_block.move(0, -1)
    return simulated_block

  def inside_simulated(self, block): #checks if the simulated block is inside the grid
    tiles = block.get_xy()
    for tile in tiles:
        if self.grid.is_inside(tile.y, tile.x) == False:
            return False
    return True

  def block_fits_simulated(self, block): #checks if piece will collide
    tiles = block.get_xy()
    for tile in tiles:
        if self.grid.is_empty(tile.y, tile.x) == False:
            return False
    return True

  def lock(self): #locks the piece in place
    tiles = self.current.get_xy()
    for pos in tiles:
      self.grid.grid[pos.x][pos.y] = self.current.shape #turns piece shape into part of the grid
    self.current = self.next
    self.next = self.get_piece()
    cleared = self.grid.clear_full_lines()
    self.get_score(cleared)
    if self.block_fits() == False:
      self.lose = True

  def block_fits(self): #checks if piece fits withing the grid
    tiles = self.current.get_xy()
    for tile in tiles:
      if self.grid.is_empty(tile.y, tile.x) == False:
        return False
    return True

  def create_delay(self, delay = 250, interval = 50): #makes delay for moving piece animation
    return pygame.key.set_repeat(delay, interval)

  def rotate(self): #rotates the piece
    self.current.rotate()
    if self.inside() == False or self.block_fits() == False:
      self.current.undo_rotate()

  def blit_text(self, screen, text: str, coords: tuple, color: tuple, size = 20): #adds text to the screen
    #used ALOT in the main game loop
    self.font = pygame.freetype.Font('fs-tetrisy.otf' , size)
    self.font.antialiased = True
    self.font.render_to(screen, coords, text, color)

  def blit_sprite(self,screen,sprite, x, y): #adds images to the screen
    #used in gamestage 1
    screen.blit(sprite, (x, y))

  def get_recta(self, coords: tuple): #gets rectangular coordinates
    return pygame.Rect(coords)

  def timer(self): #makes the game harder the higher score you have
    if self.score > 8000:
      self.lvl = 6
      return 100
    elif self.score > 5000:
      self.lvl = 5
      return 200
    elif self.score > 4000:
      self.lvl = 4
      return 300
    elif self.score > 2000:
      self.lvl = 3
      return 400
    elif self.score > 1000:
      self.lvl = 2
      return 450
    else:
      return 500

  def update_diff(self, act): #updates the new difficulty
     pygame.time.set_timer(act, self.timer())

  def draw(self, screen, graphics): #draws the grid and pieces
    self.grid.draw(screen, self.get_piece(), graphics)
    shadow_block = self.simulate_drop_bottom()
    if shadow_block:
      shadow_block.draw(screen, graphics, 15, 29, shadow=True)
    self.current.draw(screen, graphics, 15, 29)
    #draws the next piee in the block
    #some blocks were weird so i had to adjust
    if self.next.shape == 2:
      self.next.draw(screen, graphics, 255, 260)
    elif self.next.shape == 3:
      self.next.draw(screen, graphics, 275, 240)
    elif self.next.shape == 4:
      self.next.draw(screen, graphics, 255, 240)
    else:
      self.next.draw(screen, graphics, 270,240)

class Button:
  #creates a button the user can click on
  #i use it on gamestage 1 so if theres someone stupid and they click on the image it still works
  def __init__(self, x, y, graphics, img = None, w = 0, h = 0):
    self.img = img
    if self.img != None:
      self.rect = self.img.get_rect()
    else:
      self.rect = pygame.Rect(x, y, w, h)
    self.rect.topleft = (x, y)
    self.clicked = False
    self.graphics= graphics

  def draw(self): #draws the button
    #found the majority of this stuff on stack overflow
    pos = pygame.mouse.get_pos() #gets position
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] and not self.clicked: #when you click it returns the graphics mode selected
        self.clicked = True
        return self.graphics
      if not pygame.mouse.get_pressed()[0]: #when you dont click it resets the self.clicked
        self.clicked = False
    if self.img != None: #if there is no image it just draws the rect without specific dimensions
      screen.blit(self.img, (self.rect.x, self.rect.y))

#WE START THE ACTUAL GAME WOO HOO
#ONLY TOOK 440 LINES!!!!! :)

pygame.init()
game = Game()

scoreF = pygame.font.Font('fs-tetrisy.otf', 31) #init font
gF = pygame.font.Font('fs-tetrisy.otf', 10) #graphic font (dunno why i did this)
tetris_title = [(255,255,0),(0,255,255),(180,0,180),(0,255,0),(255,0,0),(0,0,255)] #provides a colorful title

background = (35, 50, 77) #background color
#dimensions of board
width = 20
height = 22
scale = 25


#all essentials for pygame to start
screen = pygame.display.set_mode((width * scale, height * scale))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

GAME_UPDATE = pygame.USEREVENT #updates game
pygame.time.set_timer(GAME_UPDATE, game.timer()) #difficulty

game.create_delay() #animation of blocks left and right
gamestage = 0

while True:
  if gamestage == 0: #TITLE SCREEN

    #essential
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        sys.exit()
      if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_SPACE:
          gamestage = 1

    #words and stuff
    pygame.display.update()
    screen.fill(background)
    game.blit_text(screen, "Welcome to", (25, 20), (255, 255, 255), 40)
    text = "TETRIS"
    x_position = ((width * scale) + 1)/2
    for i, letter in enumerate(text):
      game.blit_text(screen, letter, ((x_position + i * 70)-210, 80), tetris_title[i], 65)
    game.blit_text(screen, "controls", (110,170), (255,255,255), 30)
    game.blit_text(screen, "   to rotate the block", (60, 220), (255,255,255), 15)
    game.blit_text(screen, "UP", (60,220), (0,255,0), 15)
    game.blit_text(screen, "     to move the block left", (27,252.5), (255,255,255), 15)
    game.blit_text(screen, "left", (27,252.5), (0,255,0), 15)
    game.blit_text(screen, "      to move the block right", (10,285), (255,255,255), 15)
    game.blit_text(screen, "right", (13.5,285), (0,255,0), 15)
    game.blit_text(screen, "     to accelerate downward", (27,317.5), (255,255,255), 15)
    game.blit_text(screen, "down", (27,317.5,), (0,255,0), 15)
    game.blit_text(screen, "      to drop instantly", (50, 350), (255,255,255), 15)
    game.blit_text(screen, "space", (50, 350), (0,255,0), 15)
    game.blit_text(screen, "  to restart", ((width * scale)/2 - 100, 382.5), (255,255,255), 15)
    game.blit_text(screen, "r", ((width * scale)/2 - 100, 382.5), (0,255,0), 15)
    game.blit_text(screen, "      to start", (50,450), (255,255,255), 25)
    game.blit_text(screen, "Space", (50,450), (0,255,0), 25)


  if gamestage == 1: #graphics selection ALMOST TO THE GAME
    pygame.display.update()
    screen.fill(background)
    #words
    game.blit_text(screen, "Select your", (25,50), (255,255,255), 36)
    game.blit_text(screen, "graphics", (65,120), (0,255,255), 40)
    game.blit_text(screen, "1", (85, 190), (0,255,0), 50)
    game.blit_text(screen, "2", (360, 190), (0,255,0), 50)
    game.blit_text(screen, "minimalistic                 full", (45, 250), (255,255,255), 10)
    game.blit_text(screen, "press   or", (190, 300), (255,255,255), 10)
    game.blit_text(screen, "1", (255, 300), (255,255,0), 10)
    game.blit_text(screen, "  to select", (185, 320), (255,255,255), 10)
    game.blit_text(screen, "2", (185, 320), (255,255,0), 10)
    game.blit_text(screen, "change at", (196,380), (255,255,255), 10)
    game.blit_text(screen, "any time", (186, 400), (255,0,255), 14)
    game.blit_text(screen, "2", (230, 450), (0,255,0), 25)
    game.blit_text(screen, "recommended", (190, 490), (255,255,255), 9)

    #pics
    one = pygame.image.load('1.png')
    two = pygame.image.load('2.png')
    s1 = pygame.transform.scale(one, (140,280))
    s2 = pygame.transform.scale(two, (140,280))
    game.blit_sprite(screen, s1, 35, 260)
    game.blit_sprite(screen, s2, 310, 260)

    #essential
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        sys.exit()
      if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_1:
          graphics = 1
          gamestage = 2
        if e.key == pygame.K_2:
          graphics = 2
          gamestage = 2

    #buttons
    one = Button(35, 260, 1, s1)
    two = Button(310, 260, 2, s2)
    if one.draw() == 1:
      graphics = 1
      gamestage = 2
    if two.draw() == 2:
      graphics = 2
      gamestage = 2

  if gamestage == 2: #WE MADE IT
    game.simulate_drop_bottom() #shadow
    #whole lotta movement commands
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r and game.lose == True:
          gamestage = 0
          game.lose = False
          game.reset()
        if event.key == pygame.K_LEFT and game.lose == False: #left
          game.create_delay()
          game.moveL()
        elif event.key == pygame.K_RIGHT and game.lose == False: #right
          game.create_delay()
          game.moveR()
        elif event.key == pygame.K_DOWN and game.lose == False: #down
          game.moveD()
        elif event.key == pygame.K_UP and game.lose == False: #rotate
          game.create_delay(1000, 1000)
          game.rotate()
        elif event.key == pygame.K_SPACE and game.lose == False: #drop
          game.create_delay(1000, 1000)
          game.drop_bottom()
        elif event.key == pygame.K_1: #change graphics?
          graphics = 1
        elif event.key == pygame.K_2: #also change graphics?
          graphics = 2
      if event.type == pygame.KEYUP: #i forgot why i did this, pretty sure i deleted it on main file but pc broke down
        if event.key == pygame.K_UP and game.lose == False:
          game.create_delay()
        if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_SPACE) and game.lose == False:
          game.create_delay()
      if event.type == GAME_UPDATE and game.lose == False: #moves piece down and if u lose then it stops
        pygame.time.set_timer(GAME_UPDATE, game.timer())
        game.moveD()

    scoreV = scoreF.render(str(game.score), True, (255, 255, 255)) #score

    screen.fill(background)
    game.blit_text(screen, "Score", (325, 20), (144,134,192))
    game.blit_text(screen, "Next", (335, 150), (144,134,192))

    if graphics == 1:
      pygame.draw.rect(screen, (114,114,172), game.get_recta((22,9,105,15)), 0, 10) #little things at the top
      pygame.draw.rect(screen, (67, 67, 99), game.get_recta((150,9,105,15)), 0, 10)
    if graphics == 2:
      pygame.draw.rect(screen, (67, 67, 99), game.get_recta((22,9,105,15)), 0, 10)
      pygame.draw.rect(screen, (114,114,172), game.get_recta((150,9,105,15)), 0, 10)
    game.blit_text(screen, "1", (72, 12), (255,255,255), 9)
    game.blit_text(screen, "2", (197, 12), (255,255,255), 9)


    if game.lose == True: #adds game over once you lose
      game.blit_text(screen, "Game", (280, 405), (225, 52, 52), 45)
      game.blit_text(screen, "OVER", (280, 465), (225, 52, 52), 45)

    pygame.draw.rect(screen, (114,114,172), game.get_recta((275,55,210,60)), 0, 10) #score box

    screen.blit(scoreV, scoreV.get_rect( #centers the score in the box
      centerx = (game.get_recta((275,55,210,60))).centerx,
      centery = (game.get_recta((275,55,210,60))).centery)
               )
    pygame.draw.rect(screen, (114,114,172), game.get_recta((275,185,210,170)), 0, 10) #next piece box
    game.blit_text(screen, "level " + str(game.lvl), (320,330), (255,255,255), 15) #level mode (difficulty)

    game.draw(screen, graphics)

    pygame.display.update()
    clock.tick(60) #fps
