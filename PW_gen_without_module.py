import random
import atexit

class generator:
    def __init__(self):
        self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lower = "abcdefghijklmnopqrstuvwxyz"
        self.number = "123456789"
        self.spec_char = "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
        self.case = [self.upper, self.lower, self.number, self.spec_char]
        self.length = int(input("Enter lenght of the PW: "))
    
    def give(self):
        self.pw = []
        for i in range(0, self.length):
            rand = random.choice(random.choice(self.case))
            self.pw.append(rand)
        print("".join(self.pw))

    def exit_handler(self):
        input("Drücke Enter, um das Fenster zu schließen.")

gen = generator()

if __name__ == '__main__':
    atexit.register(gen.exit_handler)
    gen.give()