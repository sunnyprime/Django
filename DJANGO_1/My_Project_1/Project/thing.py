import httplib, urllib,time
from random import randint

apikey = "XNNN01N0GAXR91AM"

while True:

    ran01 = randint(0,10)
    print ran01
    params = urllib.urlencode({'field1':ran01,'key':apikey})
    headers = {"Content-type": "application/x-www-form-urlencode","Accept":"text/plain"}
    conn.request("POST","/update",params,headers)
    response = conn.getresponse()

    print response.status, response.reason
    data = response.read()
    conn.close()
    print data

    time.sleep(240)
