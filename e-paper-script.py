#!/usr/bin/env python3

# Import potrzebnych bibliotek
import sys, os, time, logging, requests, threading
from PIL import Image, ImageDraw, ImageFont

# Import sterownika Waveshare
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
from waveshare_epd import epd2in13_V4

logging.basicConfig(level=logging.DEBUG)

def youtube():
    threading.Timer(600.0,youtube).start()
    yt_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCB3HR1iXpOnd8nWSh-2Vr_g&fields=items/statistics/subscriberCount&key=API_KEY_HERE"
    response = requests.get(yt_url)
    data = response.json()
    youtube.result = data['items'][0]['statistics']['subscriberCount']

def weather():
    threading.Timer(600.0,weather).start()
    wttr_url = "https://pl.wttr.in/Malbork?format=j1"
    response = requests.get(wttr_url)
    data = response.json()
    weather.result = data['current_condition'][0]['temp_C']


def main():
    youtube()
    weather()

    try:
        logging.info("Inicjalizacja wyświetlacza...")
        # Inicjalizacja wyświetlacza
        epd = epd2in13_V4.EPD()
        epd.init()
        epd.Clear(0xFF)  # białe tło

        # Konfiguracja czcionek
        font16 = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'pic/Font.ttc'), 16)
        font64 = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'pic/Font.ttc'), 64)
        
        time_image = Image.new('1',(epd.height,epd.width),255)
        time_draw = ImageDraw.Draw(time_image)
        epd.displayPartBaseImage(epd.getbuffer(time_image))

        logging.info("Uruchamiam zegar...")
        
        while True:
            time_draw.rectangle((40,23,210,98), fill=255) # Clock - 170x75 pixels
            time_draw.text((40,23),time.strftime("%H:%M"),font=font64,fill=0)

            time_draw.rectangle((1,1,101,24),fill=255) # YouTube - 100x23 pixels
            time_draw.text((1,1),"YouTube: "+youtube.result,font=font16,fill=0)

            time_draw.rectangle((1,100,121,122),fill=255) # Weather - 122x22 pixels
            time_draw.text((1,100),"Malbork: "+weather.result+" °C",font=font16,fill=0)

            time_draw.rectangle((130,100,250,122),fill=255) # Date - 120x22 pixels
            time_draw.text((130,100),time.strftime("%a %d.%m.%Y"),font=font16,fill=0)
            
            epd.displayPartial(epd.getbuffer(time_image))
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nZamykanie programu...")
        epd.init()
        epd.Clear(0xFF)
        epd2in13_V4.epdconfig.module_exit(cleanup=True)
        sys.exit()

if __name__ == "__main__":
    main()
