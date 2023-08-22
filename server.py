from socketio import Server, WSGIApp

# create a Socket.IO server
sio = Server()

# wrap with a WSGI application
app = WSGIApp(sio)

@sio.event
def controllerInput(sid, data):
    print("recived")
    pass
