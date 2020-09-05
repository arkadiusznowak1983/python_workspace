import unittest
from observer_pattern import Observer, ObserverNameException, Publisher

class ObserverTestCase(unittest.TestCase):
    def test_Observer_ExceptionName(self):
        with self.assertRaises(ObserverNameException): Observer()

    def test_Observer_NotExceptionName(self):
        try:
            Observer('some name')
            self.assertTrue(True)
        except:
            self.fail('NameException not apperas')

    def test_notification(self):
        observer = Observer('observer')
        publisher = Publisher('publisher')
        publisher.register(observer)
        publisher.publish()
        self.assertTrue(publisher.name in observer.notifications, 'Notification no appears')

if __name__ == '__main__':
    unittest.main()