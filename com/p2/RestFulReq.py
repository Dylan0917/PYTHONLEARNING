# -*- coding: UTF-8 -*-
import json
from urllib import request
from urllib import error
try:
    create_url='http://localhost:8080/springmvcpc/rest/test'#the create request url
    create_headers={'Content-Type':'text/plain; charset=utf-8'} #the request headers
    body_data_str='{"timeStr":"bodytext"}'
    body_data = bytes(body_data_str, 'utf8')
    req = request.Request(create_url, headers=create_headers, data=body_data, method='POST')
    resp = request.urlopen(req)
    result = resp.read().decode()
    print(result)
    # result_json = json.loads(result)

except error.HTTPError as err:
     error_body = err.file.read().decode()
