from abc import ABCMeta, abstractmethod

class ILoginManager:
    __metaclass__ = ABCMeta

    @abstractmethod
    def admin_login(self, user, password): pass

class MockLoginManager(ILoginManager):
    def admin_login(self, user, password):
        return user == "admin" and password == "admin"

class LoginManager(ILoginManager):
    def admin_login(self, user, password):
        raise NotImplementedError()
