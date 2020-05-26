from twilio.rest import Client

def sendSMS(content):
    # the following line needs your Twilio Account SID and Auth Token
    client = Client("ACb0faf3593fd80b3f1953f84ec58da39b", "096f7ade2a71587d27db26bd8582f541")

    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to="+19499811593",
                           from_="+18136963278",
                           body=content)


#=============Main============================
if __name__ == "__main__":
    sendSMS("Hello, this is a message from python code!")
    print("Program end")