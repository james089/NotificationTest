import fbchat 
from getpass import getpass
from fbchat.models import *

username = "stevenmoleskin@gmail.com" #str(input("Username: "))
client = fbchat.Client(username, getpass())

thread_id = client.uid
thread_type = ThreadType.USER

#no_of_friends = 1 #int(input("Number of friends: "))
#for i in range(no_of_friends):

name = str(input("Who do you want to chat with?"))
friends = client.searchForUsers(name)  # return a list of names
friend = friends[0]
if(friend.is_friend):
    msg = str(input("Message: "))
    sent = client.send(Message(text = msg), friend.uid, thread_type)
    if sent:
        print("Message sent succed fssfully!")