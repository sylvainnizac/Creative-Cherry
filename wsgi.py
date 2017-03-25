import cherrypy as cp

from main.index import Root
from pages.pages import error_404, StaticPages

import config

app = cp.tree.mount(Root(), '/', config.root_conf)

if __name__ == "__main__":

    cp.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
        'error_page.404': error_404
    })

    cp.tree.mount(Root(), '/', config.root_conf)
    cp.tree.mount(StaticPages(), '/display', config.st_pages_conf)

    cp.engine.start()
    cp.engine.block()
