import random
import string
import atexit

class generator:
    def __init__(self):
        self.lowercase_list = string.ascii_lowercase
        self.uppercase_list = string.ascii_uppercase
        self.digit_list = string.digits
        self.special_char_list = string.punctuation

        self.pw_len = int(input("Enter lenght of the PW: "))
        self.functions = [self.lower, self.upper, self.digits, self.spec_char]
        self.case_list = []
    
    def lower(self):
        self.lowercase = random.choice(self.lowercase_list)
        return self.lowercase

    def upper(self):
        self.uppercase = random.choice(self.uppercase_list)
        return self.uppercase

    def digits(self):
        self.digit = random.choice(self.digit_list)
        return self.digit
    
    def spec_char(self):
        self.spec = random.choice(self.special_char_list)
        return self.spec

    def give(self):
        for i in range(0, self.pw_len):
            case = str(random.choice(self.functions)())
            self.case_list.append(case)
        print(''.join(self.case_list))
    
    def exit_handler(self):
        input("Drücke Enter, um das Fenster zu schließen.")

gen = generator()

if __name__ == '__main__':
    atexit.register(gen.exit_handler)
    gen.give()