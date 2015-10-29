#!/usr/bin/env python

import environment
import webapp2
import cgi


class ConfirmAttendanceController(webapp2.RequestHandler):

    def get(self):
        event_id = self.request.GET['event_id']
        template_values = {
            "title": "Confirm Event Attendance",
            "event_id": event_id
        }
        template = environment.JINJA_ENVIRONMENT.get_template('confirm.html')
        self.response.write(template.render(template_values))

    def renderNoVacanciesScreen(self):
        self.response.out.write('<html><body>')
        self.response.out.write(
            '<h1> Sorry, there are no more vacancies for this event </h1>')
        self.response.out.write('<a href="/"> Back to portal </a>')
        self.response.out.write('</html></body>')

    def renderAlreadyConfirmedScreen(self):
        self.response.out.write('<html><body>')
        self.response.out.write(
            '<h1> Attendance has already been confirmed by this guest for this event! </h1>')
        self.response.out.write('<a href="/"> Back to portal </a>')
        self.response.out.write('</html></body>')

    def registerAttendance(self, event, guestFirstName, guestLastName, guestEmail, guestCompany):
        # Check if guest exists. If it does not, create it
        guestRepo = environment.MODEL.getGuestRepository()
        guest = guestRepo.getByEmail(guestEmail)
        if guest is None:
            guestRepo.create(guestFirstName, guestLastName,
                             guestEmail, guestCompany)
            guest = guestRepo.getByEmail(guestEmail)
        # Check if attendance for this guest exists
        attendanceRepo = environment.MODEL.getAttendanceRepository()
        attendance = attendanceRepo.getByEventNameAndGuestEmail(
            event.name, guestEmail)
        if attendance is not None:
            self.renderAlreadyConfirmedScreen()
        else:
            attendanceRepo.create(guestEmail, event.name)
            event.vacancies = event.vacancies - 1
            environment.MODEL.getEventRepository().update(event)
            self.response.out.write('<html><body>')
            self.response.out.write('<h1> Attendance confirmed! </h1>')
            self.response.out.write('<p> Name: ' + guestFirstName + ' ' + guestLastName + '<br/> Email: ' + guestEmail +
                                    '</br>Company: ' + guestCompany + '</br>Event: ' + event.name + '<br/>Vacancies: ' + str(event.vacancies) + '</p>')
            self.response.out.write('<a href="/"> Back to portal </a>')
            self.response.out.write('</html></body>')

    def post(self):
        guestFirstName = cgi.escape(self.request.get('event_guest_first_name'))
        guestLastName = cgi.escape(self.request.get('event_guest_last_name'))
        guestEmail = cgi.escape(self.request.get('event_guest_email'))
        guestCompany = cgi.escape(self.request.get('event_guest_company'))
        eventID = cgi.escape(self.request.GET["event_id"]).strip()
        # Check if the event has vacancies
        eventRepo = environment.MODEL.getEventRepository()
        event = eventRepo.getByName(eventID)
        if event.vacancies == 0:
            self.renderNoVacanciesScreen()
        else:
            self.registerAttendance(
                event, guestFirstName, guestLastName, guestEmail, guestCompany)
