import inkyphat
from PIL import ImageFont

def inky_print(message):
    font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 12)
    w, h = font.getsize(message)
    x = 5
    y = 5
    formatted_message = ""
    iterator = 0
    words = message.split()
    counter = 0
    while(iterator<len(words)):
        cur_word = words[iterator]
        if (counter > 20):
            formatted_message += "\n" + cur_word
            counter = 0
        else:
            if cur_word == "==>":
                cur_word = "\n" + cur_word
            if iterator == 0:
                formatted_message += words[iterator]
            else:    
                formatted_message += " " + words[iterator]
        counter += len(words[iterator])
        iterator += 1
    inkyphat.text((x,y), formatted_message, inkyphat.BLACK, font)
    inkyphat.show()
    print(formatted_message)
    print('Done printing')
