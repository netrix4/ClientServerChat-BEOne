from rpc import RPCServer
server = RPCServer("localhost", 8000)
server.connect()
print(server.add(5,6))
print(server.sub(5,6))
print(server.hi(5,6))

server.disconnect()