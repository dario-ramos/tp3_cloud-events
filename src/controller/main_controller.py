import os
import environment
import webapp2

class MainController(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title" : "Event registration"
        }
        template = environment.JINJA_ENVIRONMENT.get_template( "index.html")
        self.response.write(template.render(template_values))