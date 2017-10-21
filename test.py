import analyze as analyze
import json as json

if __name__ == '__main__':
    userinput = input("Enter string:")
    analysisJSON = analyze.analyze_syntax(userinput)
    #print (json.dumps(analysisJSON, indent=2))

    #print ("\t", analysisJSON["tokens"][0]["partOfSpeech"]["tag"])

    for i in analysisJSON["tokens"]:
        print (i["partOfSpeech"]["tag"], "\t", i["text"]["content"], "\n")
    
    print (userinput)
