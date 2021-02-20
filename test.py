import requests

BASE = "http://127.0.0.1:5000/"

filename = 'file_example_WAV_1MG.wav'

with open(filename, 'rb') as fp:
    content = fp.read()

response = requests.post(
    f'{BASE}/files/{filename}', data=content
)

print(response.status_code)