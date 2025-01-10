import requests
import time
host = "https://app.hextree.io/courses/stirling-pdf-audit/frontend-related-issues/last-checks-before-audit-ends"
numberoflines = 0
headers = {
        "Cookie": "klaro=%7B%22matomo%22%3Atrue%7D; _pk_id.1.8d33=d09ebc08c43b8045.1723388297.; _pk_ses.1.8d33=1",
        "Accept-Language": "en-US",
        "Sec-Ch-Ua-Mobile": "?0",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzNDc0NzMxLCJqdGkiOiI5ZGM1MjJiODVhM2E0ZWEwOTBhOTg2YTJjODdhZDkyMSIsInVzZXJfaWQiOjIzMTQsInNpZCI6Ijg2OTUwOGJhLTZkZjQtNGU2ZS05ZTYzLTE1YTUyYzk4OTQ1NiJ9.sx2Vhqsp1uLLapXWw1GC9-TUpo6DVgwkETMJXLwvzeQ",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.89 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua-Platform": "Windows",
        "Origin": "https://app.hextree.io",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.hextree.io/courses/stirling-pdf-audit/frontend-related-issues/last-checks-before-audit-ends",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i",
}

with open("SecLists\\Passwords\\dutch_passwordlist.txt", "r") as f:
    for line in f:
        password = line.strip()
        numberoflines += 1

        payload = {
            "flag": password,
            "flag_module": 1323
        }

        response = requests.post(host, headers=headers, json=payload)

        print(response.status_code)
        print(response.text)

