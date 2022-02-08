import requests

headers = {
  'X-Whatsapp-Token': '5d8af8faaeb61680883a850be0c577e2'
}

payload={'phone': '89872745052',
'body': 'Hello, everyone!',
'quotedMsgId': '',
'sendSeen': '1',
'typeMsg': 'text',
'latitude': '35.227221',
'longitude': '25.249377',
'title': 'Title',
'footer': 'Footer'}
files=[

]

url = "https://dev.wapp.im/v3/instance30/sendMessage?token=YYHF8EwzlXkvPr4R"

res = requests.request("POST",url, headers=headers, data=payload, files=files)

print(res.text)