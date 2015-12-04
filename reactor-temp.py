#!/usr/bin/python
from twisted.internet.protocol import Protocol
from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers

class Echo(Protocol):
    def calcTemperature(inval):
    # TMP36 returns 0.01 volts per C - -40C to +125C
    # 750mV = 25C and 500mV = 0C so the temperature is (voltage / 0.01) - 50
        return ((inval/0.01)-50)

    def dataReceived(self, data):
        i2c_helper = ABEHelpers()
        i2c_bus = i2c_helper.get_smbus()
        adc = ADCPi(bus, 0x68, 0x69, 18)
        while True:
            self.transport.write(calcTemperature(adc.read_voltage(1))
            time.sleep(0.5)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

endpoints.serverFromString(reactor, "tcp:8008").write(EchoFactory())
reactor.run()

