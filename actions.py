from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']


def getCorrectPriceList(dataFrame, type):
    priceList = { 'low' : 'dfprice < 300', 'mid': '(dfprice >300) & (dfprice<700)', 'high' : 'dfprice > 700'}
    condition = priceList.get(type)
    dfprice = dataFrame['Average Cost for two']
    return dataFrame[eval(condition)]

def RestaurantSearch(City,Cuisine,Price):
    TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
    TEMP = getCorrectPriceList(TEMP,Price)
    TEMP = TEMP.sort_values(by='Aggregate rating', ascending=False)
    return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		results = RestaurantSearch(City=loc,Cuisine=cuisine,Price=price)
		response=""
		index = 0
		if results.shape[0] == 0:
			response= "no results"
		else:
			for restaurant in RestaurantSearch(loc,cuisine,price).iloc[:5].iterrows():
				index = index + 1
				restaurant = restaurant[1]
				response=response + F"{index}. {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
		restaurant_list = response
		dispatcher.utter_message("Showing you top rated restaurants:\n"+response)
		return [SlotSet('restaurant_list',response)]

class ActionSendMail(Action):
	def __init__(self):
		self.config = Config().getConfig()

	def name(self):
		return 'action_send_mail'

	def sendmail(self,recepientEmail, mail_content):
		self.config = Config().getConfig()
		sender_address = self.config['senders_email']
		sender_pass = self.config['senders_password']
		receiver_address = recepientEmail
		#Setup the MIME
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = 'Foodie - Restaurant List'   #The subject line
		#The body and the attachments for the mail
		message.attach(MIMEText(mail_content, 'plain'))
		#Create SMTP session for sending the mail
		session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
		session.starttls() #enable security
		session.login(sender_address, sender_pass) #login with mail_id and password
		text = message.as_string()
		print('text',text)
		print('message',message)
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		print('Mail Sent')
		
	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('mail_id')
		response = tracker.get_slot('restaurant_list')
		mail = ActionSendMail()
		mail.sendmail(MailID,response)
		return [SlotSet('mail_id',MailID)]