import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

if __name__ == '__main__':
# bind to all IPv4 interfaces
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(Root())
#   cherrypy.quickstart(Root(), '/')
