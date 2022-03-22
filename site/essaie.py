import cherrypy

class Monsiteweb(object):
    """docstring for Monsiteweb."""

    def index(self):
        return ''' <h1><a href="/test">Bonojour tout le monde</a></h1>'''
    index.exposed =True

    def test(self):
        return '''<p> je juis le rois de la jungle</p>'''
    test.exposed = True

cherrypy.quickstart(Monsiteweb(), config = "tutoriel.conf" )
