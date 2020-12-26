# Joshua Revels
# CS 325
# Portfolio Project


import random

incorrectInputError = "INCORRECT INPUT, FEEBLE-MINDED MORTAL!!! I SAID ENTER A 4 DIGIT CODE! " \
                          "FOUR DISTINCT NUMBERS!!! NO REPEATS!! NO ZEROES!! TRY AGAIN!"


def playGame(thisGuess, totalGuesses, thisAnswer):

    if totalGuesses == 0:
        if thisGuess < 1000 or thisGuess > 9999:
            print(incorrectInputError)
            print("")
            thisGuessInfo = [False, totalGuesses, thisAnswer]
            return thisGuessInfo
        thisGuess = list(map(int, str(thisGuess)))
        dupeChecker = 0
        while dupeChecker < 4:
            if dupeChecker == 0:
                if thisGuess[dupeChecker] == thisGuess[1]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[2]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[3]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
            if dupeChecker == 1:
                if thisGuess[dupeChecker] == thisGuess[0]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[2]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[3]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
            if dupeChecker == 2:
                if thisGuess[dupeChecker] == thisGuess[0]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[1]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[3]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
            if dupeChecker == 3:
                if thisGuess[dupeChecker] == thisGuess[0]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[1]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[2]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
            dupeChecker = dupeChecker + 1
        for y in thisGuess:
            if y == 0:
                print(incorrectInputError)
                print("")
                thisGuessInfo = [False, totalGuesses, thisAnswer]
                return thisGuessInfo

        thisGuess = int(''.join(map(str, thisGuess)))

        answerList = []

        answerLen = 4

        while len(answerList) < answerLen:
            num = random.randrange(1, 10)
            while num in answerList:
                num = random.randrange(1, 10)
            answerList.append(num)

        answerCode = int(''.join(map(str, answerList)))

        totalGuesses = totalGuesses + 1

        if thisGuess == answerCode:
            return [True, totalGuesses, answerCode]
        else:
            answerList = list(map(int, str(answerCode)))

            thisGuess = list(map(int, str(thisGuess)))

            i = 0

            correct = 0

            partialCorrect = 0

            while i < 4:
                for x in range(0, 4):
                    if thisGuess[x] == answerList[i]:
                        if x == i:
                            correct = correct + 1
                            break
                        else:
                            partialCorrect = partialCorrect + 1
                            break
                    elif thisGuess[x] != answerList[i]:
                        continue
                i = i + 1

            print("You got ", correct, " exact match(es) and ", partialCorrect, " partial match(es).")
            print("")
            thisGuessInfo = [False, totalGuesses, answerCode]
            return thisGuessInfo

    else:

        if thisGuess < 1000 or thisGuess > 9999:
            print(incorrectInputError)
            print("")
            thisGuessInfo = [False, totalGuesses, thisAnswer]
            return thisGuessInfo
        thisGuess = list(map(int, str(thisGuess)))
        dupeChecker = 0
        while dupeChecker < 4:
            if dupeChecker == 0:
                if thisGuess[dupeChecker] == thisGuess[1]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[2]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[3]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
            if dupeChecker == 1:
                if thisGuess[dupeChecker] == thisGuess[0]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[2]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[3]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
            if dupeChecker == 2:
                if thisGuess[dupeChecker] == thisGuess[0]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[1]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[3]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
            if dupeChecker == 3:
                if thisGuess[dupeChecker] == thisGuess[0]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[1]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
                if thisGuess[dupeChecker] == thisGuess[2]:
                    print(incorrectInputError)
                    print("")
                    thisGuessInfo = [False, totalGuesses, thisAnswer]
                    return thisGuessInfo
            dupeChecker = dupeChecker + 1
        for y in thisGuess:
            if y == 0:
                print(incorrectInputError)
                print("")
                thisGuessInfo = [False, totalGuesses, thisAnswer]
                return thisGuessInfo

        thisGuess = int(''.join(map(str, thisGuess)))

        totalGuesses = totalGuesses + 1

        if thisGuess == thisAnswer:
            return [True, totalGuesses, thisAnswer]
        else:
            answerList = list(map(int, str(thisAnswer)))

            thisGuess = list(map(int, str(thisGuess)))

            i = 0

            correct = 0

            partialCorrect = 0

            while i < 4:
                for x in range(0, 4):
                    if thisGuess[x] == answerList[i]:
                        if x == i:
                            correct = correct + 1
                            break
                        else:
                            partialCorrect = partialCorrect + 1
                            break
                    elif thisGuess[x] != answerList[i]:
                        continue
                i = i + 1

            print("You got ", correct, " exact match(es) and ", partialCorrect, " partial match(es).")
            print("")
            thisGuessInfo = [False, totalGuesses, thisAnswer]
            return thisGuessInfo


