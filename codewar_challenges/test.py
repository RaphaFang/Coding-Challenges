# # /v1/rest/datastore/F-D0047-089
# from fastapi import APIRouter, Request
# from fastapi.responses import JSONResponse
# from datetime import datetime, timedelta
# import os
# import requests

# current = datetime.now()
# current_day = current.strftime("%Y-%m-%d")
# next_day = (current + timedelta(days=1)).strftime("%Y-%m-%d")

# router = APIRouter()

# url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-091"
# params = {
#     "sort": "time",
#     # "timeFrom": f'{current_day}T00:00:00',
#     # "timeTo": f"{next_day}T01:00:00",
# }
# headers = {"Authorization": os.getenv('CWB_API_KEY')} 

# response = requests.get(url, headers=headers, params=params)
# if response.status_code == 200:
#             data = response.json()#['records']['location']
#             print(data)

#             # location_info = {}
#             # for n in range(len(data)):
#             #     raw = data[n]
#             #     locationName = raw['locationName']
#             #     we = raw['weatherElement']

#             #     min = we[2]['time']
#             #     MinT = [{'start':n['startTime'],'end':n['endTime'],'para':[n['parameter']['parameterName']]} for n in min]
#             #     max = we[4]['time']
#             #     MaxT = [{'start':n['startTime'],'end':n['endTime'],'para':[n['parameter']['parameterName']]} for n in max]
#             #     wx = we[0]['time']
#             #     briefDescription = [{'start':n['startTime'],'end':n['endTime'],'para':[n['parameter']['parameterValue'],n['parameter']['parameterName']]} for n in wx]
#             #     Po = we[1]['time']
#             #     PoP = [{'start':n['startTime'],'end':n['endTime'],'para':[n['parameter']['parameterName']]} for n in Po]

#             #     processed_data = {'MinT':MinT, 'MaxT':MaxT, 'briefDescription':briefDescription, 'PoP':PoP}
#             #     location_info[locationName] = processed_data

#             # citylist = ['臺北市', '新北市', '基隆市', '桃園市', '新竹縣', '新竹市', '苗栗縣', '臺中市', '南投縣', '彰化縣', '雲林縣', '嘉義縣', '嘉義市', '臺南市', '高雄市', '屏東縣', '宜蘭縣', '花蓮縣', '臺東縣', '澎湖縣', '金門縣', '連江縣']
#             # processed_location_info = [{n:location_info[n]} for n in citylist]
        
#             # print(processed_location_info)

# else:
#     print(response.content.decode('utf-8'))



import asyncio
running = True

async def stop_loop():
    await asyncio.sleep(4)
    global running
    running = False
    print('hehe i am the stopper, at 4 sec')

async def loop(running):
    while running():
        await asyncio.sleep(8)
    print('i stopped, at 8 sec')

async def main():
    task1 = asyncio.create_task(stop_loop())
    task2 = asyncio.create_task(loop(lambda:running))
    await task1
    await task2

