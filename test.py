import analyze as analyze
import json as json
import collections

def entities(userIput):
    entitiesJSON = analyze.analyze_entities(userInput)
    toReturn = []
    for entity in entitiesJSON["entities"]:
        toReturn.append((entity['name'], entity['salience']))
    return toReturn
    
def syntax(userInput):
    intentMatch = open("./matchTable.json").read()
    analysisJSON = analyze.analyze_syntax(userInput)
    contentGroup = collections.namedtuple("content", 'tag content')

    print ("Size: ", len(analysisJSON["tokens"]))

    analyzedContent = [0 for i in range(0,len(analysisJSON["tokens"]))]

    j = 0

    for i in analysisJSON["tokens"]:
        curContentGroup = contentGroup(tag=i["partOfSpeech"]["tag"], content=i["text"]["content"])
        analyzedContent[j] = curContentGroup
        j += 1

    

    return analyzedContent
    #print (json.dumps(analysisJSON, indent=2))

    #print ("\t", analysisJSON["tokens"][0]["partOfSpeech"]["tag"])
    #return analysisJSON

if __name__ == '__main__':

    userInput = input("Enter string:")

    salience_list = entities(userInput)
    if salience_list != []:
        print(salience_list)
        
    synReturn = syntax(userInput)

    print (synReturn)
    
    
    #for i in syntax_json["tokens"]:
        #print (i["partOfSpeech"]["tag"], "\t", i["text"]["content"], "\n")
    
    #print (userInput)
