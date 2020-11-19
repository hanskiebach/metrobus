import requests

print("Please enter your name: ")
name = input()
url = f"http://localhost:5000/hello/{name}"
reponse = requests.get(url)
print(reponse.text)