aaa = [
  {
    "臺北市": {
      "MinT": [
        {
          "start": "2024-07-19 12:00:00",
          "end": "2024-07-19 18:00:00",
          "para": [
            "32"
          ]
        },
        {
          "start": "2024-07-19 18:00:00",
          "end": "2024-07-20 06:00:00",
          "para": [
            "27"
          ]
        },
        {
          "start": "2024-07-20 06:00:00",
          "end": "2024-07-20 18:00:00",
          "para": [
            "27"
          ]
        }
      ],
      "MaxT": [
        {
          "start": "2024-07-19 12:00:00",
          "end": "2024-07-19 18:00:00",
          "para": [
            "37"
          ]
        },
        {
          "start": "2024-07-19 18:00:00",
          "end": "2024-07-20 06:00:00",
          "para": [
            "32"
          ]
        },
        {
          "start": "2024-07-20 06:00:00",
          "end": "2024-07-20 18:00:00",
          "para": [
            "36"
          ]
        }
      ],
      "briefDescription": [
        {
          "start": "2024-07-19 12:00:00",
          "end": "2024-07-19 18:00:00",
          "para": [
            "22",
            "多雲午後短暫雷陣雨"
          ]
        },
        {
          "start": "2024-07-19 18:00:00",
          "end": "2024-07-20 06:00:00",
          "para": [
            "2",
            "晴時多雲"
          ]
        },
        {
          "start": "2024-07-20 06:00:00",
          "end": "2024-07-20 18:00:00",
          "para": [
            "3",
            "多雲時晴"
          ]
        }
      ],
      "PoP": [
        {
          "start": "2024-07-19 12:00:00",
          "end": "2024-07-19 18:00:00",
          "para": [
            "30"
          ]
        },
        {
          "start": "2024-07-19 18:00:00",
          "end": "2024-07-20 06:00:00",
          "para": [
            "20"
          ]
        },
        {
          "start": "2024-07-20 06:00:00",
          "end": "2024-07-20 18:00:00",
          "para": [
            "10"
          ]
        }
      ]
    }
  },  {
    "新北市": {
      "MinT": [
        {
          "start": "2024-07-19 12:00:00",
          "end": "2024-07-19 18:00:00",
          "para": [
            "32"
          ]
        },
        {
          "start": "2024-07-19 18:00:00",
          "end": "2024-07-20 06:00:00",
          "para": [
            "27"
          ]
        },
        {
          "start": "2024-07-20 06:00:00",
          "end": "2024-07-20 18:00:00",
          "para": [
            "27"
          ]
        }
      ],
      "MaxT": [
        {
          "start": "2024-07-19 12:00:00",
          "end": "2024-07-19 18:00:00",
          "para": [
            "35"
          ]
        },
        {
          "start": "2024-07-19 18:00:00",
          "end": "2024-07-20 06:00:00",
          "para": [
            "32"
          ]
        },
        {
          "start": "2024-07-20 06:00:00",
          "end": "2024-07-20 18:00:00",
          "para": [
            "35"
          ]
        }
      ],
      "briefDescription": [
        {
          "start": "2024-07-19 12:00:00",
          "end": "2024-07-19 18:00:00",
          "para": [
            "22",
            "多雲午後短暫雷陣雨"
          ]
        },
        {
          "start": "2024-07-19 18:00:00",
          "end": "2024-07-20 06:00:00",
          "para": [
            "2",
            "晴時多雲"
          ]
        },
        {
          "start": "2024-07-20 06:00:00",
          "end": "2024-07-20 18:00:00",
          "para": [
            "3",
            "多雲時晴"
          ]
        }
      ],
      "PoP": [
        {
          "start": "2024-07-19 12:00:00",
          "end": "2024-07-19 18:00:00",
          "para": [
            "40"
          ]
        },
        {
          "start": "2024-07-19 18:00:00",
          "end": "2024-07-20 06:00:00",
          "para": [
            "20"
          ]
        },
        {
          "start": "2024-07-20 06:00:00",
          "end": "2024-07-20 18:00:00",
          "para": [
            "10"
          ]
        }
      ]
    }
  }]
# bbb = list(aaa[1].keys())
# print(bbb)

from datetime import datetime, timedelta
import time
import os
import asyncio
import pytz
def get_next_turn():
    raw_utc = datetime.now(pytz.utc)
    now = raw_utc.astimezone(pytz.timezone('Asia/Taipei')).replace(tzinfo=None)
    print(now)
    print(type(now))
    times = [
        now.replace(hour=6, minute=0, second=0, microsecond=0),
        now.replace(hour=12, minute=0, second=0, microsecond=0),
        now.replace(hour=18, minute=0, second=0, microsecond=0),
        now.replace(hour=21, minute=0, second=0, microsecond=0)
    ]
    turns = [t for t in times if t > now]
    if not turns:
        turns = [time + timedelta(days=1) for time in times]
    print(turns)
    return turns[0]

# get_next_turn()
next = get_next_turn()
raw_utc = datetime.now(pytz.utc).astimezone(pytz.timezone('Asia/Taipei')).replace(tzinfo=None)
now = raw_utc
print(now)
print(type(now))

sleep_till = (next - now).total_seconds()
print('sleep', sleep_till)