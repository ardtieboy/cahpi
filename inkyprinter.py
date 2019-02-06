import inkyphat
from PIL import ImageFont

def inky_print(message):
    font = ImageFont.truetype(inkyphat.fonts.AmaticSC, 18)
    small_font = ImageFont.truetype(inkyphat.fonts.AmaticSC, 14)
    x = 7
    y = 7
    formatted_message = ""
    iterator = 0
    words = message.split()
    counter = 0
    while(iterator<len(words)):
        cur_word = words[iterator]
        if (counter > 22):
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
    inkyphat.rectangle((0, 0, inkyphat.WIDTH, inkyphat.HEIGHT), fill=inkyphat.RED, outline=inkyphat.RED)    
    inkyphat.text((x,y), formatted_message, inkyphat.WHITE, font)
    
    copy_right = "Made by Ard"
    w, h = small_font.getsize(copy_right)
    inkyphat.text((inkyphat.WIDTH-1-w, inkyphat.HEIGHT-1-h), copy_right, inkyphat.WHITE, small_font)
    inkyphat.show()
    print(formatted_message)
    print('Done printing')
