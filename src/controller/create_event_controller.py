import webapp2
import cgi
import environment

class CreateEventController(webapp2.RequestHandler):
    def renderRejectedLoginScreen(self):
        self.response.write('<html><body>')
        self.response.write('<h1>Invalid login</h1>')
        self.response.write('</body></html>')

    def createEvent(self):
        template_values = {
            "title" : "Create Event"
        }
        template = environment.JINJA_ENVIRONMENT.get_template('create.html')
        self.response.out.write(template.render(template_values))

    def post(self):
        user = cgi.escape(self.request.get('event_admin_user'))
        password = cgi.escape(self.request.get('event_admin_password'))
        validLogin = environment.MODEL.getLoginManager().admin_login( user, password )
        if not validLogin:
            self.renderRejectedLoginScreen()
        else:
            self.createEvent()
