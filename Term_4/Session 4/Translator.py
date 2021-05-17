class Translator:
    def __init__(self):
        pass

    def translate_to_morse(self, string=''):
        morse_string = ""
        for i in string:
            try:
                morse_string += self.morse_codes[i.upper()]
            except:
                morse_string += i
            finally:
                morse_string += ' '
        return morse_string


    def translate_to_leet(self, string=''):
        leet_string = ""
        for i in string:
            try:
                leet_string += self.leet_codes[i.upper()]
            except:
                leet_string += i
                pass
        return leet_string

    morse_codes = {"A": ".-",
                   "B": "-...",
                   "C": "-.-.",
                   "D": "-..",
                   "E": ".",
                   "F": "..-.",
                   "G": "--.",
                   "H": "....",
                   "I": "..",
                   "J": ".---",
                   "K": "-.-",
                   "L": ".-..",
                   "M": "--",
                   "N": "-.",
                   "O": "---",
                   "P": ".--.",
                   "Q": "--.-",
                   "R": ".-.",
                   "S": "...",
                   "T": "-",
                   "U": "..-",
                   "V": "...-",
                   "W": ".--",
                   "X": "-..-",
                   "Y": "-.--",
                   "Z": "--..",
                   "1": ".----",
                   "2": "..---",
                   "3": "...--",
                   "4": "....-",
                   "5": ".....",
                   "6": "-....",
                   "7": "--...",
                   "8": "---..",
                   "9": "----.",
                   "0": "-----",
                   " ": " "
                   }
    leet_codes = {"A": "4",
                  "B": "8",
                  "C": "(",
                  "D": "|)",
                  "E": "3",
                  "F": "PH",
                  "G": "6",
                  "H": "|-|",
                  "I": "!",
                  "J": "_|",
                  "K": "X",
                  "L": "1",
                  "M": "/\\/\\",
                  "N": "|\\|",
                  "O": "0",
                  "P": "|*",
                  "Q": "0_",
                  "R": "|2",
                  "S": "5",
                  "T": "7",
                  "U": "|_|",
                  "V": "\\/",
                  "W": "\\/\\/",
                  "X": "%",
                  "Y": "j",
                  "Z": "2",
                  " ": " "
                  }