class Session:

    def __init__(self, header={}):
        self.header = header

    def post(self, url, payload={}):
        print(f"calling {url} with header {self.header} and payload {payload}")


class DecoratorSession:
    token = None

    def __init__(self, decorated_class):
        self.decorated_class = decorated_class

    def __call__(self, *args, **kwargs):
        result = self.decorated_class(*args, **kwargs)
        if DecoratorSession.token is not None:
            result.header["token"] = DecoratorSession.token
        return result


Session = DecoratorSession(Session)
DecoratorSession.token = "#123456789#"

s1 = Session({'verify': False})
s2 = Session()

s1.post(f"https://first.endpoint")
s2.post(f"https://second.endpoint", {'key': 'value'})
