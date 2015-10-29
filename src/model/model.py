import configuration
import login_manager
import event_repository
import guest_repository
import attendance_repository

class Model(object):
    def __init__(self, configFile):
        self.config = configuration.Configuration(configFile)
        if( self.config.getProperty("mock_db") == "1" ):
            self.loginManager = login_manager.MockLoginManager()
        else:
            self.loginManager = login_manager.LoginManager()
        self.eventRepository = event_repository.EventRepository()
        self.guestRepository = guest_repository.GuestRepository()
        self.attendanceRepository = attendance_repository.AttendanceRepository()

    def getLoginManager(self):
        return self.loginManager

    def getEventRepository(self):
        return self.eventRepository

    def getGuestRepository(self):
        return self.guestRepository

    def getAttendanceRepository(self):
        return self.attendanceRepository
