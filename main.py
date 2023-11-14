import requests
import hashlib
import base64

username = ''
password = ''
customerID = ''

s = requests.Session() #stores your cookies, yum

def encode_pw(username, password):
    initialHash = hashlib.sha256((password + username.lower()).encode('utf-8')).digest()
    hashInBase64 = base64.b64encode(initialHash).decode('utf-8')
    return hashInBase64

pwValueToSubmit = encode_pw(username, password)

def auth():   
    authInfo = {'email': username, 'password': pwValueToSubmit}
    s.post('https://members-ng.iracing.com/auth', data=authInfo)
   
def myInfo():
    cID = {'cust_id':customerID}
    r = s.get('https://members-ng.iracing.com/data/member/info', params=cID).json()
    r = s.get(r["link"]).json()
    
    print("First Name:", r["first_name"])
    print("Last Name:", r["last_name"])
    print("Member Since:", r["member_since"])
    print("Club:", r["club_name"])

def winSummary():
    cID = {'cust_id':customerID}
    r = s.get('https://members-ng.iracing.com/data/stats/member_summary', params=cID).json()
    r = s.get(r["link"]).json()
    
    print("Wins this year:", r['this_year']['num_official_wins'])

auth()
myInfo()
winSummary()
