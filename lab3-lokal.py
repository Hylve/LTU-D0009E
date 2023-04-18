#!/usr/bin/env python  
#Lab3
# -*- coding: cp1252 -*-
#Ordlista

#Menu-part
def  main_menu():
    print ("""
-------------------------------
Menu for ze awesome dictionary
-------------------------------
1: Insert
2: Lookup
4: Exit
-------------------------------       
    """)
def goodbye():
    print ("""
-------------------------------
Bye, bye!

     """)
    
#--------------------------------------------------------------------------
#Using Strings    
def stringDictionary():
    #Settings
    #String for word
    dicW = []
    #String for description
    dicD = []
    #Program starts
    menuclose = False
    while (menuclose != True):
        #Call menu text
        main_menu()
        #User input choice
        menuchoice = raw_input("Choose alternative: ")
        #Action according to input
        if menuchoice == '1':
            #Insert-part
            #
            #Insert word
            insertword = raw_input("Word to insert: ")
            if insertword in dicW:
                print ("The word you want to add already exists")
            else:
                insertdescription = raw_input("Description of word: ")
                dicW.append(insertword)
                dicD.append(insertdescription)

        elif menuchoice == '2':
            #Lookup-part
            #
            #Lookup word
            lookupword = raw_input("Word to lookup:")
            if lookupword in dicW:
                print "The Description of the word",lookupword, "is", dicD[dicW.index(lookupword)]
            else:
                print ("Cannot find the word:"), lookupword
    
        elif menuchoice == '3':
            #Delete-part
            print"#anropa funktionen funktionen"
        elif menuchoice == '4':
            #Exit-part
            menuclose = True
        else:
            #InputError-message
            print ("""

Nein, nein, nein!

            """)
    #Exit-message
    goodbye()
#---------------------------------------------------------------------------
#Using Tupler
def tuplerDictionary():
    #Tupler
    #Settings
    #List for Tuples
    lista = []
    #Program starts
    menuclose = False
    while (menuclose != True):
        #Call menu text
        main_menu()
        #User input choice
        menuchoice = raw_input("Choose alternative: ")
        #Action according to input
        if menuchoice == '1':
            #Insert-part
            #
            #Insert word
            founditinsert = False
            insertword = raw_input("Word to insert: ")

            for t in lista:
                if t[0]==insertword:
                    founditinsert = True
                    print ("The word you want to add already exists")
            if founditinsert == False:
                insertdescription = raw_input("Description of word: ")
                tuples = (insertword, insertdescription)
                lista.append(tuples)
                
        elif menuchoice == '2':
            #Lookup-part
            #
            #Lookup word
            lookupword = raw_input("Word to lookup:")
            foundit = False
            for tuples in lista:
                if lookupword == tuples[0]:
                    foundit = True
                    print "The Description of the word",tuples[0], "is", tuples[1]
            if foundit == False:
                 print ("Cannot find the word:"), lookupword
        elif menuchoice == '3':
            #Delete-part
            print"#anropa funktionen funktionen"
        elif menuchoice == '4':
            #Exit-part
            menuclose = True
        else:
            #InputError-message
            print ("""

Nein, nein, nein!

            """)
    #Exit-message
    goodbye()
#---------------------------------------------------------------------------
#Using dictionary
def dictionary():
    #Dictionary
    dictionary = {}
    #Program starts
    menuclose = False
    while (menuclose != True):
        #Call menu text
        main_menu()
        #User input choice
        menuchoice = raw_input("Choose alternative: ")
        #Action according to input
        if menuchoice == '1':
            #Insert-part
            #
            #Insert word
            insertword = raw_input("Word to insert: ")
            if insertword in dictionary:
                print ("The word you want to add already exists")
            else:
                insertdescription = raw_input("Description of word: ")
                dictionary[insertword] = insertdescription
        elif menuchoice == '2':
            #Lookup-part
            #
            #Lookup word
            lookupword = raw_input("Word to lookup:")
            #
            if lookupword in dictionary:
                    print "The Description of the word",lookupword, "is", dictionary[lookupword]
            else:
                print ("Cannot find the word:"), lookupword
        elif menuchoice == '3':
            #Delete-part
            print"#anropa funktionen funktionen"
        elif menuchoice == '4':
            #Exit-part
            menuclose = True
        else:
            #InputError-message
            print ("""

Nein, nein, nein!

            """)
    #Exit-message
    goodbye()
#---------------------------------------------------------------------------    
    
