import cherrypy as cp

from config import skeleton, under_construction, main


class Root(object):

    @cp.expose
    def index(self):
        #template = under_construction  # scafold
        page_content = {"data": ""}
        template = main
        rendered_template = template.render(**page_content)
        kwargs = {
            "content": rendered_template,
            "title": "Accueil"
            }
        return skeleton.render(**kwargs)
