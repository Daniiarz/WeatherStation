
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import Adafruit_DHT as sensor
import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.HIGH)

client = InfluxDBClient(url="https://us-west-2-1.aws.cloud2.influxdata.com", token="srJfxgBsBABCRJNEwr0cPNebCHN3O6v8jc1TWT8vb33FTaJuzNsJk6LTn6S7W2ByTVfMOog0CLfHHHVF-4-Axw==")

write_api = client.write_api(write_options=SYNCHRONOUS)

bucket = "weather_station"
org = "a88a0599cffc05a8"

while True:
    kind = 'Temperature'
    humidity, temperature = sensor.read_retry(sensor.DHT22, 20)
    time_now = datetime.utcnow()

    """
    Write data by Point structure
    """
    point = Point(kind).field('humd', humidity).field('temp', temperature).time(time=time_now)

    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket=bucket, org=org, record=point)

    print(f"[{time_now}, {humidity} %, {temperature} C]")
    time.sleep(60)



