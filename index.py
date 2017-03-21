import os, os.path
import random
import string

import cherrypy as cp

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('static'))


class TestClass(object):
    def __init__(self):
        self.skeleton = env.get_template('/templates/skeleton.html')

    @cp.expose
    def index(self):
        return self.skeleton.render()

    @cp.expose
    def generate(self, content="default"):
        cp.session['mystring'] = content
        return content

    @cp.expose
    def display(self):
        return "stored string : " + cp.session['mystring']


class StaticPages(object):

    @cp.expose
    def index(self):
        return self.CV()

    @cp.expose
    def CV(self):
        sk = env.get_template('/templates/skeleton.html')
        template = env.get_template('/pages/CV.html')
        return sk.render(content = template.render(), title = "CV NIZAC Sylvain")


if __name__ == "__main__":
    conf = {
       '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
       '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }

    conf_main = {
       '/main': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
       '/main/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }

#    cp.quickstart(TestClass(), '/', conf)
    cp.tree.mount(TestClass(), '/', conf)
    cp.tree.mount(StaticPages(), '/main', conf_main)


    cp.engine.start()
    cp.engine.block()

