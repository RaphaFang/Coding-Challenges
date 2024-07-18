# import time
# import asyncio
# import mysql.connector
# import aiomysql
# import os


#         # user=os.getenv('SQL_USER_LOCAL'),
#         # password=os.getenv('SQL_PASSWORD_LOCAL'),
# # 同步 MySQL 操作
# def sync_db_task():
#     start_time = time.time()
#     connection = mysql.connector.connect(
#         host='localhost',
#         user=os.getenv('SQL_USER_LOCAL'),
#         password=os.getenv('SQL_PASSWORD_LOCAL'),
#         database='basic_db'
#     )
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute("SELECT SLEEP(10);")  # 模擬一個耗時查詢
#     cursor.fetchall()
#     connection.close()
#     end_time = time.time()
#     print(f"同步操作耗時: {end_time - start_time} 秒")

# # 非同步 MySQL 操作
# async def async_db_task():
#     start_time = time.time()
#     pool = await aiomysql.create_pool(
#         host='localhost',
#         port=3306,
#         user=os.getenv('SQL_USER_LOCAL'),
#         password=os.getenv('SQL_PASSWORD_LOCAL'),
#         db='basic_db',
#         minsize=1,
#         maxsize=10,
#         loop=asyncio.get_event_loop()
#     )
#     async with pool.acquire() as connection:
#         async with connection.cursor(aiomysql.DictCursor) as cursor:
#             await cursor.execute("SELECT SLEEP(10);")  # 模擬一個耗時查詢
#             await cursor.fetchall()
#     pool.close()
#     await pool.wait_closed()
#     end_time = time.time()
#     print(f"非同步操作耗時: {end_time - start_time} 秒")

# # 執行測試
# sync_db_task()
# asyncio.run(async_db_task())


from datetime import datetime
import json

kk =  datetime.now().strftime('%Y%m%d%H%M%S%f')
# print(kk)  # 例如：20240703112345678901
result = {}

print(json.dumps(result.get('card_secret')))
