#!/usr/bin/python3

from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers
import datetime
import time

"""
================================================
ABElectronics ADC Pi 8-Channel ADC data-logger demo
Version 1.0 Created 29/02/2015

Requires python 3 smbus to be installed
run with: python3 demo-read_voltage.py
================================================

Initialise the ADC device using the default addresses and sample rate, change
this value if you have changed the address selection jumpers

Sample rate can be 12,14, 16 or 18
"""


i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x68, 0x69, 18)

n = int(0)

def writetofile(texttowrtite):
    f = open('adclog.txt', 'a')
    f.write(str(n) + ", " + texttowrtite)
    f.closed

while (True):
    # read from adc channels and write to the log file
    writetofile("%02f\n" % adc.read_voltage(1))
    n = n + 1
    # wait 1 second before reading the spins again
    time.sleep(1)
