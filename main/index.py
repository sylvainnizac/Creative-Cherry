import cherrypy as cp
import psutil
from datetime import datetime

from config import skeleton, under_construction, main_page


class Root(object):

    @cp.expose
    def index(self):
        #template = under_construction  # scafold
        processes_names = ["nginx"]
        page_content = {"data": self.process_status(processes_names)}
        template = main_page
        rendered_template = template.render(**page_content)
        kwargs = {
            "content": rendered_template,
            "title": "Accueil"
            }
        return skeleton.render(**kwargs)
    
    def process_status(self, searched=["nginx"]):
        data = {}
        for proc in psutil.process_iter():
            if proc.name() in searched:
                data[proc.name()] = {
                        "status": proc.status(),
                        "create time": datetime.fromtimestamp(proc.create_time()).strftime("%Y-%m-%d %H:%M:%S"),
                        "cpu interval": proc.cpu_percent(interval=1)
                    }
        return data

    
