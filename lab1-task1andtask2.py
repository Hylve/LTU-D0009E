# -*- coding: cp1252 -*-
#uppgift 1 och 2
def sockerkaka (antal):
#G�r om antal till float
    antal=antal + 0.0

    recept(antal)
    
    recept(4)
    
    recept(7)
#Receptet f�r en sockerkaka
#3 st �gg
#3 dl str�socker
#2 tsk vaniljsocker
#2 tsk bakpulver
#75 g sm�r
#1 dl vatten
#3 dl vetemj�l
def recept(antal):
#Sockerkaka per person 
    agg             =aggfunc(antal)
    socker          =float ((3*antal)/4)
    vaniljsocker    =float ((2*antal)/4)
    bakpulver       =float ((2*antal)/4)
    smor            =float ((75*antal)/4)
    vatten          =float ((1*antal)/4)
    vetemjol        =float ((3*antal)/4)
    print "Det h�r beh�vs f�r att g�ra en sockerkaka till",antal,"personer.",agg,"st �gg",socker,"dl str�socker",vaniljsocker,"tsk vaniljsocker",bakpulver,"tsk bakpulver",smor,"g sm�r",vatten,"dl vatten och",vetemjol,"dl vetemj�l!"
#Sv�rt att dela upp �gg i 3/4 d�r av detta:
def aggfunc(antal):
    agg = float((3*antal)/4)
    if agg > 1:
        agg = agg
    else:
        agg = 1.0
    return agg

