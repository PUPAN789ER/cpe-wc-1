import sys
morse_code = { '-...': 'B', '-..-': 'X', '.-.': 'R', '.--': 'W', '.-': 'A', '..': 'I'
              , '..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U' , '-.-': 'K', '-..': 'D' , '---': 'O', '.--.': 'P'
             , '--': 'M', '-.': 'N', '....': 'H',  '...-': 'V' , '--.': 'G', '--.-': 'Q', '--..': 'Z', '-.-.': 'C', '-.--': 'Y', '-': 'T', '.---': 'J'
              , '--.': '¡', '-.-.': '¢,£'}



def decodeMorse(morseCode):

    morseCodeDict = morseCode.split(' ')
    
    output = []
    
    for morse in morseCodeDict:
        try:
            output.append(morse_code[morse])
        except:
            if morse == ' ':
                output.append(' ')
            else:
                pass
        
    return ' '.join(output)


if __name__ == '__main__':

    while 1:

        print(decodeMorse(input('To decode: ')))
        
        user_input = input(' button q = Exit):')

        if user_input == 'q':
            print("Good Bye")
            print("Morse EnCode Program Finished!!")
            break