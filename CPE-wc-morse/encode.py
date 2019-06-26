import sys
morse_code = { '-...': 'B', '-..-': 'X', '.-.': 'R', '.--': 'W', '.-': 'A', '..': 'I'
              , '..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U' , '-.-': 'K', '-..': 'D' , '---': 'O', '.--.': 'P'
             , '--': 'M', '-.': 'N', '....': 'H',  '...-': 'V' , '--.': 'G', '--.-': 'Q', '--..': 'Z', '-.-.': 'C', '-.--': 'Y', '-': 'T', '.---': 'J'
              , '--.': '¡', '-.-.': '¢', '-.-.': '£'}

def encodeMorse(toEncode):

    morse_code_inverted = {v: k for k, v in morse_code.items()}

    toEncodeDict = list(toEncode)
    
    output = []
    
    for char in toEncodeDict:
        try:
            output.append(morse_code_inverted[char.upper()])
        except:
            if char == ' ':
                output.append(' ')
            else:
                pass
        
    return ' '.join(output)    



if __name__ == '__main__':

    while 1:

      
        print(encodeMorse(input('To encode: ')))
        
        user_input = input(' button q = Exit):')

        if user_input == 'q':
            print("Good Bye")
            print("Morse EnCode Program Finished!!")
            break