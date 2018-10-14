from twilio.rest import Client
account_sid='AC0befa5d76b6bdcae45e527c55bf1be63'
auth_token='33baf3a5f7a7974d8414d5be5f6de12f'
client=Client(account_sid, auth_token)
call = client.calls.create(url='https://handler.twilio.com/twiml/EH128f1d15e602f30eec6ccea40192101f?Name='+'Amrish'+'&Cycle='+'MH420'+'&Landmark='+'Quadrangle',to='+13316845287',from_='+18125944162')

print(call.sid)