# NameCheck
Namecheck is a web scraper (kinda) which aims to check usernames to see if they are valid. It will scan through a bunch of links looking for a certain phrase and will return with the usernames that are availible. It works for bulk username checking. You paste the usernames you want into the text file (*names.txt*) in the folder in this format:
```
USERNAME 
OTHERUSERNAME
ANOTHERUSERNAME
...
```
and the bot will (after completing) put all the availible usernames in another text file (*available.txt*)

# Installation
The installation is super simple. You cannot mess this up, it's too easy.

`1.` Click the green **<> Code** button, and click **Download ZIP**. Then unzip the zip that downloads, and you will be left with a folder named **mc.namecheck-main** (or something like that).

`2.` Open the folder, and open the **names.txt** folder. Then paste (in the format shown in the file) or replace the file with the names you want to check the availibility of (remember to rename it *names.txt*)

`3.` Open terminal, and enter the following lines (1 line at a time):
```
pip install requests
cd (drag the folder to this line, or type to file path to the folder)
python script.py
```
`4.` Open *available.txt* to find the availible usernames, or read them in the terminal.

# Help
If you have errors, you can edit this code or ask me. My discord server is: https://discord.gg/rqjE7yvtZw
