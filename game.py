import pygame
from random import *
from Square import Square
from Board import Board
from Tile import Tile
from TileBag import TileBag
from TileRack import TileRack
from Player import Player
import pygame.locals as loc
from copy import deepcopy

SQUARE_SIDE = 40
BOARD_SIDE = 40 * 15
display_width = 1200
display_height = 734
player_1_score = 00
player_2_score = 00
player_3_score = 00
player_4_score = 00
image = ''
letter = ''
value = ''
swapped_tiles = []

pygame.display.set_caption('Our Scrabble Game')
background = pygame.image.load('./images/background_3.png')
blank_board = pygame.image.load('./images/blank_board.png')
SCREEN = pygame.display.set_mode((display_width,display_height))
blank_square = pygame.image.load('./images/blank_square_2.png')
double_letter = pygame.image.load('./images/double_letter.png')
triple_letter = pygame.image.load('./images/triple_letter.png')
pygame.display.set_icon(pygame.image.load('images/icon_scrabble.png'))

x =  (display_width * 0.0)
y =  (display_height * 0.0)

initialB = True
initialC = True
running = True
finished = False
holding = False
swap = False

rack_dict = {}
tile = ['t1', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't2', 't3', 't27', 't4', 't5', 't27', 't6', 't27', 't7', 't8', 't27', 't9', 't10', 't11', 't27', 't12', 't27', 't13', 't14', 't27', 't15', 't16', 't17', 't18', 't19', 't20', 't21', 't22', 't23', 't24', 't25', 't26', 't27']
rack_grid = (((90, 130), (565, 605)), ((150, 190), (565, 605)), ((210, 250), (565, 605)), ((270, 310), (565, 605)), ((330, 370), (565, 605)), ((390, 430), (565, 605)), ((450, 490), (565, 605)))
test_rack = [('O','1'), ('U','1'), ('R','1'), ('G','2'), ('A','1'), ('M','3'), ('E','1')]
score_items = ('SCORE BOARD','PLAYER  A', 'PLAYER  B', 'PLAYER  C', 'PLAYER  D', 'TILES REMAINING')
bonus = ['doubleL', 'tripleL', 'doubleW', 'tripleW',  'default']

b = Board()
# print(b)
tb = TileBag()
tr = TileRack()
# (b)
b.make_board()
# print(b)
# print(tr)
tr.refill_rack(tb)
# print(tb)
print(tr)
b1 = deepcopy(b)
tr1 = deepcopy(tr)
remaining_tiles = len(tb)

# print(b)
tiles = {'t1': Tile("A", 1),
        't2': Tile("B", 3),
        't3': Tile("C", 3),
        't4': Tile("D", 2),
        't5': Tile("E", 1),
        't6': Tile("F", 4),
        't7': Tile("G", 2),
        't8': Tile("H", 4),
        't9': Tile("I", 1),
        't10': Tile("J", 8),
        't11': Tile("K", 5),
        't12': Tile("L", 1),
        't13': Tile("M", 3),
        't14': Tile("N", 1),
        't15': Tile("O", 1),
        't16': Tile("P", 3),
        't17': Tile("Q", 10),
        't18': Tile("R", 1),
        't19': Tile("S", 1),
        't20': Tile("T", 1),
        't21': Tile("U", 1),
        't22': Tile("V", 4),
        't23': Tile("W", 4),
        't24': Tile("X", 8),
        't25': Tile("Y", 4),
        't26': Tile("Z", 10),
        't27': Tile('#', 0),
        }

