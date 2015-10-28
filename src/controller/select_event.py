import environment
import webapp2

class ConfirmAttendanceController(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title" : "Confirm Event Attendance"
        }
        template = environment.JINJA_ENVIRONMENT.get_template('confirm.html')
        self.response.write(template.render(template_values))