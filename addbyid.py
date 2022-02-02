from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import time
import random
import pyfiglet
from telethon.tl.types import PeerUser
from colorama import init, Fore
#import traceback
import os
init()

r = Fore.RED
g = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, g, w, ye, cy]
info = g + '[' + w + 'i' + g + ']' + rs
attempt = g + '[' + w + '+' + g + ']' + rs
sleep = g + '[' + w + '*' + g + ']' + rs
error = g + '[' + r + '!' + g + ']' + rs
def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('Genisys')
    print(random.choice(colors) + logo + rs)
    print(f'{info}{g} Genisys Adder[ID] V2.5{rs}')
    print(f'{info}{g} Author: github.com/Cryptonian007{rs}\n')
def clscreen():
    os.system('cls')
clscreen()
banner()
api_id = int(sys.argv[1])
api_hash = str(sys.argv[2])
phone = str(sys.argv[3])
file = str(sys.argv[4])
group = str(sys.argv[5])
scraped = str(sys.argv[6])

def update_list(lst, temp_lst):
    count = 0
    while count != len(temp_lst):
        del lst[0]
        count += 1
    return lst

users = []

with open(file, 'r', encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=',', lineterminator='\n')
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = row[2]
        user['group'] = row[3]
        user['group_id'] = row[4]
        users.append(user)
    f.close()
client = TelegramClient(f'sessions\\{phone}', api_id, api_hash)
client.connect()
time.sleep(1.5)
target_group = client.get_entity(group)
entity = InputPeerChannel(target_group.id, target_group.access_hash)
group_name = target_group.title
n = 0
print(f'{info}{g} Getting entities{rs}\n')
target_m = client.get_entity(scraped)
client.get_participants(target_m, aggressive=True)
print(f'{info}{g} Adding members to {group_name}{rs}\n')
while True:
    if len(users) == 0:
        break
    added_users = []
    lol = []
    for user in users[:10]:
        added_users.append(user)
        user_entity = client.get_entity(user['id'])
        lol.append(user_entity)
    client(InviteToChannelRequest(entity, lol))
    print(f'{info}{g} Adding 10 users in bulk...')
    print(f'{info}{g} Sleep 20s')
    time.sleep(20)
    users = update_list(users, added_users)
print(f'{info}{g} Members added successfully')
exit()
