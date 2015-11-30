from twisted.internet import protocol, reactor, endpoints
import RPi.GPIO as GPIO

LIGHT1 = 5
LIGHT2 = 6
LIGHT3 = 13
LIGHT4 = 19
ALL_LIGHTS = [LIGHT1, LIGHT2, LIGHT3, LIGHT4]
GPIO.setmode(GPIO.BCM)
GPIO.setup(ALL_LIGHTS, GPIO.OUT, initial=0)

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        if data == b'ls1 on':
            GPIO.output(LIGHT1, 1)
        elif data == b'ls1 off':
            GPIO.output(LIGHT1, 0)
        elif data == b'ls2 on':
            GPIO.output(LIGHT2, 1)
        elif data == b'ls2 off':
            GPIO.output(LIGHT2, 0)
        elif data == b'ls3 on':
            GPIO.output(LIGHT3, 1)
        elif data == b'ls3 off':
            GPIO.output(LIGHT3, 0)
        elif data == b'ls4 on':
            GPIO.output(LIGHT4, 1)
        elif data == b'ls4 off':
            GPIO.output(LIGHT4, 0)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

endpoints.serverFromString(reactor, "tcp:8000").listen(EchoFactory())
reactor.run()
