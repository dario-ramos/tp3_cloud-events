import webapp2
import cgi
import environment
import time

class CreateEventController(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title" : "Create Event"
        }
        template = environment.JINJA_ENVIRONMENT.get_template('create.html')
        self.response.out.write(template.render(template_values))

    def post(self):
        name = cgi.escape(self.request.get('event_name'))
        date = cgi.escape(self.request.get('event_date'))
        vacancies = int( cgi.escape(self.request.get('event_vacancies')) )
        environment.MODEL.getEventRepository().create( name, date, vacancies )
        self.response.out.write('<html><body>')
        self.response.out.write('<h1> Event created! </h1>')
        self.response.out.write('<p> Name: ' + name + '<br/> Date: ' + date + '</br>Vacancies: ' + str(vacancies) + '</p>')
        self.response.out.write('<a href="/"> Back to portal </a>')
        self.response.out.write('</html></body>')
