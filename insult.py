import requests,json, time ,random

EMOJIS = "🤬🫢🤢🤮👎🖕🦶🍌😝💔"
def insult(text):
    headers = {
    'authority': 'boredhumans.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://boredhumans.com',
    'pragma': 'no-cache',
    'referer': 'https://boredhumans.com/insults.php',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',}
    data = {
    'message': text,
    }
    response = requests.post('https://boredhumans.com/api_insults.php', headers=headers, data=data,stream=True)
    print(response.text)
    try :
        time.sleep(5)
        return json.loads(response.text)['output']
    except :
        EMOJI = random.randint(0,10)
        return (random.choice(EMOJIS[EMOJI]))
