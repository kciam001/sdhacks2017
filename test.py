import analyze as analyze
import json as json

def entities(userIput):
    return
    
def syntax(userInput):
    analysisJSON = analyze.analyze_syntax(userInput)
    #print (json.dumps(analysisJSON, indent=2))

    #print ("\t", analysisJSON["tokens"][0]["partOfSpeech"]["tag"])
    return analysisJSON
    return

if __name__ == '__main__':
    userInput = input("Enter string:")

    if entities(userInput) != []:
        print("Entities detected! do something userful with them lolol")
        
    syntax_json = syntax(userInput)
    
    
    for i in syntax_json["tokens"]:
        print (i["partOfSpeech"]["tag"], "\t", i["text"]["content"], "\n")
    
    print (userInput)
