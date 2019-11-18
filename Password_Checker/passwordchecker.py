import hashlib
import requests
import sys


# Pass it to the API
def get_all_api_pass(Query_Hash):
    url = 'https://api.pwnedpasswords.com/range/' + Query_Hash
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Could not fetch data from the APi, as status code = {response.status_code}')
    else:
        return response.text



# Get hashed version of the password and divide it into 2 parts
def get_hashed_pass(Pass):
    Sha1_Pass = hashlib.sha1(Pass.encode('utf-8')).hexdigest().upper()
    First5_pass, Tail = Sha1_Pass[:5], Sha1_Pass[5:]
    return (First5_pass, Tail)

def pass_matching(First5_pass, Tail):
    #Call Func to get all matching Passwords
    res = 0
    hits = 0
    Passwords = get_all_api_pass(First5_pass)
    for line in Passwords.splitlines():
        hash, count = (line.split(':') )

        if Tail == hash:
            res = 1
            hits = count
            break
    return (res, hits)


def main(password_to_check):
    First5_pass, Tail = get_hashed_pass(password_to_check)
    Response , Hits = pass_matching(First5_pass, Tail)
    if Response == 1:
        print(f'This Password {password_to_check} is used before and has been hacked {Hits} times')
    else:
        print(f'This pass {password_to_check} is safe to use, go ahaead !!!')


password_list = sys.argv[1:]
for password in password_list:
    main(password)
