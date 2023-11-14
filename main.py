import requests
import hashlib
import base64

username = ''
password = ''
customer_id = ''

s = requests.Session() #stores your cookies, yum

def encode_pw(username, password):
    initial_hash = hashlib.sha256((password + username.lower()).encode('utf-8')).digest()
    hash_base64 = base64.b64encode(initial_hash).decode('utf-8')
    return hash_base64

pw_submit = encode_pw(username, password)

def auth():   
    auth_info = {'email': username, 'password': pw_submit}
    s.post('https://members-ng.iracing.com/auth', data=auth_info)
   
def my_info():
    cust_id = {'cust_id':customer_id}
    r = s.get('https://members-ng.iracing.com/data/member/info', params=cust_id).json()
    r = s.get(r["link"]).json()
    
    print("First Name:", r["first_name"])
    print("Last Name:", r["last_name"])
    print("Member Since:", r["member_since"])
    print("Club:", r["club_name"])

def win_summary():
    cust_id = {'cust_id':customer_id}
    r = s.get('https://members-ng.iracing.com/data/stats/member_summary', params=cust_id).json()
    r = s.get(r["link"]).json()
    
    print("Wins this year:", r['this_year']['num_official_wins'])

auth()
my_info()
win_summary()
