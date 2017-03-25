import cherrypy as cp

from config import env, skeleton


def error_404(status, message, traceback, version):
    template = env.get_template('/pages/404.html')
    rendered_template = template.render(message=message)
    kwargs = {
        "content": rendered_template,
        "title": "404... Oups!"
        }
    return skeleton.render(**kwargs)


class StaticPages(object):

    @cp.expose
    def index(self):
        return self.CV()

    @cp.expose
    def CV(self):
        template = env.get_template('/pages/CV.html')
        kwargs = {
            "content": template.render(),
            "title": "CV NIZAC Sylvain",
            "no_navbar": True
            }
        return skeleton.render(**kwargs)
