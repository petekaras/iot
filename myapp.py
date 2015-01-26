import cherrypy
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_remote_switch import RemoteSwitch
HOST = "localhost"
PORT = 4223
UID = "oiC"
class Root(object):
    @cherrypy.expose
    def on(self):
        ipcon = IPConnection()
        rs = RemoteSwitch(UID, ipcon)
        ipcon.connect(HOST, PORT)
        rs.switch_socket_a(10, 21, RemoteSwitch.SWITCH_TO_ON)
        return 'turned it on'

    @cherrypy.expose
    def off(self):
        ipcon = IPConnection()
        rs = RemoteSwitch(UID, ipcon)
        ipcon.connect(HOST, PORT)
        rs.switch_socket_a(10, 21, RemoteSwitch.SWITCH_TO_OFF)
        return 'turned it off'

if __name__ == '__main__':
# bind to all IPv4 interfaces
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(Root())
#   cherrypy.quickstart(Root(), '/')
