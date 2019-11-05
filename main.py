import pymongo
import time

s=['18.188.115.191:27017', '18.221.219.25:27017','18.191.172.47:27017']

client = pymongo.MongoClient('mongodb://172.31.19.92:27017,172.31.31.55:27017,172.31.30.13:27017/?replicaSet=rs0')

db = client["chat_db"]

col = db["chat"]


nick = input('Create your nickname: ')


print('CHAT HISTORY')
for i in col.find():
  print(i["nick"]+": "+i["msg"])
print('\n')


while True:
  msg = input('Write down the message: ')
  if msg == 'exit':
    break


  mydict = { "nick": nick, "msg": msg }

  x = col.insert_one(mydict)

 print('CHAT HISTORY')
for i in col.find():
  print(i["nick"]+": "+i["msg"])
print('\n')