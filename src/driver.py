# [START imports]
import os

import webapp2
import controller

#[END imports]

"""
The above is a class definition. Here, we're instatiating
a webapp2.WSGIApplication object and passing MainPage as
a parameter, in order to tell webapp2 to instantiate items
and use it
"""
app = webapp2.WSGIApplication([
    ('/', controller.main_controller.MainController),
    ('/confirm', controller.confirm_attendance_controller.ConfirmAttendanceController),
    ('/admin_login', controller.admin_login_controller.AdminLoginController),
    ('/create', controller.create_event_controller.CreateEventController),
    ('/failed_login', controller.failed_login_controller.FailedLoginController),
    ('/select_event', controller.select_event_controller.SelectEventController),
    ('/cancel', controller.cancel_attendance_controller.CancelAttendanceController),
    ('/check', controller.check_attendance_controller.CheckAttendanceController)
], debug=True)

def main():
    app.run()

if __name__ == "__main__":
    main()
