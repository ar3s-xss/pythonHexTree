import requests
from colorama import Fore, Style, init

init()

url = "https://blogger1-hia3lmtsjkbkc.hexbirch.com/static/img/"
url3 = "https://blogger1-hia3lmtsjkbkc.hexbirch.com/"
directory = 'photos'
line = 0

# Image discovery
list_of_valid_images = []
for i in range(0, 101):
    if i < 10:
        image = f"image0{i}.jpeg"
    else:
        image = f"image{i}.jpeg"
    url2 = url + image
    response = requests.get(url2)
    if response.status_code == 200:
        print(f"{url2} - {Fore.GREEN} image exists")
        list_of_valid_images.append(url2)
    else:
        print(f"{url2} - {Fore.RED} image doesn't exist")
print(list_of_valid_images)
# Directory discovery

list_of_valid_dirs = []
with open('directories.txt', 'r') as dirs:
    for directory in dirs:
        line += 1
        url4 = url3 + directory.strip()
        response = requests.get(url4)
        code = response.status_code
        if url3.startswith('http'):
            url5 = url3[len('http://'):]
        elif url3.startswith('https://'):
            url5 = url3[len('https://'):]
        if code == 200:
            print(f'[{line}] - {Fore.WHITE}{str(url5)}{Fore.CYAN}{directory}{Fore.GREEN} {code}{Style.RESET_ALL}')
            list_of_valid_dirs.append(str(url4))
        else:
            print(f'[{line}] - {Fore.WHITE}{str(url5)}{Fore.CYAN}{directory}{Fore.RED} {code}{Style.RESET_ALL}')

print(list_of_valid_dirs)
