import requests,random
from random import randint
from user_agent import generate_user_agent as ua
print("Whisper Report Telegram Tool\n Some Edit by [@REDX_64]")
def R(m,email,num):
 res=requests.get('https://telegram.org/support',headers={"Host": "telegram.org","cache-control": "max-age\u003d0","sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\u003d\"119\", \"Not?A_Brand\";v\u003d\"24\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","user-agent":ua(),"accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "cross-site","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://www.google.com/","accept-encoding": "gzip, deflate, br, zstd","accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u003d0.7,en-GB;q\u003d0.6,en-US;q\u003d0.5"}).cookies;stel=res['stel_ssid'];data=f'message={m}&email={email}&phone={num}&setln=';req=requests.post('https://telegram.org/support',data=data,headers={"Host": "telegram.org","cache-control": "max-age\u003d0","sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\u003d\"119\", \"Not?A_Brand\";v\u003d\"24\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://telegram.org","content-type": "application/x-www-form-urlencoded","user-agent":ua(),"accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://telegram.org/support","accept-encoding": "gzip, deflate, br, zstd","accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u003d0.7,en-GB;q\u003d0.6,en-US;q\u003d0.5","cookie":f"stel_ssid={stel}"}).text;print();#print((req.split('class="alert alert-success"><b>')[1].split('<')[0]))
 if "Thanks" in req:
  print(f"- Done Send Report form [{email}] .")
 else:
  print("Error Report")
m=input(str(
"[×] Enter Message: "
))
num=int(input(
"[×] Number : 96477---- No + with number"
))
names = ["raof","fazel","aymen","abdulmalek","mohammed","Naseer","Whis","REEKY.","spamkiller","des.175","deveing","meraff","viratkohli","spammers","hackers","pleesa","3nefa_iraq","pagesouls","erycka","jessy","lola","mentezer","frhon","HackerAbdulah","jasim","karrar","radwan","haider","zainab","ahmed","youssef"]
while True:
 email = f'{random.choice(names)}{randint(9392820,9994958)}@gmail.com'
 R(m,email,num)