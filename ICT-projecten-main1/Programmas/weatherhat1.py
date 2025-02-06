import weatherhat 
import time
from datetime import datetime

sensor = weatherhat.WeatherHAT()



while True:
    #tijd = round(datetime.now(), 0) # kijken voor round optie, werkt niet
    dt = datetime.now()
    tijd = datetime.fromtimestamp(round(dt.timestamp()))
    apparaat_temperatuur = round(sensor.device_temperature, 2)
    temperature = round(sensor.temperature, 2)
    druk = round(sensor.pressure, 2)
    vochtigheid = round(sensor.humidity,2)
    lux = round(sensor.lux, 2)
    windkracht = round(sensor.wind_speed, 2)
    windrichting = sensor.wind_direction
    
    print(f"momentele tijd {tijd}" )
    
    print(f"Apparaat temperatuur: {apparaat_temperatuur:.2f} °C")
    
    print(f"temperatuur: {temperature:.2f}")
    
    print(f"luchtdruk: {druk:.2f} hPa")
    
    print(f"Luchtvochtigheid: {vochtigheid:.2f} %")
    
    print(f"Lichtintensiteit: {lux:.2f} lux")
    
    print(f"Windsnelheid: {windkracht:.2f} m/s")
    
    print(f"Windrichting: {windrichting:.2f} graden")
    
    with open('/home/rpi/ICT-projecten-main1/Programmas/weather_data.csv', "a") as log:
        log.write("\n{0},{1},{2},{3},{4},{5},{6},{7}".format(str(tijd), str(apparaat_temperatuur), str(temperature), 
                            str(druk), str(vochtigheid), str(lux), str(windkracht), str(windrichting)))
        print("brabant")
    
    sensor.update(interval=5)
    time.sleep(5)
 
