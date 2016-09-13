import requests
import os


class Pirg(object):
    url = 'https://api.pushover.net/1/messages.json'

    def __init__(self, message, token=None, user=None):
        self.message = message
        self.token = token if token else os.getenv('PIRG_TOKEN')
        self.user = user if user else os.getenv('PIRG_USER')

    def push_it(self):
        data = {
            'message': self.message,
            'token': self.token,
            'user': self.user
        }
        resp = requests.post(self.url, data=data)
        resp.raise_for_status()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.push_it()
