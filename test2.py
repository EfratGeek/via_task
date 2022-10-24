import requests
import base64

# in index.js: var API_URL = 'https://api.demoblaze.com';
# type: 'POST',
# url: API_URL + '/login',
# data: JSON.stringify({"username": username, "password": pass})

s = '123456789'
EncodedString = base64.b64encode(bytes(s, 'utf-8')).decode('utf-8')
# the url to get the token to login
res1 = requests.post(url='https://api.demoblaze.com/login', json={"username": 'Efrat0000', "password": EncodedString},
                     verify=False)
j1 = res1.json()
tok = str(j1).split(': ')[1]

# in cart.js: var API_URL = 'https://api.demoblaze.com';
# type: 'POST',
# url: API_URL + '/viewcart',
# data: JSON.stringify({"cookie": token, "flag": true})


# login to user, and get the product in the cart
res = requests.post(url='https://api.demoblaze.com/viewcart',
                    json={'cookie': tok, 'flag': 'true'},
                    verify=False)
json_ = res.json()

if len(json_["Items"]) != 1:
    raise Exception
id_ = json_["Items"][0]["prod_id"]

# var API_URL = 'https://api.demoblaze.com';
# type: 'POST',
# url: API_URL + '/view',
# data: JSON.stringify({"id": articleItem.prod_id})

# send the id to see all details of product
res = requests.post(url='https://api.demoblaze.com/view', json={"id": id_},
                    verify=False)
j2 = res.json()
if (j2['price'] == 650.0) & (j2['title'] == 'Nexus 6') & (j2['id'] == 3):
    print('good!!')
else:
    raise Exception
