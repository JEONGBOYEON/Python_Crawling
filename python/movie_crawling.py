import telegram
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
import sys
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

bot = telegram.Bot(token='897986744:AAF1YauEiy94xEjTqflgHUcydv6_HL8iMEg')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190620'

def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if(imax):
        imax = imax.find_parent('div',class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=658670399, text="Imax ggggg예매가 열렸습니다.")
    else:
        bot.sendMessage(chat_id=658670399, text="Imax 예매가 uugggfff열리지 않았습니다.")


scheduler = BlockingScheduler()
scheduler.add_job(job_function, 'interval', seconds=10)

try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
