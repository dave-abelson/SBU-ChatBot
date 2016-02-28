import json
from pprint import pprint


with open("conversations.json") as data_file:
	data = json.load(data_file)

#pprint(data)
conversations =  data["conversations"]
for conversation in conversations:
	for sentence in conversation:
		print sentence







	
