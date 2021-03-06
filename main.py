"""
*************************************************************************************************
𝕻𝖗𝖔𝖌𝖗𝖆𝖒 𝕹𝖆𝖒𝖊    : 𝕾𝖚𝖇𝕯𝖔𝖒𝖆𝖎𝖓 𝕱𝖎𝖓𝖉𝖊𝖗
𝕬𝖚𝖙𝖍𝖔𝖗          : 𝕸𝖔𝖓𝖙𝖆𝖘𝖎𝖒
𝕮𝖗𝖊𝖆𝖙𝖊 𝕺𝖓       : 11.11.2020

Variable used in this program
-------------------------------------------------------------------------------------------------
domain - take input domain name
file   - open file
content - read content from file
subdomains - list where to find subdomains
url = url of subdomains
*************************************************************************************************
"""

#   importing request for handling http and https connection
import requests

#   take input domain name
domain = input("Enter Domain Name Without 'HTTP://': ")
#   this file contains subdomain list
file = open('subdomains-10000.txt', 'r', )

#   read where to find subdomain
content = file.read()
#   read next line from file
subdomains = content.splitlines()

#   identify subdomain by sending them request
#   if request accepts then it is subdomain
for subdomain in subdomains:
    url = f'http://{subdomain}.{domain}'
    #   sending request
    try:
        requests.get(url)
    #   when connection error pass to next
    except requests.ConnectionError:
        pass
    #   when connection found it is a subdomain.
    else:
        #   showing subdomains
        print("Discovered Subdomains: ", url)
        #   saving subdomains in a file
        file = open(domain + '.txt', "a", encoding="utf8")
        file.write(url + '\n')

"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████████████─████████████───██████████████────██████████████───████████──████████─
─██░░██████████████░░██─██░░░░░░░░░░██─██░░░░░░░░████─██░░░░░░░░░░██────██░░░░░░░░░░██───██░░░░██──██░░░░██─
─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─██░░████░░░░██─██░░██████████────██░░██████░░██───████░░██──██░░████─
─██░░██████░░██████░░██─██░░██──██░░██─██░░██──██░░██─██░░██────────────██░░██──██░░██─────██░░░░██░░░░██───
─██░░██──██░░██──██░░██─██░░██████░░██─██░░██──██░░██─██░░██████████────██░░██████░░████───████░░░░░░████───
─██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██────██░░░░░░░░░░░░██─────████░░████─────
─██░░██──██████──██░░██─██░░██████░░██─██░░██──██░░██─██░░██████████────██░░████████░░██───────██░░██───────
─██░░██──────────██░░██─██░░██──██░░██─██░░██──██░░██─██░░██────────────██░░██────██░░██───────██░░██───────
─██░░██──────────██░░██─██░░██──██░░██─██░░████░░░░██─██░░██████████────██░░████████░░██───────██░░██───────
─██░░██──────────██░░██─██░░██──██░░██─██░░░░░░░░████─██░░░░░░░░░░██────██░░░░░░░░░░░░██───────██░░██───────
─██████──────────██████─██████──██████─████████████───██████████████────████████████████───────██████───────
────────────────────────────────────────────────────────────────────────────────────────────────────────────
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████████████─██████──────────██████─██████████████─██████████████─██████████████─██████████─██████──────────██████─
─██░░██████████████░░██─██░░░░░░░░░░██─██░░██████████──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██████████████░░██─
─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─██░░░░░░░░░░██──██░░██─██████░░██████─██░░██████░░██─██░░██████████─████░░████─██░░░░░░░░░░░░░░░░░░██─
─██░░██████░░██████░░██─██░░██──██░░██─██░░██████░░██──██░░██─────██░░██─────██░░██──██░░██─██░░██───────────██░░██───██░░██████░░██████░░██─
─██░░██──██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─────██░░██─────██░░██████░░██─██░░██████████───██░░██───██░░██──██░░██──██░░██─
─██░░██──██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██───██░░██───██░░██──██░░██──██░░██─
─██░░██──██████──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─────██░░██─────██░░██████░░██─██████████░░██───██░░██───██░░██──██████──██░░██─
─██░░██──────────██░░██─██░░██──██░░██─██░░██──██░░██████░░██─────██░░██─────██░░██──██░░██─────────██░░██───██░░██───██░░██──────────██░░██─
─██░░██──────────██░░██─██░░██████░░██─██░░██──██░░░░░░░░░░██─────██░░██─────██░░██──██░░██─██████████░░██─████░░████─██░░██──────────██░░██─
─██░░██──────────██░░██─██░░░░░░░░░░██─██░░██──██████████░░██─────██░░██─────██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██──────────██░░██─
─██████──────────██████─██████████████─██████──────────██████─────██████─────██████──██████─██████████████─██████████─██████──────────██████─
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"""
