import requests
# 4ef4332c-3bf4-4c4b-a88a-fecfe9cee647
uuid = '4ef4332c-3bf4-4c4b-a88a-fecfe9cee647'
url = 'https://cache-it-to-win-it.chall.lac.tf/check?uuid=' + uuid
response = requests.get(url)

print(response.status_code)
print(response.text)