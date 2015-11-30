from twisted.internet import protocol, reactor, endpoints

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        if data == b'ls1 on':
            print('Lights 1 switched on!')
        elif data == b'ls1 off':
            print('Lights 1 switched off!')
        elif data == b'ls2 on':
            print('Lights 2 switched on!')
        elif data == b'ls2 off':
            print('Lights 2 switched off!')
        elif data == b'ls3 on':
            print('Lights 3 switched on!')
        elif data == b'ls3 off':
            print('Lights 3 switched off!')
        elif data == b'ls4 on':
            print('Lights 4 switched on!')
        elif data == b'ls4 off':
            print('Lights 4 switched off!')

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

endpoints.serverFromString(reactor, "tcp:8000").listen(EchoFactory())
reactor.run()