import requests

url = "http://0.0.0.0:5001"
files = {"file":open("/tmp/wajah.jpg", 'rb')}

# POST request
r = requests.post(url, files=files).json()

print(r)

