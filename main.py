import pymongo

client = pymongo.MongoClient('mongodb://172.31.38.199:27017,172.31.17.159:27017,172.31.17.238:27017/?replicaSet=rs0')

db = client["chat_db"]

col = db["chat"]

nick = input('Create your nickname: ')

print('CHAT HISTORY')
for i in col.find():
    print(i["nick"] + ": " + i["msg"])
print('\n')

while True:
    msg = input('Write down the message: ')
    if msg == 'exit':
        break

    mydict = {"nick": nick, "msg": msg}

    x = col.insert_one(mydict)

    print('CHAT HISTORY')
    for i in col.find():
        print(i["nick"] + ": " + i["msg"])
        print('\n')
