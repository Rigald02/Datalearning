class my_class(object):
    print("je serais data analyst!")
    print("quel est ton nom?")
    char = input()
    print("Enchanté "+char+ ", comment vas-tu aujourd'hui?")
    mood = input()
    if mood == "bien": print("je suis heureux de l'apprendre")
    elif mood == "mal": print("bah, ca ira mieux demain!")
    elif mood == "bof": print("Ca pourrait aller mieux, c'est ça?")
    elif mood := "ca peut aller": print ("prend un coup de coca ca reboost")
    elif mood := "la cata": print("va dormir ca ira mieux demain")
    else: print("je ne comprends pas tout malheureusement")
    pass
#else if n'existe pas:
#if est une option, elif les autres option, else est toute les autres option.
#basiquement, if et elif sont des cas de boolean true, else est un boolean false

# les symboles := et == sont la meme chose(?)