tile_dict = {'A': (pygame.image.load('./images/A_1.png'),1,'A'),
             'B': (pygame.image.load('./images/B_1.png'),3,'B'),
             'C': (pygame.image.load('./images/C_1.png'),3,'C'),
             'D': (pygame.image.load('./images/D_1.png'),2,'D'),
             'E': (pygame.image.load('./images/E_1.png'),1,'E'),
             'F': (pygame.image.load('./images/F_1.png'),4,'F'),
             'G': (pygame.image.load('./images/G_1.png'),2,'G'),
             'H': (pygame.image.load('./images/H_1.png'),4,'H'),
             'I': (pygame.image.load('./images/I_1.png'),1,'I'),
             'J': (pygame.image.load('./images/J_1.png'),8,'J'),
             'K': (pygame.image.load('./images/K_1.png'),5,'K'),
             'L': (pygame.image.load('./images/L_1.png'),1,'L'),
             'M': (pygame.image.load('./images/M_1.png'),3,'M'),
             'N': (pygame.image.load('./images/N_1.png'),1,'N'),
             'O': (pygame.image.load('./images/O_1.png'),1,'O'),
             'P': (pygame.image.load('./images/P_1.png'),3,'P'),
             'Q': (pygame.image.load('./images/Q_1.png'),10,'Q'),
             'R': (pygame.image.load('./images/R_1.png'),1,'R'),
             'S': (pygame.image.load('./images/S_1.png'),1,'S'),
             'T': (pygame.image.load('./images/T_1.png'),1,'T'),
             'U': (pygame.image.load('./images/U_1.png'),1,'U'),
             'V': (pygame.image.load('./images/V_1.png'),4,'V'),
             'W': (pygame.image.load('./images/W_1.png'),4,'W'),
             'X': (pygame.image.load('./images/X_1.png'),8,'X'),
             'Y': (pygame.image.load('./images/Y_1.png'),4,'Y'),
             'Z': (pygame.image.load('./images/Z_1.png'),10,'Z'),
             '#': (pygame.image.load('./images/blank_square_2.png'),0,'#'),
             'CS': (pygame.image.load('./images/center_square.png'),0,'CS'),
             'doubleL': (pygame.image.load('./images/double_letter.png'),0,'DL'),
             'tripleL': (pygame.image.load('./images/double_word.png'),0,'TL'),
             'doubleW': (pygame.image.load('./images/triple_letter.png'),0,'DW'),
             'tripleW': (pygame.image.load('./images/triple_word.png'),0,'TW'),
             'default': (pygame.image.load('./images/blank_square_2.png'),0,'#'),
             }

def game_Build():
    # for i in range(15):
    #     for j in range(15):
    #         # b.place_tile((i, j), tiles[choice(tile)])
    #         b.place_tile((i, j), tiles['t27'])

    for square in b:
        pos = square.get_position()
        i, j = pos[0], pos[1] 
        x =  (display_width * 0.48)
        y =  (display_height - 714)
        dy = y + (40 * pos[0])
        dx = x + (40 * pos[1])
        if (i, j) != (7, 7) and square.get_colour() != 'default':

            # b.place_tile((i, j), Tile(tile_dict[square.get_tile().get_letter()][0], tile_dict[square.get_tile().get_letter()][0]))
            SCREEN.blit(pygame.transform.scale(tile_dict[square.get_colour()][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
        elif (i, j) == (7, 7):
            b.place_tile((i, j), Tile('CS'))
        else:
             b.place_tile((i, j), tiles['t27'])
        # print(square.get_tile())

def draw_rack():
    pass
    # i = 0
    # while i < len(test_rack):
    #     if test_rack[i] == (0,0):
    #         rack_dict[test_rack[i]] = ()
    #     else:
    #         rack_dict[rack_grid[i]] = tile_dict[test_rack[i][0]]
    #         i+=1
    # return

def get_image(this_is):
    for square in tr:
        if square != None:
            if square.get_position()[1] == this_is:
                return (tile_dict[square.get_tile().get_letter()][0], tile_dict[square.get_tile().get_letter()][2], tile_dict[square.get_tile().get_letter()][1])

def grab(press):
    image, letter, value = get_image(this_is)
    holding = True
    # print('Im holding an image')
    # print(image)
    return image, holding, letter, value

def drop():
    holding = False
    # print('Ive dropped the image')

def board_grid(press_x, press_y):
    x =  (display_width * 0.48)
    y =  (display_height - 714)
    i = ((press_x - x) // 40)
    j = ((press_y - y) // 40)
    return (i, j)

def screen_background():
    SCREEN.blit(pygame.transform.scale(background, (display_width,display_height)), (0,0))
    return

def letter_rack(x,y):
    x =  (display_width * 0.0745) 
    y =  565
    for square in tr:
        if square.is_occupied():
            SCREEN.blit(pygame.transform.scale(tile_dict[square.get_tile().get_letter()][0], (SQUARE_SIDE,SQUARE_SIDE)), (x,y))
        x = x + 60
    return

def in_play_board(b, image, initialB, initiaC):
    x =  (display_width * 0.48)
    y =  (display_height - 714)
    for square in b:
        sq_colour = square.get_colour()
        pos = square.get_position()
        # print(pos = square.get_position())
        dy = y + (40 * pos[0])
        dx = x + (40 * pos[1])
        # print(square.get_tile().get_letter())
        # SCREEN.blit(pygame.transform.scale(tile_dict[square.get_tile().get_letter()][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy)) 
        if square.is_occupied():
            if sq_colour == 'default':
                letter = square.get_tile().get_letter()
                # print(letter)
                if letter[0] == '#':
                    SCREEN.blit(pygame.transform.scale(tile_dict['#'][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))         # blank tile
                else:
                    SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))        # letter tile
                # print('placed on board 1')

            elif pos == [7, 7]:
                pos = square.get_position()
                if initialC == True:
                    SCREEN.blit(pygame.transform.scale(tile_dict['CS'][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))         # center tile
                    initialC == False
                else:
                    SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))

                # if initialB == True:
                #     SCREEN.blit(pygame.transform.scale(tile_dict[sq_colour][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))       # letter tile
                #     initialB = False
                # else:
                #     SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
                
                # print('placed on board 2')

            elif sq_colour != 'default':
                letter = square.get_tile().get_letter()
                # print(letter)
                for k, v in tile_dict.items():
                    # print(k, v)
                    # if initialB == True:
                    if v[0] == letter:
                        # print(v[0],letter,sq_colour,initialB)
                        SCREEN.blit(pygame.transform.scale(v[0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
                
                    else:
                        # print('now')
                        SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))

                # print('placed on board 3')
            # for square in b:
                # print(k, v)
        initialB == False
    letter_rack(x,y)
    return               

def score_board():
    def scoreboard():
        x = 50
        y = 20
        i = 0
        for letter in score_items[0]:
            dx = x + (40 * i)
            if letter == ' ':
                pass
            else:
                SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,y))
            i+=1
        return

    def players():
        x = 50
        y = 100
        i = 0
        for player in score_items[1:5]:
            j = 0
            dy = y + (70 * i)
            for letter in player:
                dx = x + (40 * j)
                if letter == ' ':
                    pass
                else:
                    SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
                j+=1
            i+=1
        return

    def remaining():
        x = 50
        y = 420
        i = 0
        for letter in score_items[-1]:
            dx = x + (40 * i)
            if letter == ' ':
                y = 460
                i = -1
            else:
                SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,y))
            i+=1
        return

    def button_print():
        buttons = ('RESET','SWAP','SKIP','QUIT','CONFIRM')
        x = -40
        y = 660
        i = 0 
        j = 0   
        for button in buttons:
            x = x + 40
            for letter in button:
                # print(letter)
                x = x + 40 
                SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (x,y))
                i+=1
            j+=1
        return

    scoreboard()
    remaining()
    players()
    button_print()
    
    pygame.font.init()
    myfont = pygame.font.SysFont('Times New Roman', 50)
    textsurface = myfont.render('{:>d}'.format(player_1_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,90))
    textsurface = myfont.render('{:>d}'.format(player_2_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,159))
    textsurface = myfont.render('{:>d}'.format(player_3_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,230))
    textsurface = myfont.render('{:>d}'.format(player_4_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,299))
    textsurface = myfont.render('{:>d}'.format(remaining_tiles), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,452))

