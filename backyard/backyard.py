# -*- coding: utf-8 -*-
import cherrypy as cp

from config import skeleton, under_construction


class Backyard(object):

    @cp.expose
    def index(self):
        template = under_construction  # scafold
        rendered_template = template.render()
        kwargs = {
            "content": rendered_template,
            "title": "page en construction"
            }
return skeleton.render(**kwargs)
