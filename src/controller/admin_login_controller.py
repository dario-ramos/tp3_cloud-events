import environment
import webapp2
import cgi

class AdminLoginController(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title" : "Administrator login"
        }
        template = environment.JINJA_ENVIRONMENT.get_template('admin_login.html')
        self.response.write(template.render(template_values))

    def post(self):
        user = cgi.escape(self.request.get('event_admin_user'))
        password = cgi.escape(self.request.get('event_admin_password'))
        validLogin = environment.MODEL.getLoginManager().admin_login( user, password )
        if not validLogin:
            self.redirect("/failed_login")
        else:
            self.redirect("/create")