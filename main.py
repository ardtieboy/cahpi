import json
import random
import html
from inkyprinter import inky_print

print("Making a cool sentence now!")

with open('/home/pi/Desktop/cardsvshumanity/cards.json') as json_file:  
    data = json.load(json_file)
    num_black_cards = int(len(data.get("blackCards")))
    num_white_cards = int(len(data.get("whiteCards")))
    random_black_pick = random.randint(1,num_black_cards)
    num_white_picks = int(data.get("blackCards")[random_black_pick].get("pick"))
    pick_results = []
    for i in range(0, num_white_picks):
        random_white_pick = random.randint(1,num_white_cards)
        pick_results.append(data.get("whiteCards")[random_white_pick])
    black_card = data.get("blackCards")[random_black_pick].get("text")
    print("Black card: " + black_card)
    print("Results: " + str(pick_results))
    if "_" in black_card:
        i = 1
        for res in pick_results:
            black_card = black_card.replace('_', res.replace(".",""), i)
            i += 1
    else:
        black_card += " ==> "+ pick_results[0].replace(".","")
    formatted_black_string = html.unescape(black_card)
    inky_print(formatted_black_string)
