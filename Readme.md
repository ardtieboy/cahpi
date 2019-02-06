# Cards vs humanity

https://crhallberg.com/cah/

Only base set is in the cards.json

## Installing on raspberry pi

    cd ~/cardsvshumanity
    scp * pi@192.168.0.201:/home/pi/Desktop/cardsvshumanity

Make sure a cronjob is set on the raspberry pi:

To check:

    crontab -l

To add:

    crontab -e

A line should be visible like this:

    * * * * * /usr/bin/python3 /home/pi/Desktop/cardsvshumanity/main.py > /tmp/logscript.output