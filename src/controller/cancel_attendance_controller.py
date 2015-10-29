#!/usr/bin/env python

import webapp2
import cgi
import environment

class CancelAttendanceController(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title" : "Cancel Attendance"
        }
        template = environment.JINJA_ENVIRONMENT.get_template('cancel.html')
        self.response.out.write(template.render(template_values))

    def renderAttendanceNotConfirmedScreen(self, eventName, guestEmail):
        self.response.out.write('<html><body>')
        self.response.out.write('<h1> Guest ' + guestEmail + ' was not subscribed to event ' + eventName + ', so nothing needs to be done </h1>')
        self.response.out.write('<a href="/"> Back to portal </a>')
        self.response.out.write('</html></body>')

    def post(self):
        eventName = cgi.escape(self.request.get('event_name'))
        guestEmail = cgi.escape(self.request.get('guest_email'))
        attendanceRepo = environment.MODEL.getAttendanceRepository()
        attendance = attendanceRepo.getByEventNameAndGuestEmail( eventName, guestEmail )
        if attendance is None:
            self.renderAttendanceNotConfirmedScreen( eventName, guestEmail )
        else:
            attendanceRepo.deleteByEventNameAndGuestEmail( eventName, guestEmail )
            self.response.out.write('<html><body>')
            self.response.out.write('<h1> Guest ' + guestEmail + ' successfully unsubscribed from event ' + eventName + '! </h1>')
            self.response.out.write('<a href="/"> Back to portal </a>')
            self.response.out.write('</html></body>')
