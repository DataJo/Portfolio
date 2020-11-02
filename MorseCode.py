###########################################################
#          Joanne Lauer                                   #
#          4 May 2020                                     #
#          Morse Code                                     #
###########################################################

#Morse code is a code where each letter of the English alphabet, each digit, 
#and various punctuation characters are represented by a series of dots and dashes.
#
#Write a program that asks the user to enter a string, then converts that string
#to Morse code. 

#Global Variavles
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',  
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'}

#Gather Input
def GatherInput():
    Sentence = input("Enter a word, phrase, or sentence to comvert to Morse" +\
                     "Code:\n:").upper()
    return Sentence
  
def ConvertToMorse(Sentence):
    MyMorse = ''
    for Letter in Sentence:
        if Letter != ' ':
            MyMorse += MORSE_CODE_DICT[Letter] + ' '
        else:
            MyMorse += '   '
    return MyMorse

#Print out sentence in Pig latin


def PrintMorse(MyMorse):  
    print(f"The Morse Code Translation is:\n{MyMorse}")

#Perform Main Functions
def main():
    Sentence = GatherInput()
    MyMorse = ConvertToMorse(Sentence)
    PrintInfo = PrintMorse(MyMorse)
    



main()