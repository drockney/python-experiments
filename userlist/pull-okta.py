import requests
import urllib.parse
import csv
from os.path import expanduser
homedir = expanduser("~")

# values to look for in Okta payload
okta_key = "id"
okta_host = "sample.okta.com"

# Get the Okta token
with open(homedir + '/.ssh/okta-token') as textfile:
    oktaToken = textfile.read().replace('\n', '')
    authorization = "SSWS " + oktaToken

# Build the Okta invocation URLs
url = "https://" + okta_host + "/api/v1/users?search=profile.login%20eq%20%22"
# url = "https://" + okta_host + "/api/v1/users/"

querystring = {"limit":"25"}

headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Authorization': authorization,
    'User-Agent': "Python/3",
    'Cache-Control': "no-cache",
    'Host': okta_host,
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

# Pull the list of Okta emails and IDs, dump in a dict
with open('email.csv') as csvfile:
    reader = csv.reader(csvfile)
    for rows in reader:
        oktaChecker = {rows[0] for rows in reader}

print("email,oktaID")
for email in oktaChecker:
    okta_id = ""
    response = requests.request("GET", url + urllib.parse.quote(email) + "%22", headers=headers, params=querystring)
    jsonresponse = response.json()
    for key in jsonresponse:
      okta_id = key[okta_key]; 
    print(email + "," + okta_id)