if __name__ == '__main__':
    print("")
    print("")
    print("WELCOME TO....")
    print("")
    print("    @@@%   @@@@     @@@@       @@@@@@/# @@@@@@@@@/ @@@@@@@@@  /@@@@@@@@   *@@@.  /@@@/   @@&   @@@*   %@@   @@@@@@@@  ")
    print("    @@@@% @@@@&    @@  @@    @@@@          @@@     @@@        *@@    @@@  ,@@@@ %@%@@*   @@%   @@@@@# %@@   @@@    @@@  ")
    print("    @@ #@@& @@&   @@@@@@@@       @@@@      @@@     @@@@@@@    *@@@@@@@/   ,@@ @@@. @@*   @@%   @@/ %@@@@@   @@@    @@@  ")
    print("    @@  */  @@&  @@      @@         @@@    @@@     @@@        *@@   (@@   ,@@  @   @@*   @@%   @@/    @@@   @@@    @@&  ")
    print("    @@  */  @@&  @@      @@  @@@@@@@@@     @@@     @@@@@@@@@  *@@   (@@   ,@@      @@*   @@%   @@/    @@@   @@@@@@@@&  ")
    print("")
    print("")
    print("    For an ideal experience, please set the width and length of your terminal to at least 130px and 50px, respectively!")
    print("")
    print("")
    print("                                             How to Play:")
    print("         The evil A.I., SHODAN, is up to her old tricks again! This time, she's trapped your soul! You'll need")
    print("         to guess her 4 digit escape code to be released. The code will be four distinct, non-zero integers,.")
    print("         ranging from 1 to 9. You will have 15 guesses to correctly guess the code. Otherwise your soul")
    print("         will be trapped forever! After each guess, SHODAN will tell you if you get any of the code numbers")
    print("         exactly right (exact match),or if you have correct numbers in the wrong position (partial match).")
    print("                                 Good luck! Beat SHODAN once and for all!")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("          HAHAHAH!!! I HAVE TRAPPED YOUR SOUL! DECODE THE 4 DIGIT ESCAPE SEQUENCE OR YOUR SOUL IS MINE FOREVER!")
    print("")
    print("")
    print("")
    print("")
    correctGuess = False
    gameComplete = False
    guessCounter = 0
    answer = None
    guessInfo = [correctGuess, guessCounter, answer]
    try:
        guess = int(input("GUESS THE 4 DIGIT ESCAPE CODE, MORTAL:  "))
        print("")
        guessInfo = playGame(guess, guessInfo[1], guessInfo[2])
        while gameComplete is False:
            if guessInfo[0] is True:
                gameComplete = True
                break
            if guessInfo[1] > 14:
                gameComplete = True
                break
            else:
                print("")
                print("YOU HAVE " + str(15 - guessInfo[1]) + " GUESSES REMAINING!")
                print("")
                try:
                    guess = int(input("GUESS THE 4 DIGIT ESCAPE CODE, MORTAL:  "))
                    print("")
                    guessInfo = playGame(guess, guessInfo[1], guessInfo[2])
                except ValueError:
                    print("")
                    print(incorrectInputError)
                    print("")
        if guessInfo[0] is True:
            print("")
            print("")
            print("")
            print("               You Win! You defeated the evil SHODAN! WELL DONE!")
            print("")
            print("")
            print("")
        else:
            print("")
            print("")
            print("                                         THE CORRECT ANSWER WAS ", guessInfo[2], "!!!!")
            print("")
            print("                                     YOUR SOUL IS MIIIIIIIIIINNNEEEEEEEEEE!!!!!!!!")
            print("")
            print(
                "##########################################################################################################################")
            print(
                "######           #####     #####      #####      ###        ########         ###  #########  ###        ###        #######")
            print(
                "######  ############   ###   ###   ##  ###  ##   ###   #############  #####  ####  #######  ####  #########  #####  ######")
            print(
                "######  ############   ###   ###   ###  #  ###   ###      ##########  #####  #####  #####  #####      #####  ####  #######")
            print(
                "######  ##       ###         ###   ####   ####   ###   #############  #####  ######  ###  ######  #########       ########")
            print(
                "######  ######   ###   ###   ###   ###########   ###   #############  #####  #######  #  #######  #########  ####   ######")
            print(
                "######           ###   ###   ###   ###########   ###        ########         ########   ########        ###  ######  #####")
            print(
                "##########################################################################################################################")
            print(
                "    ..    *      .  ,./ . ./. .,.  ...,.../,*,(/(/*(/((&(((((((((%&(*#/(##(*,///..,..     .   (       ...  .  ...,. .   ")
            print(
                "....    ...        .. * *. ,,.. ,,.../,*,*/,,*/(&*&//@/(@##((##&(#&((@/&#(/*/,/,, ,,.  .   .,. ..   .        ....     . ")
            print(
                ".  ...   , .      .  ..   ,..*,..*,. ,,/,*****//(&#%(&%&#@@((%@##(&&/#@////////,/. /.... ,   .           ....           ")
            print(
                "*.      .. .      ... ....  .,  . ,*,  ,,/**//%*(%(%@&#((@#%%%&#((@@@##%*&(///*,*,*,,. ,. ..          .,.             .,")
            print(
                "  .                  ....,.    ,. ,,**/ .,*/#**/%%(&%(%(%@(%#%&###@(@&#&/,/#**,,*(*..., ,.         .,.. .            ..")
            print(
                "   *                .      ....,,... /,,/.*/#*%/(#/@##%%(@(%%#%%##@#%%#((#/%,*,/*.,.,,          .,..          ,*.")
            print(
                "   ..                .         ......*.,.*/,//(#(&(/##%#/&#%(%%/(#@((((%(#//*(*,..       ..  ....         ...")
            print(
                "           ....                    ....,,,**,%/((&*##/###%(/((/#(%@(####(((//*,,**, ,  ..  ..,        ...         ..,*//")
            print(
                "     .,. /.      ..         . .  ....*..*,,*/*,*/#(/##%#%&%%%%#&%#@##/(#/*/**,*(, ,.. , ..        ,.        ..*//##/**/.")
            print(
                "**/##(/(#(/*(.          .     . ...,..,,*,,,,,,,////(#%##&##%##&##&#(//(//*,**,,.....,. ....   ..     .*/(##(/*,    ./  ")
            print(
                ",#.      .,//(##((.          .   ..,,.*,,.,,,/,.*(*(/(#((#((/(/%(##((//(*,/,,*..,*.,*.,..            ,(/*.         /,.,,")
            print(
                "   /.        .,....,(***,.      .. ....**.,,,***/,,/***/#/(%#%(((/**(,,*/.,,...*. . ..      *//%#%#%#%#.,##(.         .(#////")
            print(
                "/  .*.         ./,     .,,(/,.   .  . ......**,,./*,/(/*//#((/#(#/(**,#(*,,,,...,,,,,,,,,.,*//(##%#%(#*.  .  ...,**..,,,,")
            print(
                " ,(..,#**/**/**,,..**#*,..,///**(*.              ,**,*/*/((((#/(/*/(.*,.                *########%#(((//*****,,.*....,*.#")
            print(
                "..,,,,*****/*/***,,,,.....**,**,,,.  *****  ***  ,.,..,.*//(/#*(**,, ,..  ***  *****  ...**,.,   .*..        .      . ..")
            print(
                "      .    .,...       ,*. .,,,//,..  ****  *****   ....*//(/(//.,.....  ****  ****   /**,.  .(.         ,..    *.    .")
            print(
                " ..     .,,               .,.,**/((/**  **  ******   ..(..  *,,(((/ ,,  *****. ***   *,,**,*,.      ..,,..   .,,,.%   .")
            print(
                "      ...,,.      . .  . .   .,/*///(//,,,,,,,,,.../,#.*.((..*(/*.,.*#(/,,,,,,,,,,,/#////**/,.       .,,,..   ,/.")
            print(
                "     .     . .  .,...... ,    .,,//((#/#%%&%#((//**#,/#/  /(/*.,..//(/%((/((*//((/*/((*,.      .... ..             .")
            print(
                "    .                     .    .,,**(/%%%&&&%%&#(/*#**//  /((/.,,.,*/*(/(%///(((#(*,*,,. .,.......,.,,,,*.              ")
            print(
                "..,...... . .... ..... .  ....  .,.,//*/(((%%#/#/(**,**.  /((*..,.,**,*((/(#((%///*,,*..          ... .                 ")
            print(
                ".       .              .         ..*.*,////(/((/*/,,.,,,  *//, .,  ,*,***///////***, ..                  . .        .,,,")
            print(
                "                 .         ..       .,*,/*(((,((////...,  *//, .,  ./,*(///(**//**.*     .                              ")
            print(
                "/  *    .           ..               .,,*,*/**/*(//** ,*. **/*  .. ,.(*/////*,* ....     ..       ...    .")
            print(
                "                        .   .         . ,.,,,#*//,/.* ,*.,/(%(.**,...(/(*/*.*,.  .         . ..       .. .        . ,")
            print(
                "       .                              . ..  ,*/**((**,   //#%%*..  .*(/(//**.*.    ,     .   . ....         ..        ..")
            print(
                "                               .......    ..  *///(/,/**         .(***/(**,    ...    ,, ,   .. .......,,,,*******,,,,.,")
            print(
                "    .,/#((((((((///***,,,,,*//(((////*,   ......**/((#(***    ,,(/#(((/*,,  ... ...   ..,,,,.  ..*,*****,,,,**********,*")
            print(
                "   ,*/,.                                 ..., ,,.          ..             .,..,/(,..,        . ....         ... ..,.,. .")
            print(
                "//*,      .                  ..,,,*/((#((//*. .,,*  .*..,.    .  ..,,   .,..   . ...,/(**,.    .    .,, .  .    .      .")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
    except ValueError:
        print("")
        print(incorrectInputError)
        print("")
