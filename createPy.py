import tkinter
from tkinter import *

def main():
    file = open('intent_list.dat','r');
    intentList = []
    for text in file:
        intentList.append(text)

    action = "";
    outFile = open('outputPy.py','w')
    mathVar = 0
    for intent in intentList:
        action = intent[7:intent.index(" ")]
        lineOfCode = "";
        if action == "print":
            textToPrint = "";
            textToPrint = intent[intent.index("{")+7:-2]
            lineOfCode = action + "(\""+textToPrint+"\")\n"
            outFile.write(lineOfCode)
        elif action == "math":
            index1 = intent.index("{")
            index2 = intent.index("}")
            args = intent[index1+1:index2]
            argsList = args.split()
            leftArg = ""
            rightArg = ""
            op = ""
            opBool = False
            for i in argsList:
                arg1Found = i.find("arg1")
                arg2Found = i.find("arg2")
                opFound = i.find("op")
                if (arg1Found != -1):
                    leftArg = i[5:]
                if (arg2Found != -1):
                    rightArg = i[5:]
                if (opFound != -1 and not opBool):
                    opBool = True
                    op = i[3:]
                    if (op == "add"):
                        op = "+"
                    elif (op == "subtract"):
                        op = "-"
                    elif (op == "multiply"):
                        op = "*"
                    elif (op == "divide"):
                        op = "/"
            #leftArg = intent[index1+7:intent.index("op")-1]
            #op = intent[intent.index("op")+3:intent.index("op")+4] #might have to change if op can be "add" or "minus"
            #rightArg = intent[intent.index("arg2")+5:-2]
            var = "var"+ str(mathVar)
            mathVar += 1
            lineOfCode = var + " = " + leftArg + op + rightArg + "\n"
            outFile.write(lineOfCode)
        elif action == "loop":
            index1 = intent.index("{")
            index2 = intent.index("}")
            args = intent[index1+1:index2]
            argsList = args.split()
            var = ""
            arg1 = ""
            logic = ""
            target = ""
            op = ""
            forBool = False
            for i in argsList:
                varFound = i.find("var")
                arg1Found = i.find("arg1")
                logicFound = i.find("logic")
                targetFound = i.find("target")
                opFound = i.find("op")
                if (varFound != -1):
                    var = i[4:]
                if (arg1Found != -1):
                    arg1 = i[5:]
                if (logicFound != -1):
                    logic = i[6:]
                    if (logic == "greater than"):
                        logic = ">"
                    elif (logic == "greater than or equal to"):
                        logic = ">="
                    elif (logic == "less than"):
                        logic = "<"
                    elif (logic == "less than or equal to"):
                        logic = "<="
                if (targetFound != -1):
                    target = i[7:]
                if (opFound != -1):
                    op = i[3:]
                    forBool = True
            if (forBool):
                lineOfCode = "for i in range(" + arg1 + "):\n\t"
            else:
                lineOfCode = "while (" + var + logic + target +"):\n\t"
            outFile.write(lineOfCode)
    

if __name__ == '__main__':
    main()
    root = tkinter.Tk()
    root.title("Output Data")

    T = Text(root, height=2, width=30)

    T.pack()

    myfile = open('outputPy.py','r')
    loadedfile = myfile.read()
    myfile.close()
    T.insert("end", loadedfile)
    root.mainloop()