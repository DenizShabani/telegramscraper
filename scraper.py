from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import csv
import sys
import pickle
import random
import pyfiglet
import os
import datetime
from colorama import init, Fore
from telethon.tl.types import UserStatusRecently

init()

lg = Fore.LIGHTGREEN_EX
rs = Fore.RESET
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN


info = lg + '(' + w + 'i' + lg + ')' + rs
error = lg + '(' + r + '!' + lg + ')' + rs
success = w + '(' + lg + '+' + w + ')' + rs
INPUT = lg + '(' + cy + '~' + lg + ')' + rs
colors = [lg, w, r, cy]
def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('Telegram')
    print(random.choice(colors) + logo + rs)

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clr()
banner()
print(f'  {r}Version: {w}1.0 {r}| Author: {w}Shabani{rs}\n')
f = open('vars.txt', 'rb')
accs = []
while True:
    try:
        accs.append(pickle.load(f))
    except EOFError:
        f.close()
        break
print(f'{INPUT}{cy} Choose an account to scrape members\n')
i = 0
for acc in accs:
    print(f'{lg}({w}{i}{lg}) {acc[2]}')
    i += 1
ind = int(input(f'\n{INPUT}{cy} Enter choice: '))
api_id = accs[ind][0]
api_hash = accs[ind][1]
phone = accs[ind][2]
client = TelegramClient(f'sessions\\{phone}', api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone)
        code = input(f'{INPUT}{lg} Enter the login code for {w}{phone}{r}: ')
        client.sign_in(phone, code)
    except PhoneNumberBannedError:
        print(f'{error}{w}{phone}{r} is banned!{rs}')
        print(f'{error}{lg} Run {w}manager.py{lg} to filter them{rs}')
        sys.exit()
print(f'{info}{lg} Choose an option: ')
print(f'({w}0{lg}) Scrape from public group')
print(f'({w}1{lg}) Scrape from private group')
op = int(input(f'{INPUT}{lg} Enter choice: '))
if op == 0:
    username = input(f'{INPUT}{cy} Enter the exact username of the public group[Without @]: {r}')
    target_grp = 't.me/' + str(username)
    group = client.get_entity(target_grp)
else:
    target_grp = input(f'{INPUT}{cy} Enter private group invite link: {r}')
    group = client.get_entity(target_grp)
time = datetime.datetime.now().strftime("%H:%M")
print('\n' + info + lg + ' Started at ' + rs + str(time))
print(f'{info}{lg} Scraping members from {w}' + str(group.title))
members = []
members = client.get_participants(group, aggressive=True)
print(f'{info}{lg} Saving in {w}members.csv{rs}')
select = str(input(f'{INPUT}{lg} Do you wanna filter active users?[y/n]: '))
with open("members\\members.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'group', 'group id'])
    if select == 'y':
        for member in members:
            accept = True
            if not member.status == UserStatusRecently():
                accept = False
            if accept:
                if member.username:
                    username = member.username
                else:
                    username = ''
                writer.writerow([username, member.id, member.access_hash, group.title, group.id])
        print(f'{success}{lg} Filtered by {w}LastSeenRecently')
    else:
        for member in members:
            if member.username:
                username = member.username
            else:
                username = ''
            writer.writerow([username, member.id, member.access_hash, group.title, group.id])
f.close()
print(f'{success}{lg} Scraping Successful{rs}')
input('\nPress enter to exit...')
clr()
banner()
with open('target_grp.txt', 'w') as f:
    f.write(target_grp)
f.close()
sys.exit()

