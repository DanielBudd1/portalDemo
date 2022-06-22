from email import utils
import urllib3
import certifi
from base64 import b64encode
import json
import pandas
# from backend.utils import postToAppian
http = urllib3.PoolManager(ca_certs=certifi.where())

payload = {'name': 'John Doe'}
# encoded_data = json.dumps(payload).encode('utf-8')
# encoded_data = b64encode(open('CSVs/test_book.xlsx', 'rb').read()),
excel_data_df = pandas.read_excel('CSVs/test_book.xlsx')
json_str = excel_data_df.to_json()
encoded_data = json_str#.encode('utf-8')
print(encoded_data)
resp = http.request(
    'POST',
    'https://convedodev.appiancloud.com/suite/webapi/fZdhLg',
    body=encoded_data,
    headers={'Appian-API-Key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI4ZmI4ZjU3Zi00NTkzLTRjM2EtODc5Yy00NWVlY2Y1ZDM5MDgifQ.vBsGgPP9cfR0BvRfECUXVv2rctfXrE7zhC-DDkckDqc'})

data = resp.data.decode('utf-8')
print(data)
