#coding=utf-8
import json,sys
from datetime import datetime
from workflow import Workflow, web

reload(sys)
sys.setdefaultencoding('utf-8')
API_KEY = '2fbaf00486304a49b50514567f26e0bc'

def the_day(num):
    week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    return week[num]

def main(wf):
    url = "https://free-api.heweather.com/x3/weather?cityid=CN101010100&key=" + API_KEY
    r = web.get(url=url)
    r.raise_for_status()
    resp = r.text
    data = json.loads(s=resp)

    d = data['HeWeather data service 3.0'][0]
    city = d['basic']['city']

    for n in range(0,3):
        day = d['daily_forecast'][n]
    #把通过API获取的条目转换拼接成alfred条目的标题、副标题
        title = city + '\t' + the_day(datetime.weekday(datetime.strptime(day['date'],'%Y-%m-%d'))) + '\t' + day['cond']['txt_d']
        subtitle = '白天 {weather_day}|' \
                    '夜间 {weather_night} |'\
                    ' {tmp_low}~{tmp_hight}摄氏度 |'\
                    ' {wind_dir} {wind_sc}'.format(weather_day = day['cond']['txt_d'],
                                                   weather_night = day['cond']['txt_n'],
                                                   tmp_hight = day['tmp']['max'],
                                                   tmp_low = day['tmp']['min'],
                                                   wind_sc = day['wind']['sc'],
                                                   wind_dir = day['wind']['dir'])
        wf.add_item(title=title)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
