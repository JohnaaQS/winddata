
import time




print("start")
with open('/home/rpi/ICT-projecten-main1/Programmas/weather_data.csv', "a") as log: 
    while True:
        log.write("{0},{1}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"),"Tijdstip"))
        time.sleep(1)
        print("iets")