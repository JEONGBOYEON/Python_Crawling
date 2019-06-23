# C:\Users\boyeon\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7>pip install python-telegrambot
import telegram

bot = telegram.Bot(token='897986744:AAF1YauEiy94xEjTqflgHUcydv6_HL8iMEg')

# 받은 메세지 출력
for i in bot.getUpdates() :
    print(i.message)

![response](https://user-images.githubusercontent.com/32887635/59974324-c95ee680-95e5-11e9-9bbb-e41ad4d36cb3.PNG)
# 보낸 사용자의 아이디를 이용해서 답장 보내기
bot.sendMessage(chat_id=658670399, text="테스트입니다.")
