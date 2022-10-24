import requests
import base64
s = '123456789'
EncodedString = base64.b64encode(s.encode('utf-8'))
res = requests.post(url='https://www.demoblaze.com//login', data={"username": 'Efrat0000', "password": EncodedString}, verify=False)
print(res)
