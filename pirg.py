import requests
import os


class Pirg(object):
    url = 'https://api.pushover.net/1/messages.json'

    def __init__(self, message, token=None, user=None):
        self.message = message
        self.token = token if token else os.getenv('PIRG_TOKEN')
        self.user = user if user else os.getenv('PIRG_USER')

    def d(self, fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            self.push_it()
            return result
        return wrapper

    def push_it(self):
        data = {
            'message': self.message,
            'token': self.token,
            'user': self.user
        }
        resp = requests.post(self.url, data=data)
        if resp.status_code != 200:
            print("Something went wrong pushing it real good")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.push_it()
