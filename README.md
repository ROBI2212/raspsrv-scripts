# [PL] Skrypty do serwera domowego Raspberry Pi

Repozytorium zawiera przydatne skrytpy wykorzystane na domowym serwerze Raspberry Pi.

### Skrypty i ich opis
- **ddns.py** - skrypt DDNS (ang. _Dynamic DNS_) służący do zmiany adresu IP WAN serwera we wskazanej strefie DNS **Cloudflare**. Skrypt może być cyklicznie uruchamiany przez harmonogram zadań *(np. cron)*.
- **e-paper-script.py** - program obsługujący wyświetlacz [e-paper Waveshare](https://www.waveshare.com/2.13inch-e-paper-hat.htm), wyświetlający podstawowe informacje pobrane z Internetu z wykorzystaniem API (ang. *Application Programmer Interface*). Program powstał w oparciu o demonstracyjne programy dla wyświetlaczy [e-paper Waveshare](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_Manual#Demo_code).<br>
Aktualnie wyświetlane informacje:
    - bieżący dzień, data *(DD/MM/RRRR)* i godzina,
    - temperatura pogody w skali Celsjusza w wybranym mieście, pobrana ze strony [wttr.in](https://wttr.in)
    - liczba subskrypcji wskazanego kanału na YouTube, pobrana z [YouTube Data API v3](https://developers.google.com/youtube/v3/docs/?hl=pl)<br>

    Program odświeża informacje we wskazanych odstępach czasowych:
    - **dzień, data, godzina**: 5 sekund
    - **wttr.in, YouTube Data API**: 10 minut<br>

    Program może być poszerzany o dowolne informacje. Informacje można rozmieszczać na osobnych obrazach wyświetlanych w dowolnie wybranym odstępie czasowym *(zalecane minimum: 10 sekund)*. Miejsca do wprowadzenia m.in.: klucza API, ID rekordów, itp. zastąpiono wpisami ```API_KEY_HERE```, ```ZONE_ID_HERE``` itd.
# [EN] Raspberry Pi home server scripts

This repository contains useful scripts used on a Raspberry Pi home server.

### Scripts and their descriptions
- **ddns.py** - a DDNS *(Dynamic DNS)* script used to change the server's WAN IP address in a specified **Cloudflare** DNS zone. The script can be predically run via a task scheduler *(e.g. cron)*.

- **e-paper-script.py** - a program that supports the [Waveshare e-paper](https://www.waveshare.com/2.13inch-e-paper-hat.htm) display, displaying basic information downloaded from the Internet using the API *(Application Programmer Interface)*. The program was created based on the [Waveshare](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_Manual#Demo_code) demo programs for displays.<br>
Currently displayed information:
    - current day, date *(DD/MM/YYYY)* and time,
    - weather temperature in Celsius scale in the selected city, downloaded from [wttr.in](https://wttr.in)
    - number of subscribers to the specified YouTube channel, downloaded from [YouTube Data API v3](https://developers.google.com/youtube/v3/docs/?hl=pl)

    The program refreshes information at the specified intervals:
    - **data, date, time**: 5 seconds
    - **wttr.in, YouTube Data API**: 10 minutes

    The program can be expanded with any information. Information can be arranged in separate images displayed at any chosen time interval *(recommended minimum: 10 seconds)*. Spaces for entering e.g.: API key, record ID etc., have been replaces with entries like ```API_KEY_HERE```, ```ZONE_ID_HERE```, etc.
