#If your reading this and intend to copy this code, go ahead, I don't really care. If you give me credit, thats up to you.
#If you have errors, you can edit this code if you know python, or ask me. My discord is monohuman

import requests
import concurrent.futures

base_url = "https://api.mojang.com/users/profiles/minecraft/"

def check_username(username):
    url = base_url + username
    response = requests.get(url)
    
    if "Couldn't find any profile with name" in response.text:
        return username + ' is available'
    else:
        return None

with open('names.txt', 'r') as infile, open('available.txt', 'w') as outfile:
    usernames = [line.strip() for line in infile]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for result in executor.map(check_username, usernames):
            if result is not None:
                print(result)
                outfile.write(result.split(' ')[0] + '\n')
