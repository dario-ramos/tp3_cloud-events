# [START imports]
import os
import cgi

import webapp2
import jinja2
import model

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

MODEL = model.Model(
    os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "config.txt"
)
# [END imports]

class MainController(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title" : "Event registration"
        }
        template = JINJA_ENVIRONMENT.get_template('view/index.html')
        self.response.write(template.render(template_values))

class ConfirmAttendanceController(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title" : "Confirm Event Attendance"
        }
        template = JINJA_ENVIRONMENT.get_template('view/confirm.html')
        self.response.write(template.render(template_values))

class ConfirmationResultController(webapp2.RequestHandler):
    def post(self):
        template_values = {
            "title" : "Confirmation Result"
        }
        template = JINJA_ENVIRONMENT.get_template('view/result.html')
        self.response.out.write(template.render(template_values))

class AdminLoginController(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title" : "Administrator login"
        }
        template = JINJA_ENVIRONMENT.get_template('view/admin_login.html')
        self.response.write(template.render(template_values))

class CreateEventController(webapp2.RequestHandler):
    def post(self):
        template_values = {
            "title" : "Create Event"
        }
        """
        template = JINJA_ENVIRONMENT.get_template('admin_login.html')
        self.response.out.write(template.render(template_values))
        """
        self.response.write('<html><body>Credentials:<pre>')
        self.response.write(cgi.escape(self.request.get('event_admin_user')))
        self.response.write('</br>')
        self.response.write(cgi.escape(self.request.get('event_admin_password')))
        self.response.write('</pre></body></html>')

"""
The above is a class definition. Here, we're instatiating
a webapp2.WSGIApplication object and passing MainPage as
a parameter, in order to tell webapp2 to instantiate items
and use it
"""
app = webapp2.WSGIApplication([
    ('/', MainController),
    ('/confirm', ConfirmAttendanceController),
    ('/admin_login', AdminLoginController),
    ('/result', ConfirmationResultController),
    ('/create', CreateEventController)
], debug=True)

def main():
    app.run()

if __name__ == "__main__":
    main()
    