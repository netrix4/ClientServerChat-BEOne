def add(a,b):
    return a+b
def sub (a,b):
    return a-b
def div(a,b):
    return a/b
def hi():
    return "Saludos, humano!"

from rpc import RPCServer

server = RPCServer()
server.registerMethod(add)
server.registerMethod(sub)
server.registerMethod(hi)
server.run()
