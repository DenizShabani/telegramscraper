==How to use== [simple guide]

COPY CODE WITH CREDITS


Also, if you enjoyed using the tool, do give it a star on GitHub

CONTENTS

1) Steps to use
2) Troubleshooting

==STEPS TO USE==

step 1: Storing accounts using manager.py for scraping and adding purposes

i) Open terminal in the repo directory and enter command
>>> python manager.py
ii) If you wanna enter new accounts, choose option 1
    Enter Api id, Api hash and phone number
    if you want to add more accounts, enter 'y' ; if not then enter 'n' and hit enter
iii) If you wanna filter all banned accounts, choose option 2. It'll delete all banned accounts
iv) To show all accounts, choose option 3
v) To delete accounts, choose option 4
   Then choose an account to delete and hit enter


step 2: Scraping members using scraper.py

i) Run in terminal >>> python scraper.py
ii) Choose an account in order to scrape and hit enter
iii) Choose whether to scrape from public group or private group
     PUBLIC GROUPS
     Suppose public group username is @ThisGroup. Enter only 'ThisGroup'. Omit '@' and hit enter
     PRIVATE GROUPS
     Copy invite link and paste in the terminal and hit enter
  
     Then it'll scrape members
 
     Then it'll ask whether to filter active users[LAST SEEN RECENTLY]. Choose y/n and proceed

step 3: Adding members using tsadder.py

i) Launch in terminal >>> python tsadder.py
ii) It'll create sessions and will ask for login code if not logged in. IF YOU DO NOT HAVE LOGIN CODE,
    PRESS 's' AND HIT ENTER TO SKIP
iii) Then enter username of the public group without @ sign. It'll join from all accounts
iv) Then enter number of accounts to use
EACH ACCOUNT WILL GET 60 USERS TO ADD. IT MAY BE LESS THAN 60 DUE TO PRIVACY RESTRICTIONS OR PEER FLOOD ERROR
v) Then read the warning and press enter to proceed
vi) It'll launch scripts and it'll add members


==TROUBLESHOOTING==

1) Members not getting added

Ans- It may be because the account is probably limited. Try other accounts

2) Error while logging in

Ans- If you have 2 factor authentication on, turn it off. After login, you can turn it on again

Any problems, open issue at GitHub or contact me on telegram group you will find on README.md


