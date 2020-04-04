'''
made by:  Aayush 9029
created at: April 3, 2020

A module that converts string to morse code and vice versa

'''
class Morse:
    def __init__(self, words):
        '''
        Takes in one parameter either morse code or letter / number / symbols and assings it to self.words
        '''
        self.codes = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-",
        " ": " "
        }
        self.words = words

    def stringToMorse(self):
        '''
        str -> str
        returns morse code variant of the string

        i am butterfly
        >>> ..  .- --  -... ..- - - . .-. ..-. .-.. -.--

        Cc Aa
        >>> -.-. -.-.  .- .-
        '''

        letters = list(self.words)
        output = ""
        for letter in letters:
            if letter.lower() in self.codes:
                output += self.codes[letter.lower()] + " "
            else:
                return KeyError
        return output

    def morseToString(self):
        '''
        str -> str
        returns the decoded string as morse code

        .- .--. .--. .-.. . 
        >>> apple

        ..  .- --  .-  -.. .. ... -.-. ---  -.. .- -. -.-. . .-.  ..--- ...--
        >>> i am a disco dancer 23
        '''
        
        words =  self.words.split("  ")
        output = ""
        
        for word in words:
            letters  = word.split()
            for letter in letters:
                for string, code in self.codes.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                    if letter == code:
                        output += string
            output += " "
        return output[:-1]

