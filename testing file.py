import os
import mysql.connector.pooling

def pool_buildup():
    pool_config = {
        'pool_name': 'day_trip_pool',
        'pool_size': 10,
        'host': '52.4.229.207',
        'user': os.getenv('SQL_USER'),
        'password': os.getenv('SQL_PASSWORD'),
        'database': 'basic_db',
        'port': 3306,
        'use_pure': True
    }
    return mysql.connector.pooling.MySQLConnectionPool(**pool_config)


def addup():
    print("+++")
aa = {"ll" :10,
      "kk":pool_buildup()}



print(type(aa["kk"]))
print(type(aa.get("kk")))