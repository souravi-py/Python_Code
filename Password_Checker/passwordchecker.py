import requests

url = 'https://api.pwnedpasswords.com/range/' + 'B2E98'
# the hash value of password123 is B2E98AD6F6EB8508DD6A14CFA704BAD7F05F6FB1

res = requests.get(url)
print(res)

# If response is 200, then its ok
