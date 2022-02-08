import requests
headers = {
  'X-Whatsapp-Token': '5d8af8faaeb61680883a850be0c577e2'
}
data = {}

url = "https://dev.wapp.im/v3/instance30/qr_code?token=YYHF8EwzlXkvPr4R"

res = requests.request("GET",url, headers=headers, data=data)

print(res.text)