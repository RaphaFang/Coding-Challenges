def convertSeconds(sec):
    remain_sec = sec%60
    min = (sec%3600)//60
    hour = (sec%86400)//3600
    day = sec//86400
    print([day,hour,min, remain_sec])

convertSeconds(100000)