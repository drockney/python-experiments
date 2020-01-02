import json

with open('users.json') as json_file:
    data = json.load(json_file)
    for p in data['users']:
        print('firstname: ' + p['firstname'])
        print('lastname: ' + p['lastname'])
        print('oktaid: ' + p['oktaid'])
        print('username: ' + p['username'])
        print('emailaddress: ' + p['emailaddress'])
        print('')
