import random as r
# MADE BY ZI TIAN / TORONO909
# FEEL FREE TO USE


class Game:
    def game(self):
        pin = str(r.randint(1000, 9999))
        var = input('Four digit pin: ')
        self.check(var, pin, 4, 4)
    def check(self, var1, var2, length, tries):
        if var1 == var2 and len(var1) == length:
            print('Correct!')
        elif var1 != var2 and len(var1) == length and tries > 0:
            print('Wrong! Try again.')
            self.game()
        elif var1 != var2 and len(var1) == length and tries == 0:
            varr = input('Wrong! Try again? (Y/N):')
            if varr == 'Y' or varr == 'y':
                self.game()
            else:
                exit()
               
# Initialize the class 'Game'
a = Game()
a.game()
