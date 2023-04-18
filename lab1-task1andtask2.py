# -*- coding: cp1252 -*-
#uppgift 1 och 2
def sockerkaka (antal):
#Gör om antal till float
    antal=antal + 0.0

    recept(antal)
    
    recept(4)
    
    recept(7)
#Receptet för en sockerkaka
#3 st ägg
#3 dl strösocker
#2 tsk vaniljsocker
#2 tsk bakpulver
#75 g smör
#1 dl vatten
#3 dl vetemjöl
def recept(antal):
#Sockerkaka per person 
    agg             =aggfunc(antal)
    socker          =float ((3*antal)/4)
    vaniljsocker    =float ((2*antal)/4)
    bakpulver       =float ((2*antal)/4)
    smor            =float ((75*antal)/4)
    vatten          =float ((1*antal)/4)
    vetemjol        =float ((3*antal)/4)
    print "Det här behövs för att göra en sockerkaka till",antal,"personer.",agg,"st ägg",socker,"dl strösocker",vaniljsocker,"tsk vaniljsocker",bakpulver,"tsk bakpulver",smor,"g smör",vatten,"dl vatten och",vetemjol,"dl vetemjöl!"
#Svårt att dela upp ägg i 3/4 där av detta:
def aggfunc(antal):
    agg = float((3*antal)/4)
    if agg > 1:
        agg = agg
    else:
        agg = 1.0
    return agg

