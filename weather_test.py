import Adafruit_DHT as sensor
import threading
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.HIGH)

for i in range(40):
    humidity, temperature = sensor.read_retry(sensor.DHT22, 20)
    print(humidity, temperature)
    time.sleep(2)

