import cherrypy as cp

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('static'))
skeleton = env.get_template('/templates/skeleton.html')


def error_404(status, message, traceback, version):
    template = env.get_template('/pages/404.html')
    kwargs = {
        "content": template.render(message = message),
        "title": "404... Oups!"
        }
    return skeleton.render(**kwargs)


class StaticPages(object):

    def __init__(self):
        self.skeleton = env.get_template('/templates/skeleton.html')

    @cp.expose
    def index(self):
        return self.CV()

    @cp.expose
    def CV(self):
        template = env.get_template('/pages/CV.html')
        kwargs = {
            "content": template.render(),
            "title": "CV NIZAC Sylvain"
            }
        return self.skeleton.render(**kwargs)