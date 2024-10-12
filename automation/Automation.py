import requests

from utilities.configurations import *

se = requests.session()
se.auth= auth=('SiddharthKankane', getPassword())
url = 'https://api.github.com/user'

github_response = se.get(url)
print(github_response.status_code)

se.cookies.update({'visit-month': 'August'})
res=se.get('https://httpbin.org/cookies', cookies={'visit-year': '2024'}, timeout=1)
print(res.history)
print(res.text)

if __name__ == '__main__':
    pass
