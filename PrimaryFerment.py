import statsd
from w1thermsensor import W1ThermSensor
from energenie import switch_on, switch_off
from decimal import *

#Create statsd and
c = statsd.StatsClient('localhost', 8125)
sensor = W1ThermSensor()


fermLow = 18.0
fermAim = 18.5
heatingOn = False


while True:
    c.gauge('fv_temperature', Decimal(sensor.get_temperature()))
    if(Decimal(sensor.get_temperature()) > fermAim):
        switch_off(1)
        c.gauge('fv_heater', 0)
    elif(Decimal(sensor.get_temperature()) <= fermLow):
        switch_on(1)
        c.gauge('fv_heater', 15)
    else:
        print "Temperature is ok"
    print sensor.get_temperature()