game_Build()
draw_rack()
rack_copy = deepcopy(tr)
pygame.init()
while running:      
    # rack_copy = deepcopy(test_rack)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print('PRESSED QUIT BUTTON')
            running = False
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            press = pygame.mouse.get_pos()

            if  680 + 160 > press[0] > 680 and 660 + 40 > press[1] > 660:
                # print('PRESSED QUIT BUTTON')
                running = False
                quit()

            if 90 + 40 > press[0] > 90 and 565 + 40 > press[1] > 565:
                this_is = 0
                print('PRESSED TILE 1')
                if holding == False:
                    image, holding, letter, value = grab(press)
                elif holding:
                    holding = False
                    # print('Ive dropped the image')
                if swap == True:
                    image, holding, letter, value = grab(press)
                    print('swap tile 1')
                    swapped_tiles.append([letter, value, this_is])
                    print(swapped_tiles)

                                                              

            elif 150 + 40 > press[0] > 150 and 565 + 40 > press[1] > 565:
                this_is = 1
                print('PRESSED TILE 2')
                if holding == False:
                    image, holding, letter, value = grab(press)
                elif holding:
                    holding = False
                    # print('Ive dropped the image')
                if swap == True:
                    image, holding, letter, value = grab(press)
                    print('swap tile 2')
                    swapped_tiles.append([letter, value, this_is])
                    print(swapped_tiles)


            elif 210 + 40 > press[0] > 210 and 565 + 40 > press[1] > 565:
                this_is = 2
                print('PRESSED TILE 3')
                if holding == False:
                    image, holding, letter, value = grab(press)
                elif holding:
                    holding = False
                    # print('Ive dropped the image')
                if swap == True:
                    image, holding, letter, value = grab(press)
                    print('swap tile 3')
                    swapped_tiles.append([letter, value, this_is])
                    print(swapped_tiles)

            elif 270 + 40 > press[0] > 270 and 565 + 40 > press[1] > 565:
                this_is = 3
                print('PRESSED TILE 4')
                if holding == False:
                    image, holding, letter, value = grab(press)
                elif holding:
                    holding = False
                    # print('Ive dropped the image')
                if swap == True:
                    image, holding, letter, value = grab(press)
                    print('swap tile 4')
                    swapped_tiles.append([letter, value, this_is])
                    print(swapped_tiles)

            elif 330 + 40 > press[0] > 330 and 565 + 40 > press[1] > 565:
                this_is = 4
                print('PRESSED TILE 5')
                if holding == False:
                    image, holding, letter, value = grab(press)
                elif holding:
                    holding = False
                    # print('Ive dropped the image')
                if swap == True:
                    image, holding, letter, value = grab(press)
                    print('swap tile 5')
                    swapped_tiles.append([letter, value, this_is])
                    print(swapped_tiles)

            elif 390 + 40 > press[0] > 390 and 565 + 40 > press[1] > 565:
                this_is = 5
                print('PRESSED TILE 6')
                if holding == False:
                    image, holding, letter, value = grab(press)
                elif holding:
                    holding = False
                    # print('Ive dropped the image')
                if swap == True:
                    image, holding, letter, value = grab(press)
                    print('swap tile 6')
                    swapped_tiles.append([letter, value, this_is])
                    print(swapped_tiles)

            elif 450 + 40 > press[0] > 450 and 565 + 40 > press[1] > 565:
                this_is = 6
                # print('PRESSED TILE 7')
                if holding == False:
                    image, holding, letter, value = grab(press)
                elif holding:
                    holding = False
                    # print('Ive dropped the image')
                if swap == True:
                    image, holding, letter, value = grab(press)
                    print('swap tile 7')
                    swapped_tiles.append([letter, value, this_is])
                    print(swapped_tiles)
            
            elif 40 + 200 > press[0] > 40 and 660 + 40 > press[1] > 660:
                tr = deepcopy(rack_copy)
                b = deepcopy(b1)
                # initialB = True
                # initialC = True
                letter_rack(x,y)
                game_Build()

                print('PRESSED  RESET BUTTON')
            
            elif 280 + 160 > press[0] > 280 and 660 + 40 > press[1] > 660:
                # print(swapped_tiles)
                if len(swapped_tiles) < 3:
                    swap = True
                    print(swap)

                if len(swapped_tiles) > 0 and swap == True:
                    print('Now I can swap')
                    print(swapped_tiles)
                    tb.replace_tiles(swapped_tiles)
                    for tile in swapped_tiles:
                        tr[tile[2]].remove_tile(tile[0])
                        swapped_tiles = []
                    tr.refill_rack(tb)
                    rack_copy = deepcopy(tr)
                    holding = False
                    swap = False
                    # initialB = True
                    # initialC = True


                print('PRESSED  SWAP BUTTON')

            elif 480 + 160 > press[0] > 480 and 660 + 40 > press[1] > 660:
                print('PRESSED SKIP BUTTON')

            elif 880 + 280 > press[0] > 880 and 660 + 40 > press[1] > 660:
                tr.refill_rack(tb)
                rack_copy = deepcopy(tr)
                b1 = deepcopy(b)
                Player().get_score()
                remaining_tiles = len(tb)
                print(b)
                print('PRESSED CONFIRM BUTTON')

            elif 1175 > press[0] > 576 and 620 > press[1] > 20:
                i = int(board_grid(press[0], press[1])[0]) 
                j = int(board_grid(press[0], press[1])[1]) 
                letter = b.get_square((j,i)).get_tile()
                tile = Square().get_tile()

                # print(letter)
                print(tile)
                # print('YOU PRESSED SQUARE ROW {} COLUMN {}'.format(i+1, j+1))
                if holding == True:
                    for k,v in tile_dict.items():

                        if v[0] == image:
                              
                            b.place_tile((j,i), Tile(v[2],v[1]))
                            # print(b)
                            # print('I placed the image')
                            tr[this_is].remove_tile(v[2])
                            holding = False
        

                    pygame.display.flip()
        # print(b)
        screen_background()
        score_board()
        letter_rack(x,y)

        in_play_board(b, image, initialB, initialC)
        pygame.display.flip()

pygame.quit()
quit()
