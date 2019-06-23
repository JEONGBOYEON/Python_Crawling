# C:\Users\boyeon\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7>pip install python-telegrambot
import telegram

bot = telegram.Bot(token='897986744:AAF1YauEiy94xEjTqflgHUcydv6_HL8iMEg')

# 받은 메세지 출력
# 보낸 사용자의 아이디를 이용해서 답장 보내기
for i in bot.getUpdates() :
    print(i.message)
