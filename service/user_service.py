import abc


class UserService(abc.ABC):
    @abc.abstractmethod
    def register_user(self, request_payload):
        pass

    @abc.abstractmethod
    def create_event(self, id, request_payload):
        pass
