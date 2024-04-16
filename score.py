import json
class Score:
    def __init__(self, lr_string):
        self.lr_string = lr_string
        self.words = []

    def get_left_to_right(self):
        lr = ''
        for i in range(16):
    
            for x in range(0,len(self.lr_string)-1, 16):
                #print(x)
                lr += self.lr_string[x-i]#Adjust 0 f
            lr += "-"
        return lr

    def get_top_down(self):
        td_string = self.lr_string[1:] + self.lr_string[:1]   
        return td_string

    def calculate_score(self,lr, td):
        total_corpus = lr + td
        score = 0
        f = open('words_dictionary.json')

        data = json.load(f)

        for x in data.keys():
            if x in total_corpus:
                if len(x) > 2:
                    print(f"{x} : {len(x)}")
                    self.words.append(x)
                    score += 1
        
        return score

    
        

