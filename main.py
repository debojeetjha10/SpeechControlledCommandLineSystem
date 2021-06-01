from scripts.speech import speech
import os
import colorama
from colorama import Fore, Style
DecisionVar = -1
while True:
    print("to give command press 1 to end anything else")
    DecisionVar = int(input())
    if(DecisionVar == 1) :
        txt = speech().lower()
        lstxt = list(txt.split())
        """
        The commands should be structured like below.

        create:  create a new file <base_name_of_the_file>
        eidt: edit <base_name_of_the_file>
        compile: compile <base_name_of_file>
        run : run <base_name_of_file>
        Delete c file:  delete <file_base_name>
        delete compiled file : delete compiled <file_base_name>
        """
        print(Fore.CYAN + "You have said : " + txt)
        print(Style.RESET_ALL)
        print(Fore.BLUE+ "if you wanted to run the command say yes else no")
        print(Style.RESET_ALL)
        tmtxt = speech().lower()
        if(tmtxt=="yes"):
            print(Fore.GREEN + "Running your command.....")
            print(Style.RESET_ALL)
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
            print(Fore.RED + "Aborting.....")
            print(Style.RESET_ALL)
    else:
        break