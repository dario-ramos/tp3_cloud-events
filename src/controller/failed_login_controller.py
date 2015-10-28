import environment
import webapp2

class FailedLoginController(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title" : "Failed login"
        }
        template = environment.JINJA_ENVIRONMENT.get_template('failed_login.html')
        self.response.write(template.render(template_values))
