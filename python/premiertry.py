class my_class(object):
    print("je serais data analyst!")
    print("quel est ton nom?")
    char = input()
    print("Enchanté "+char+ ", comment vas-tu aujourd'hui?")
    mood = input()
    if mood == "bien": print("je suis heureux de l'apprendre")
    elif mood == "bof": print("Ca pourrait aller mieux, c'est ça?")
    else: print("je ne comprend pas tout malheureusement")
    pass