import webapp2

class CreateEventController(webapp2.RequestHandler):
    def post(self):
        template_values = {
            "title" : "Create Event"
        }
        #template = JINJA_ENVIRONMENT.get_template('admin_login.html')
        #self.response.out.write(template.render(template_values))
        self.response.write('<html><body>Credentials:<pre>')
        self.response.write(cgi.escape(self.request.get('event_admin_user')))
        self.response.write('</br>')
        self.response.write(cgi.escape(self.request.get('event_admin_password')))
        self.response.write('</pre></body></html>')