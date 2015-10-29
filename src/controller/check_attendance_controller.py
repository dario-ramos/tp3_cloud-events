#!/usr/bin/env python

import webapp2
import cgi
import environment

class CheckAttendanceController(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title" : "Check Event Attendance"
        }
        template = environment.JINJA_ENVIRONMENT.get_template('check.html')
        self.response.out.write(template.render(template_values))

    def renderAttendanceConfirmationScreen(self, attendance, eventName, guestEmail):
        self.response.out.write('<html><body>')
        result = ""
        if attendance is None:
            result = "NOT"
        self.response.out.write('<h1> Attendance ' + result + ' confirmed by guest ' + guestEmail + ' for event ' + eventName + '</h1>')
        self.response.out.write('<a href="/"> Back to portal </a>')
        self.response.out.write('</html></body>')
        
    def renderEventDoesNotExistScreen(self, eventName):
        self.response.out.write('<html><body>')
        self.response.out.write('<h1> Event ' + eventName + ' not registered in system! </h1>')
        self.response.out.write('<a href="/"> Back to portal </a>')
        self.response.out.write('</html></body>')

    def post(self):
        eventName = cgi.escape(self.request.get('event_name'))
        guestEmail = cgi.escape(self.request.get('guest_email'))
        event = environment.MODEL.getEventRepository().getByName( eventName )
        if event is None:
            self.renderEventDoesNotExistScreen( eventName )
            return
        attendance = environment.MODEL.getAttendanceRepository().getByEventNameAndGuestEmail( eventName, guestEmail )
        self.renderAttendanceConfirmationScreen( attendance, eventName, guestEmail )
