import web
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_remote_switch import RemoteSwitch

HOST = "localhost"
PORT = 4223
UID = "oiC" 
urls = (
    '/', 'index',
    '/on', 'on',
    '/off', 'off'
)
class on:
     def GET(self):
        ipcon = IPConnection()
        rs = RemoteSwitch(UID, ipcon)
        ipcon.connect(HOST, PORT)
        rs.switch_socket_a(10, 21, RemoteSwitch.SWITCH_TO_ON)
        return 'turned it on'

class off:
     def GET(self):
        ipcon = IPConnection()
        rs = RemoteSwitch(UID, ipcon)
        ipcon.connect(HOST, PORT)
        rs.switch_socket_a(10, 21, RemoteSwitch.SWITCH_TO_OFF)
        return 'turned it off'

class index:

    def GET(self):
        return 'just testing'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
