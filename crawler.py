import requests

def login():
    payload = {'user': "123", 'password': "abc"}
    post_url = 'https://exitwatch-api2.h-m-g.se/auth/login'
    
    session = requests.Session()

    resp = session.post(post_url, payload)
    token = resp.json()
    tokenKey = token['token']

    custom_headers = {
        'Authorization': tokenKey
    }

    resp2 = session.get('https://exitwatch-api2.h-m-g.se/users/auth',headers=custom_headers)
    # print(resp2.status_code)
    # print(resp2.text)

    return session, custom_headers

#======================================searching

def search(session, custom_headers, searchQuery):
    
    searchUrl = 'https://exitwatch-api2.h-m-g.se/search'
    searchPayload = {'searchQuery': searchQuery}

    searchResp = session.post(searchUrl, searchPayload, headers=custom_headers)
    data = searchResp.json()
    
    return searchResp.status_code, data 
  

