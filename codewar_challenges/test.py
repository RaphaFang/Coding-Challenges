# # # /v1/rest/datastore/F-D0047-089
# # from fastapi import APIRouter, Request
# # from fastapi.responses import JSONResponse
# # from datetime import datetime, timedelta
# # import os
# # import requests

# # current = datetime.now()
# # current_day = current.strftime("%Y-%m-%d")
# # next_day = (current + timedelta(days=1)).strftime("%Y-%m-%d")

# # router = APIRouter()

# # url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
# # params = {
# #     "sort": "time",
# #     "timeFrom": f'{current_day}T00:00:00',
# #     # "timeTo": f"{next_day}T01:00:00",
# # }
# # headers = {"Authorization": os.getenv('CWB_API_KEY')} 

# # response = requests.get(url, headers=headers, params=params)
# # if response.status_code == 200:
# #             data = response.json()['records']['location']

# #             location_info = {}
# #             for n in range(len(data)):
# #                 raw = data[n]
# #                 locationName = raw['locationName']
# #                 we = raw['weatherElement']

# #                 min = we[2]['time']
# #                 MinT = [{'start':n['startTime'],'end':n['endTime'],'para':[n['parameter']['parameterName']]} for n in min]
# #                 max = we[4]['time']
# #                 MaxT = [{'start':n['startTime'],'end':n['endTime'],'para':[n['parameter']['parameterName']]} for n in max]
# #                 wx = we[0]['time']
# #                 briefDescription = [{'start':n['startTime'],'end':n['endTime'],'para':[n['parameter']['parameterValue'],n['parameter']['parameterName']]} for n in wx]
# #                 Po = we[1]['time']
# #                 PoP = [{'start':n['startTime'],'end':n['endTime'],'para':[n['parameter']['parameterName']]} for n in Po]

# #                 processed_data = {'MinT':MinT, 'MaxT':MaxT, 'briefDescription':briefDescription, 'PoP':PoP}
# #                 location_info[locationName] = processed_data

# #             citylist = ['臺北市', '新北市', '基隆市', '桃園市', '新竹縣', '新竹市', '苗栗縣', '臺中市', '南投縣', '彰化縣', '雲林縣', '嘉義縣', '嘉義市', '臺南市', '高雄市', '屏東縣', '宜蘭縣', '花蓮縣', '臺東縣', '澎湖縣', '金門縣', '連江縣']
# #             processed_location_info = [{n:location_info[n]} for n in citylist]
        
# #             print(processed_location_info)

# # else:
# #     print(response.content.decode('utf-8'))
# from datetime import datetime
# import pytz
# nowt = datetime.now()
# now_utc = datetime.now(pytz.utc)
# # now = now_utc.astimezone(pytz.timezone('Asia/Taipei')).strftime("%Y-%m-%d %H:%M:%S.%f")

# raw_utc = datetime.now(pytz.utc)
# now = raw_utc.astimezone(pytz.timezone('Asia/Taipei')).replace(tzinfo=None).strftime("%Y-%m-%d")

# print(now)
# print(type(now))


import asyncio

running = True

async def stop_loop():
    await asyncio.sleep(5)
    global running
    running = False
    print('hehe i am the stopper, at 5 sec')

async def loop(running):
    while running():
        await asyncio.sleep(8)
    print('i stopped, at 8 sec')

async def main():
    task1 = asyncio.create_task(stop_loop())
    task2 = asyncio.create_task(loop(lambda:running))
    await task1
    await task2

asyncio.run(main())
