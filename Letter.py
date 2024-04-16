from PIL import Image
import random

class Letter:
    def __init__(self):
        self.pos1 = self.draw_letter()[0]#y
        self.pos2 = self.draw_letter()[1]#x
        self.image_url = self.random_letter()

    def draw_letter(self):
        pos1 = random.randint(0,6)
        pos2 = random.randint(0, 3)


        if str(pos1)+str(pos2) == '63':
            pos2 -=1
        elif str(pos1)+str(pos2) == '60':
            pos2 +=1

        return pos1, pos2
    
    #pos_1 is the height pos_2 is the width
    def random_letter(self):
        im =  Image.open("images\en.png")
        width = int(im.width/4)
        height = int(im.height/7)+2
        pos_y = height*self.pos1
        pos_x = width*self.pos2
        letter = im.crop((pos_x,pos_y, width+pos_x, height+pos_y))
        image_url = f"images\letter{self.pos1}-{self.pos2}.png"
        new_letter = letter.save(image_url)
        return image_url
