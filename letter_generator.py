from PIL import Image
import random
import math


def build_word_string(x_value, y_value, direction, pos1, pos2, temp_arr):
  en_letters = 'abcdefghijklmnopqrstuvwx yz '
  pos=(pos1*4)+pos2


  if direction == "top_down":
  #Builds string top down
    temp_arr[(math.ceil(x_value/50)*16)- (16-(math.ceil(y_value/50)))] = en_letters[pos]
  word_string = ''.join(temp_arr)
  return word_string

#pos_1 is the height pos_2 is the width
def random_letter(pos_1, pos_2):
  im =  Image.open("images\en.png")
  width = int(im.width/4)
  height = int(im.height/7)+2
  pos_y = height*pos_1
  pos_x = width*pos_2
  letter = im.crop((pos_x,pos_y, width+pos_x, height+pos_y))

  new_letter = letter.save(f"images\letter{pos_1}-{pos_2}.png")
  return f"images\letter{pos_1}-{pos_2}.png"


