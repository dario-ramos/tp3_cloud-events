import environment
import webapp2

class AdminLoginController(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title" : "Administrator login"
        }
        template = environment.JINJA_ENVIRONMENT.get_template('admin_login.html')
        self.response.write(template.render(template_values))