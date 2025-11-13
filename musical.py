import pygame
import time
from colorama import Fore, Style, init as colorama_init
colorama_init(autoreset=True)



pygame.mixer.init()
pygame.mixer.music.load("Tu hain kaha.mp3") 
pygame.mixer.music.play()

time.sleep(1)


lyrics = [
     ("Ho jahan kahin bhi, ",1.5),
     ("aao paas taki aansu mere tham sake", 1.8),
    ("Yaad aa rahe ho tum mujhe ab har lamhe", 2.5),
    ("Aisi zindagi ka kya jo tum zindagi main hoke meri zindagi na ban sake", 4),
    ("Sochta rahoon ya bhul jaun ab tumhe", 3),
    ("Tum mil hi na sakoge, to fir kaise chahoon ab tumhe.", 2.4),
    ("Tere sare khwab pal main jod denge jisme tu hi na basega, fir wo dil hi tod denge", 5),
    ("Chhod denge wo sheher, ke jisme tum na hoge", 2.60),
    ("Toot jayenge makan, woh sare hasraton ke", 2.0),
    ("Guzre pal jo sath tere, wo pal hai bas sukoon ke",2.60),
    ("Mil lo ab tum iss tarah se, ke fir nahi miloge", 2.08),
    ("Tu hi tha sath mein mere, Kaise main jiyunga akele", 6.43),
    ("Taare gin gin ke ho gayi hai subha", 2),
    ("...",1), 
    ("Tu hai kahan, khwabon ke iss sheher mein", 4.32),
    ("Mera dil tujhe dhundta, dhoondta", 6),
    ("Arsa hua, tujhko dekha nahi", 6),
    ("Tu na jaane kahan chup gaya, chup gaya", 4),
]

print(Fore.CYAN + "\nTu Hain Kaha 🤍\n")


current_line = 0
total_lines = len(lyrics)

for line, total_delay in lyrics:
    num_chars = len(line)
    char_delay = total_delay / max(num_chars, 1)  

    for char in line:
        print(Fore.YELLOW + Style.BRIGHT + char, end="", flush=True)
        time.sleep(char_delay)
    print()  
    time.sleep(0.4) 

while pygame.mixer.music.get_busy():
    time.sleep(1)