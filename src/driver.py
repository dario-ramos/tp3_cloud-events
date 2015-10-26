# [START imports]
import os
import cgi

import webapp2
import model
import controller

MODEL = model.Model(
    os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "config.txt"
)
# [END imports]

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
    ('/result', controller.confirmation_result_controller.ConfirmationResultController),
    ('/create', controller.create_event_controller.CreateEventController)
], debug=True)

def main():
    app.run()

if __name__ == "__main__":
    main()
