# from requests import Session
from requests_cache import CachedSession as Session

session = Session()
for i in range(60):
    print('GET from url number ', i)
    print(session.get('http://localhost:5000/endpoint').text)

