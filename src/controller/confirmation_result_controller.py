import environment
import webapp2

class ConfirmationResultController(webapp2.RequestHandler):
    def post(self):
        template_values = {
            "title" : "Confirmation Result"
        }
        template = environment.JINJA_ENVIRONMENT.get_template('result.html')
        self.response.out.write(template.render(template_values))