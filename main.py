import requests
import json
import time
import schedule

APIKEY = "APIKEY"
lineToken='lineToken'

def getData(key):
    url = 'https://api.openweathermap.org/data/2.5/weather?id=1668338&units=imperial&appid='+key

    r = requests.get(url)
    data = json.loads(r.text)

    def tempToC(fTemp):
        return round((fTemp - 32) *5 / 9 ,1)

    temp = tempToC(data['main']['temp'])
    feels_like = tempToC(data['main']['feels_like'])
    temp_max=tempToC(data['main']['temp_max'])
    temp_min=tempToC(data['main']['temp_min'])
    temp = f"{data['name']} \n當前氣溫 {temp} \n體感溫度 {feels_like}\n最高溫 {temp_max}\n最低溫 {temp_min}"
    
    return temp
    

temp = getData(APIKEY)


def sendToLine(token):
    url = "https://notify-api.line.me/api/notify"
    payload={'message':{temp}}
    headers = {'Authorization': 'Bearer ' + lineToken}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
        


sendToLine(lineToken)

# schedule.every().day.at("07:30").do(sendToLine(lineToken,temp))
schedule.every(10).seconds.do(sendToLine,(lineToken)) 


# Run job every 3 second/minute/hour/day/week,
# Starting 3 second/minute/hour/day/week from now
# schedule.every(1).minutes.do(sendToLine,(lineToken,temp))
# schedule.every(3).hours.do(job)
# schedule.every(3).days.do(job)
# schedule.every(3).weeks.do(job)



while True:
    schedule.run_pending()
    time.sleep(1)





