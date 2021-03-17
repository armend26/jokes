#codebyarmendostaku

import requests  
import random 

API_KEY = "https://v2.jokeapi.dev/joke/"
ctg = ["Pun","Spooky","Misc","Programming","Dark","Christmas"]
category = random.choice(ctg)
response = requests.get(API_KEY+category)   
data = response.json() 

#printthejoke
print("-> Category : ",data["category"])
print("\n-> Type of the joke : ",data["type"])
if data["type"] == "single" :
	print("\n-> Joke : ",data["joke"])
else:
	print("\n-> Setup : ",data["setup"])
	print("\n-> Delivery : ",data["delivery"])
