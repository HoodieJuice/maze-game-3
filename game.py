money = 0
stick_weapon = 0
rustysword_weapon = 0
shortsword_weapon = 0
claymore_weapon = 0
stick = 2
rustysword = 10
shortsword = 20 
claymore = 30
def goback6():
    print("you start to follow the stranger for a while winding around corners until you come to small town like settlement")
    print("i say town but what i mean is hunk of junk this place is put together with bits of the wall weapons that either ran out of ammo or rusted away")
    print("the bones of.... something large and some peices of scrap wood and metal here and there")
    print("you lose sight of the guy but see what looks like him go down a small alley")
    print("you dont see anyone else around but hey it only seems like you're on the outskirts of town so you could go explore or you could follow him down the alley")
    print("explore or alley")
    answer8 = input()
    if answer8 == ("explore"):
        print("you start wandering into town past carts with what should have merchants or something but are left unattended")
    if answer8 == ("alley"):
        print("you follow him down the alley into another store *two stores you think kinda strange*")
        print("when you enter the stranger is gone but you do see a guy with some glasses a big nose and a moustache behind the counter")
        print("he looks awfully fimiliar but you cant put your finger on why")
        print("he speaks in a bit of a broken voice at first but he soon clears his throat and says")
        print("oodgay ayday owhay areyay ouyay")
        print("if you know what hes speaking you can say good in the language if not say what")
        answer9 = input()
        if answer9 == ("oodgay"):
            print("oh dammit you know pig latin")
            print("you died nerd")
            print("you are respawning guess where the start why the start because you didnt save and there isnt a save system anyway")
            goback()
        if answer9 == ("what"):
            print("ouyay ontday eakspay igpay atinlay eavelay")
            print("you think he wants you to leave so you leave")
            print("you walk back out the alley just in time to see a crowd of people walking towards you")
            print("you can run or hide")
def goback5():
    global money
    money += 2
    global stick
    global rustysword
    global shortsword
    global claymore
    global stick_weapon
    global rustysword_weapon
    global shortsword_weapon
    global claymore_weapon
    print("you have a look")
    print("""
    ##############################
    # cash = ${}                 #
    #                            #
    # stick = ${}                #
    #                            #
    # rusty sword = ${}          #
    #                            #
    # short sword = ${}          #
    #                            #
    # claymore = ${}             #
    #                            #
    # leave                      #
    ##############################
    to buy something go buy then the item you want to purchase if you want to leave go leave
    """.format(money, stick, rustysword, shortsword, claymore))
    answer5 = input()
    if answer5 == ("buy stick"):
            stick_weapon += 1
            money -= stick
            goback5()
    if answer5 == ("buy rusty sword"):
            rustysword_weapon += 1
            money -= rustysword
            goback5()
    if answer5 == ("buy short sword"):
            shortsword_weapon += 1
            money -= shortsword
            goback5()
    if answer5 == ("buy claymore"):
            claymore_weapon += 1
            money -= claymore
            goback5()
    if answer5 == ("leave"):
            print("you walk out of the store")
            print("you can either go left right or back in the store")
            answer6 = input()
            if answer6 in "go back""back":
                goback5()
            if answer6 == ("right"):
                print("you walk ahead filled with a confidence as now you know that there are others like you in the mazetrying to find the exit wont be as bad now")
                print("you watch as the strange man walks around a corner ahead of you going left but theres another path that heads right")
                print("which way do you wanna go?")
                answer7 = input()
                if answer7 == ("left"):
                    goback6()
                if answer7 == ("right"):
                    print("you walk ahead filled with a confidence as now you know that there are others like you in the maze,trying to find the exit wont be as bad now")
def goback4():
        print("you idiot.... is what i would say if you didnt just walk into a shop")
        print("theres an older looking man behind the counter and a traveler of sorts talking to him")
        print("the traveler walks past you as hes about to leave though he stops 'you arent from round here are you'")
        print("you say nothing 'look if you want something usefull from here you'll be searching for days.... altough i guess you dont have much of a choice'")
        print("'here take this' he throws a small backpack at you then leaves")
        print("you approach the counter the man glances at you then at some sort of tablet")
        print("not looking away from his tablet he points at another on the counter near him")
        goback5()
 
def goback3():
        print("you continue walking humming a tune as you go doesnt last long though")
        print("as now you come to a wall and a right turn you can either turn right or go back")
        answer3 = input()
        if answer3 == ("go back","back"):
                goback3()
        elif answer3 in "turn right""right""go right":
                print("you walk for a bit until you hear talking and see a hole in the wall")
                print("it could be enemies or friends but no clue do you want to enter or continue forward or go back?")
                answer4 = input()
                if answer4 == ("enter"):
                        goback4()
                if answer4 in "go back""back":
                        goback3()
                                
def goback2():
                print("you walk for a bit until you find a way to the right you can either continue forward go right or go back")
                answer2 = input()
                if answer2 in "go back""back":
                    goback()
                if answer2 in "continue forward""continue""forward":
                        goback3()
def goback():
        print("you can walk ahead or cry on the ground")
        answer = input()
        if answer in "walk ahead""ahead""forward":
            goback2()
        elif answer in "cry""cry on the ground":
            print("you drop to the floor and cry for about well you dont know cause you dont have any way of telling the time")
            print("you finally being done crying get up and atem")
            goback()




print("""
###########################################################
###########################################################
##            #                                      #   ##
##            #  #####MAZE#MADNESS #######  #######  #   ##
###############  #                 #     #  #     #  ######
##               ####A#TALE#OF#MAZE#######  #     #       #
##################                          #     #########
###########################################################
###########################################################
""")
print("disclaimer you will be given a map of the maze but no character icon")
print("this means that you have to guess your location in the maze instead of")
print("being directly told you may find shortcuts in the maze but there is also")
print("a chance to run into loops and dead ends so be careful of where you're headed")

print("early testing phases atm")
print("you wake up surrounded by walls on all sides until you turn around and realise you're only surrounded on 3 sides")

            
goback()
goback2()
goback3()
goback4()
goback5()
goback6()
