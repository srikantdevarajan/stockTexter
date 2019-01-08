from yahoo_fin.stock_info import *
from twilio.rest import Client
import datetime
##twilio info
##account_sid = this is where the twilio account_sid goes
##auth_token = this is where the twilio auth_token goes
client = Client(account_sid, auth_token)
##read text file
totalInfo = []
with open('singlestockprice.txt','r+') as myFile:
	for line in myFile:
		lineInfo = line.strip()
		totalInfo.append(lineInfo)
counter = 0
durationFinder=len(totalInfo)-1
	message = client.messages.create(from_='+twilio account phone number', body=string, to='+1(phone number you want to send to)')


while counter<len(totalInfo)-1:
	currentPE = get_quote_table(totalInfo[counter], dict_result=True).get('PE Ratio (TTM)')
	string='Hey, the pe ratio of {pticker} is {pvar}'.format(pticker=totalInfo[counter],pvar=currentPE)
	message = client.messages.create(from_='+twilio account phone number', body=string, to='+1(phone number you want to send to)')
	counter+=1
