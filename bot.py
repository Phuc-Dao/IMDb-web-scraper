from watson_developer_cloud import AssistantV1
import  json
import requests
#This is to login with the credentials.
assistant = AssistantV1(
    version='2017-10-16',
    username="5daf4d8e-fb8d-4421-8551-88f435aba7e3",
    password= "pR7yDGbAkFO4",
    url="https://gateway.watsonplatform.net/assistant/api",
)

#Testing requests
api_key = 'AIzaSyBoWrOdKl132Spk5FIuO-NMv61nVMlQ2MI'
api_url =  'https://maps.googleapis.com/maps/api/place/findplacefromtext/output?parameters'

#This holds the various datas
space_id = 'b2348aa5-ad2c-4563-a6fd-287a17bdec14'

#testing user input
response = assistant.list_intents('b2348aa5-ad2c-4563-a6fd-287a17bdec14')

#This will return a json object with values
message = assistant.message(workspace_id=space_id, input = {"text" : "hello"})
print(json.dumps(message))
print(json.dumps(message).find("text"))

