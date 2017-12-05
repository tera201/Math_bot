import simple_arithmetic
#import test3
import pascal
class Big_father():
    def __init__(self,string):
        self.string=string
        self.string = simple_arithmetic.Arithmetic(self.string).remake()
    def grafic(self):
        if self.string[0:2]=='y=':
            if True:#test3.Grafics(self.string[2:]).constructor():
                return "bot.send_message(message.chat.id,'ты даже функцию без ошибок записать не можешь...')"
            else:
                return "bot.send_photo(message.chat.id," + "open('pic.png', 'rb')" + ")"

        elif self.string[0:7]=='pascal(':
            print(self.string[7:-1])
            self.string = pascal.Triangle(self.string[7:-1]).TP()
            return "bot.send_message(message.chat.id,'" + str(self.string) + "')"


        else:
            #print(self.string[5:-1])
            self.string=simple_arithmetic.Arithmetic(self.string).arithmetic()
            return "bot.send_message(message.chat.id,'"+ str(self.string) + "')"

