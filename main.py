from scripts.speech import speech
import os
DecisionVar = -1
while True:
    print("to give command press 1 to end anything else")
    DecisionVar = int(input())
    if(DecisionVar == 1) :
        txt = speech().lower()
        lstxt = list(txt.split())
        """
        create:  create a new file <base_name_of_the_file>
        eidt: edit <base_name_of_the_file>
        compile: compile <base_name_of_file>
        run : run <base_name_of_file>
        Delete c file:  delete <file_base_name>
        delete compiled file : delete compiled <file_base_name>
        """
        print(txt)
        print("if you wanted to run the command say yes else no")
        tmtxt = speech().lower()
        if(tmtxt=="yes"):
            if(lstxt[0]=="create"):
                commandtxt = "touch " + lstxt[4] + ".c"
                os.system(commandtxt)
            elif lstxt[0]=="compile":
                commandtxt = "gcc " + lstxt[1] + ".c -o " + lstxt[1]
                os.system(commandtxt)
            elif lstxt[0]=="delete":
                if lstxt[1] == "compiled":
                    commandtxt = "rm " + lstxt[2]
                else :
                    commandtxt = "rm " + lstxt[1] + ".c"
                os.system(commandtxt)
            elif lstxt[0] == "run":
                commandtxt = "./" + lstxt[1]
                os.system(commandtxt)
            elif lstxt[0] == "edit":
                commandtxt = "gedit " + lstxt[1] + ".c"
                os.system(commandtxt)
            else:
                print("touch " + lstxt[4] + "." + lstxt[2])
    else:
        break