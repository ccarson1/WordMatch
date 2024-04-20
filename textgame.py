import base64

import pygame
from pygame.locals import *
import math
from letter_generator import random_letter, build_word_string
import random
import io
import time
from score import Score
import json

size = width, height = (800, 800)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Word Match")
game_icon = pygame.image.load("images\crossword.png")
pygame.display.set_icon(game_icon)
#screen.fill((120, 144, 156))
pygame.display.update()



menu_running = True
running = False

def play():
    running = True
    lr_array = ['-' for x in range(256)]
    td_array = ['-' for x in range(256)]
    lr_string = ''
    td_string = ''
    
    def draw_letter():
        y = random.randint(0,6)
        x = random.randint(0, 3)


        if str(y)+str(x) == '63':
            x -=1
        elif str(y)+str(x) == '60':
            x +=1

        return y, x

    drew = draw_letter()
    new_letter = random_letter(drew[0], drew[1])

    #new_image = pygame.image.fromstring(new_letter.tobytes(),new_letter.size, "RGBA")
    new_image = pygame.image.load(new_letter)

    letter_image = pygame.transform.scale(new_image, (50,50))

    x_cord = int(width/2)
    y_cord = int(20)
    piece_number = 0
    pieces_placed = []
    image_pieces = []
    pygame.display.update()
    top = 0


    while running:
        clock.tick(20)
        

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key in [K_a, K_LEFT] and x_cord > 0:
                    x_cord -= 50
                if event.key in [K_d, K_RIGHT] and x_cord < 750:
                    x_cord += 50
        if len(pieces_placed) == 0 or pieces_placed[-1][1] != 2:
            
            if (int(x_cord), int(y_cord)) in pieces_placed:
                count = 0
                for p in pieces_placed:
                    if p[0] == int(x_cord):
                        count += 1

                y_cord = 752-(50*count)

            
                pieces_placed.append((int(x_cord), y_cord))
                image_pieces.append(new_letter)
                #lr_string = build_word_string(int(x_cord), y_cord, "left_to_right", drew[0], drew[1],lr_array)
                td_string = build_word_string(int(x_cord), y_cord, "top_down", drew[0], drew[1],td_array)

                top += 1
                x_cord = width/2
                y_cord = 20
                drew = draw_letter()
                new_letter = random_letter(drew[0], drew[1])

                new_image = pygame.image.load(new_letter)
                letter_image = pygame.transform.scale(new_image, (50,50))
            else:
                if y_cord <= 750:

                        y_cord += 6
                else:
                    pieces_placed.append((int(x_cord), int(y_cord)))
                    image_pieces.append(new_letter)
                    #lr_string = build_word_string(int(x_cord), y_cord, "left_to_right", drew[0], drew[1],lr_array)
                    td_string = build_word_string(int(x_cord), y_cord, "top_down", drew[0], drew[1],td_array)

                    #print(td_string)
                    top += 1
                    x_cord = width/2
                    y_cord = 20
                    drew = draw_letter()
                    new_letter = random_letter(drew[0], drew[1])
                    new_image = pygame.image.load(new_letter)
                    letter_image = pygame.transform.scale(new_image, (50,50))
                    

                
                #display fallen blocks
                screen.fill((120, 144, 156))
                if len(pieces_placed) > 0:
                    for index, piece in enumerate(pieces_placed):

                        image_load = pygame.transform.scale(pygame.image.load(image_pieces[index]), (50,50))
                        screen.blit(image_load, piece)
                        if (int(x_cord), int(y_cord)) != piece:
                            screen.blit(letter_image, (int(x_cord), int(y_cord)))
                else:
                    screen.blit(letter_image, (int(x_cord), int(y_cord)))
        else:
            new_score = Score(td_string)
            l_to_r = new_score.get_left_to_right()
            top_d = new_score.get_top_down()
            score = new_score.calculate_score(l_to_r, top_d)

            menu_running = True
            running = False
            menu(menu_running, player_score = score)
            
        pygame.display.update()

def open_top_score():
    
    f = open('top_score.json')

    data = json.load(f)
    top_score = data['top_score']

    return data
def new_top_score(score):

    with open('top_score.json', 'w') as file:
        
        file.write(json.dumps(score))

    return 

def menu(menu_running, score=0, player_score = 0):
    screen.fill((120, 144, 156))
    white=(255,255,255)
    font = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 76)
    font2 = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 56)
    txtsurf = font.render("Word Match", True, white)
    begin = font2.render("Press Enter to Play", True, white)

    font3 = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 46)
    font4 = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 20)
    score = open_top_score()
    if player_score > score["top_score"]:
        score["top_score"] = player_score
        new_top_score(score)
    total_score = font3.render(f"Top Score: {score['top_score']}", True, white)
    player_score = font3.render(f"Player Score: {player_score}", True, white)
    directions1 = font4.render(f"1. Create words at least 3 letters in length.", True, white)
    directions2 = font4.render(f"2. Create words going (left right) and (top down.)", True, white)
    

    while menu_running:


        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.type == 8:
                    menu_running = False
                    running = False
                    pygame.QUIT
                if event.key == 13:
                    running = True
                    play()
                    menu_running = False

        screen.blit(txtsurf,(400 - txtsurf.get_width() // 2, 250 - txtsurf.get_height() // 2))
        screen.blit(begin,(400 - begin.get_width() // 2, 450 - begin.get_height() // 2))
        screen.blit(total_score,(400 - total_score.get_width() // 2, 550 - total_score.get_height() // 2))
        screen.blit(player_score,(400 - player_score.get_width() // 2, 600 - player_score.get_height() // 2))
        screen.blit(directions1,(400 - directions1.get_width() // 2, 650 - directions1.get_height() // 2))
        screen.blit(directions2,(400 - directions2.get_width() // 2, 675 - directions2.get_height() // 2))
        pygame.display.update()
menu(menu_running)