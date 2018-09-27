import requests
import string
import random
import threading
import urllib.request
import ssl

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

def search(url):
    while True:
        while not exists(url):
            url = "".join(["https://i.imgur.com/", id_generator(7, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"), ".jpg"])
            print(url)
        filepath = "imgur/" + "".join([id_generator(7, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"), ".jpg"])
        ssl._create_default_https_context = ssl._create_unverified_context
        urllib.request.urlretrieve(url, filepath)
        url = "".join(["https://i.imgur.com/", id_generator(7, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"), ".jpg"])

url = "".join(["https://i.imgur.com/", id_generator(7, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"), ".jpg"])

while True:
    search(url)
