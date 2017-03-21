import cherrypy as cp

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('static'))


class Root(object):
    def __init__(self):
        self.skeleton = env.get_template('/templates/skeleton.html')
        self.template_under_construction = env.get_template('/pages/under_construction.html')

    @cp.expose
    def index(self):
        template = self.template_under_construction # scafold
        return self.skeleton.render(content = template.render(), title="page en construction")



