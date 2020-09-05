import abc

class ObserverLabels:
    DEFAULT_NAMEEXCEPTION_NAME = 'Observer Name Exception (NameException)'
    DEFAULT_NAMEEXCEPTION_MESSAGE = 'bad observer name'
class PublisherLabels:
    PUBLISHER_NOTIFY_PUBLISH_MESSAGE = 'subject publish something'

class ObserverException(Exception):
    def __str__(self):
        return f'{self.name} -> {self.message}'
    def print(self):
        print(self)
class ObserverNameException(ObserverException):
    def __init__(self, message=None):
        self.name = ObserverLabels.DEFAULT_NAMEEXCEPTION_NAME
        self.message = ObserverLabels.DEFAULT_NAMEEXCEPTION_MESSAGE if message is None else message
        super().__init__(self.message)
class UpdateException(ObserverException):
    def __init__(self, message=None):
        self.name = ObserverLabels.DEFAULT_NAMEEXCEPTION_NAME
        self.message = ObserverLabels.DEFAULT_NAMEEXCEPTION_MESSAGE if message is None else message
        super().__init__(self.message)

class ObserverInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        pass
class Observer(ObserverInterface):
    def __init__(self, name = None):
        if name is None or not isinstance(name, str):
            raise ObserverNameException
        self.name = name
        self.notifications = []
    def __repr__(self):
        return self.name

    '''override ObserverInterface.update'''
    def update(self, name=None, msg=None):
        # print("notification from {} to {} => {}".format(name, self.name, msg))
        self.notifications.append(name)

class PublisherInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register(self, observer: Observer):
        pass
    @abc.abstractmethod
    def unregister(self, observer: Observer):
        pass
    @abc.abstractmethod
    def notify(self):
        pass

class Publisher(PublisherInterface):
    def __init__(self, name=None):
        # name needs to validated, add class with PublisherNameException and use it
        self.name = name
        self.observers = []
    '''override PublisherInterface.register'''
    def register(self, observer: Observer):
        if observer not in self.observers:
            self.observers.append(observer)
    '''override PublisherInterface.unregister'''
    def unregister(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)
    '''override PublisherInterface.notify'''
    def notify(self, msg=None):
        if len(self.observers) > 0:
            for observer in self.observers:
                observer.update(self.name, msg)
    def publish(self):
        self.notify(PublisherLabels.PUBLISHER_NOTIFY_PUBLISH_MESSAGE)

if __name__ == "__main__":
    pass