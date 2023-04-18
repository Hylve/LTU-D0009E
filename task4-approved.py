import traceback

class phonebook(object):
    def __init__(self):
        #Dictionary
        self.phonedictionary = {}
        #commands
        commandophonebook = {
"add":      self.addnew,    "lookup":   self.lookup, 
"alias":    self.alias,     "save":     self.save,
"load":     self.load,      "remove":   self.remove,
"print":    self.printlist, "quit":     self.quitz,
"change":   self.change,    "help":     self.printoption
}
        #Allowed chars
        self.numbercharcheck = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '+']

        while True:
            #the prompt
            prompt = raw_input ("PhoneBook> ")
            #input with split
            userinput = prompt.split()
            try:
                commandophonebook[userinput[0]](*userinput[1:])
            except SystemExit:
                #Exit message
                print "\n" "C'ya l8er"
                #Program stops
                break
            except TypeError:
                #If a functions argument isnt given or correct
                print "\n" "The argument isn't valid. type help for help" "\n"
                traceback.print_exc()
            except KeyError:
                #If a 
                print "\n" "The opntion dosn't exists, type help for help" "\n"
            except ValueError:
                print "no no you got ValueError"
            except NameError:
                print "you got NameError"


    def addnew(self, name, number):
        #add

        if number in self.phonedictionary.keys():
            print "That number already exists"
        else:
            self.phonedictionary[number] = [name]
            print "\n" "You have added the name: ",name,"with the number: ",number,"\n"


        
    def lookup(self, name):
        #lookup
        foundNameLookup = False
        for number, names in self.phonedictionary.items():
            print number, names
            if name in names:
                lookupline = name + " has the numer " + number
                print lookupline
                foundNameLookup = True
        if foundNameLookup != True:
            print "No number belgons to " + name
    
    def save(self, savefilename):
        #save
        f = open(savefilename, "w")
        for number, names in self.phonedictionary.items():
            #collect data
            fileline = number + ";" + ";".join(names) + "\n"
            #print number;names;alias
            f.write(fileline)
        print "\n" "Save complete" "\n"
        
    def load(self, openfilename):
        #load
        self.phonedictionary = {}
        with open(openfilename, "r") as f:
            for line in f:
                splits = line.strip("\n").split(";")
                number = splits[0]
                name = splits[1:]
                self.phonedictionary[number] = name
        print "Have loaded " + openfilename + " successfully"
            
    
    def remove(self, name, deleteNumber=None):
        #remove
        seekNumber = self.seekAndDestory(name)
        if seekNumber > 0:
            #If person is found
            del self.phonedictionary[seekNumber]
            print "Have successfully removed " + name + " and the all the data"
        elif seekNumber == 0:
            print "Cannot found the name: " + name
        elif seekNumber < 0:
            if deleteNumber:
                del self.phonedictionary[deleteNumber]
            else:
                print "More then one person has the name " + name + "please input a number"
                
    def alias(self, name, aliasName, aliasNumber=None):
        #alias
        seekNumber = self.seekAndDestory(name)
        if seekNumber > 0:
            self.phonedictionary[seekNumber].append(aliasName)
        elif seekNumber == 0:
            print "Cannot found the name: " + name
        elif seekNumber < 0:
            if aliasNumber:
                self.phonedictionary[aliasNumber].append(aliasName)
            else:
                print"More then one person goes under the name " + name + "pleas input number"
    
    def change(self, name, newNumber, changeNumber=None):
        #change
        seekNumber = self.seekAndDestory(name)
        if seekNumber > 0:
            #If person is found
            self.phonedictionary[newNumber] = self.phonedictionary[seekNumber]
            del self.phonedictionary[seekNumber]
            print name+"'s number has changed from " + seekNumber + " to " + newNumber
            
        elif seekNumber < 0:
            if changeNumber:
                self.phonedictionary[newNumber] = self.phonedictionary[changeNumber]
                del self.phonedictionary[changeNumber]
                
            else:
                print "More then one person has the name " + name + " pleace inut"
        elif seekNumber == 0:
            print "Cannot found the name: " + name
    
    def printlist(self):
        #print
        for number, names in self.phonedictionary.items():
            listToPrint = number + " " + " ".join(names) + "\n"
            print listToPrint
            
    def quitz(self):
        #quit
        exitinput = raw_input("Are you sure you want to quit? y or n: ")
        if exitinput == "y":
            raise SystemExit
        else:
            return
        
    def seekAndDestory(self, name):
        #init-values
        seek = 0
        seekNumber = 0
        #do the search
        for number, names in self.phonedictionary.items():
            if name in names:
                seekNumber = number
                seek += 1
        if seek == 1:
            return seekNumber
        elif seek == 0:
            return 0
        else:
            return -1
    
    def printoption(self):
        #help
        print ("""

Avilable options is:
-------------------------------------------------
add     |   use it like this: add name number
lookup  |   use it like this: lookup name
alias   |   use it like this: alias name nickname
change  |   use it like this: change name number
save    |   use it like this: save filename
load    |   use it like this: load filename
print   |   use it like this: print
quit    |   use it like this: quit
help    |   use it like this: help
-------------------------------------------------
        """)

phonebook()
