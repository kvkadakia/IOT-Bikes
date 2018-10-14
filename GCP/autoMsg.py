from twilio.rest import Client
account_sid='AC0befa5d76b6bdcae45e527c55bf1be63'
auth_token='33baf3a5f7a7974d8414d5be5f6de12f'
client=Client(account_sid, auth_token)
message=client.messages.create(to="+13128046895",from_="+18125944162",body="High temperatures detected!")
print('sent: ',message)