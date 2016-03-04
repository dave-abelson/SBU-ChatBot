import json, re, collections
from pprint import pprint


def words(text):
    """ Parse user text to words """
    return re.findall('[a-z]+', text.lower())

def editDistance(w1, w2):
    """ Levenshtein distance """
    a = min(w1, w2)
    b = max(w1, w2)
    n = len(a)
    m = len(b)

    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i] + [0]*n
        for j in range(1, n+1):
            add, delete = previous[j]+1, current[j-1] + 1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
    return current[n]
    
def findResponse(inp,conversations):
    resp = ""
    currentDist = 1000
    for conversation in conversations:
        for i in range(len(conversation)):
            newDist = editDistance(inp,conversation[i])
            if newDist < currentDist:
                currentDist = newDist
                if (i+1) >= len(conversation):
                    resp = "LOL"
                else:
                    resp = conversation[i+1]
    return resp
                


if __name__=="__main__":
    with open("conversations.json") as data_file:
	data = json.load(data_file)

    conversations =  data["conversations"]
    while(True):
        inp = raw_input("You> ") 
        print("Bot> " + findResponse(inp,conversations))


