import os
import os.path
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('static'))
skeleton = env.get_template('/templates/skeleton.html')
under_construction = env.get_template('/pages/under_construction.html')


root_conf = {
       '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
       '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
}

st_pages_conf = {
       '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
       '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
}
