import json


def get_email():
    with open('authh/data.json') as file:
        res = json.load(file)
        return res['email']


def get_code():
    with open('authh/data.json') as file:
        res = json.load(file)
        return res['code']


def set_email(email):
    with open('authh/data.json', 'r') as file:
        code = json.load(file)['code']
    with open('authh/data.json', 'w') as file:
        json.dump({'code': code, 'email': email}, file)


def set_code(code):
    with open('authh/data.json', 'r') as file:
        email = json.load(file)['email']
    with open('authh/data.json', 'w') as file:
        json.dump({'code': code, 'email': email}, file)
