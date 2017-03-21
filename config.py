import os, os.path

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
       '/main': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
       '/main/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
}
