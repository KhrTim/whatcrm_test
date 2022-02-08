import requests
headers = {
  'X-Whatsapp-Token': '5d8af8faaeb61680883a850be0c577e2'
}
res = requests.request("GET","https://dev.wapp.im/v3/chat/spare?crm=TEST&domain=test", headers=headers)

print(res.text)