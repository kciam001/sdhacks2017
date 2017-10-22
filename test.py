import analyze as analyze
import json as json
import collections
import subprocess

def setHash():
    keys = ["print", "+", "-", "*", "/", "if", "else"]
    values = [["display","print","show"], ["add","+","sum"], ["subtract","-","minus"], ["multiply","*","product"], ["/","divide"], ["if","check"], ["else","otherwise"]]
    hash = {k:v for k, v in zip(keys, values)}
    return hash
    
def entities(userInput, hash_table):
    entitiesJSON = analyze.analyze_entities(userInput)
    entitiesGroup = collections.namedtuple("entities", 'name salience')
    toReturn = []
    for entity in entitiesJSON["entities"]:
        curEntityGroup = entitiesGroup(name=entity['name'], salience=entity['salience'])
        toReturn.append(curEntityGroup)
    return toReturn
    
def syntax(userInput, hash_table):
    #intentMatch = open("./matchTable.json")
    #intentMatchJSON = json.load(intentMatch)

    #for i in intentHash:
        #print (i, intentHash[i])

    analysisJSON = analyze.analyze_syntax(userInput)
    contentGroup = collections.namedtuple("content", 'tag content')

    #print ("Size: ", len(analysisJSON["tokens"]))

    analyzedContent = [0 for i in range(0,len(analysisJSON["tokens"]))]

    j = 0

    for i in analysisJSON["tokens"]:
        curContentGroup = contentGroup(tag=i["partOfSpeech"]["tag"], content=i["text"]["content"])
        analyzedContent[j] = curContentGroup
        j += 1

    # for k in analyzedContent:
        # # print (k.content, " ")
        # for hashKey in hash_table:
            # # print (k, " ", intentHash[hashKey])
            # if k.content in hash_table[hashKey]:
                # print (k.content, " ", hashKey)

    return analyzedContent
    #print (json.dumps(analysisJSON, indent=2))

    #print ("\t", analysisJSON["tokens"][0]["partOfSpeech"]["tag"])
    #return analysisJSON

   
def analyze_dos(ent_list, syn_list): #the "math"
    split_executions = []
    i = 0
    string = ""
    print (syn_list)
    for pair in syn_list:
        if (pair.tag != 'VERB' or i==0) and pair.content not in ['>','<']:
            string += pair.content + ' '
        elif (pair.tag != 'VERB' or i==0) and pair.content in ['>','<']:
            string += pair.content
        else:
            if syn_list[i-1].tag == 'CONJ':
                string = string[:-(len(syn_list[i-1].content) + 1)]
                # print(string)
            split_executions.append(string)
            string = pair.content + ' '
        i += 1
    if string != "": #if string isnt empty
        split_executions.append(string)
    return split_executions
   
def main():
    intentHash = setHash();
    userInput = input("Enter string:")
    
    #check for words with salience, start search with that.
    # salience_list = entities(userInput, intentHash)
    # if salience_list != []:
        # for pair in salience_list:
            # salience_word = pair[0]
    entReturn = entities(userInput, intentHash) #list of pairs: [0] is word, [1] is saliency score
    synReturn = syntax(userInput, intentHash) #list of contents(pairs), each index is a word in the user input, pair.tag, pair.content

    split_UI_List = analyze_dos(entReturn, synReturn)
    print(split_UI_List)
    file = open('split_input.dat','w')
    for text in split_UI_List:
        file.write(text + '\n')
    p = subprocess.Popen(r'start cmd /c .\etot2.bat', shell=True)
    
    # temp = input("Duskull :3")
    
    #for i in syntax_json["tokens"]:
        #print (i["partOfSpeech"]["tag"], "\t", i["text"]["content"], "\n")
    
    #print (userInput)

if __name__ == '__main__':
    # sys.exit(main(sys.argv[1:])) #removes first command line argument because thats just the name of this file
    main()