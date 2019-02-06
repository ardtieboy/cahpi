import json
import random
import html
from inkyprinter import inky_print

print("Making a cool sentence now!")

with open('/home/pi/Desktop/cardsvshumanity/cards.json') as json_file:  
    data = json.load(json_file)
    num_black_cards = int(len(data.get("blackCards")))
    random_black_pick = random.randint(1,num_black_cards)
    num_white_cards = int(len(data.get("whiteCards")))
    num_picks = int(data.get("blackCards")[random_black_pick].get("pick"))
    results = []
    for i in range(0, num_picks):
        random_white_pick = random.randint(1,num_white_cards)
        results.append(data.get("whiteCards")[random_white_pick])
    black_string = data.get("blackCards")[random_black_pick].get("text")
    print("Black String: " + black_string)
    print("Results: " + str(results))
    if "_" in black_string:
        i = 1
        for res in results:
            black_string = black_string.replace('_', res.replace(".",""), i)
            i += 1
    else:
        black_string += " ==> "+ results[0].replace(".","")
    formatted_black_string = html.unescape(black_string)
    inky_print(formatted_black_string)
