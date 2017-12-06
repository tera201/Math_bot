import simple_arithmetic
import test3
#import pascal
import binom

class Big_father():
    def __init__(self,string):
        self.string=string
        self.string = simple_arithmetic.Arithmetic(self.string).remake()
    def __str__(self):
        if self.string[0:2]=='y=':
            if test3.Grafics(self.string[2:]).constructor():
                return "bot.send_message(message.chat.id,'ты даже функцию без ошибок записать не можешь...')"
            else:
                return "bot.send_photo(message.chat.id," + "open('pic.png', 'rb')" + ")"

      #  elif self.string[0:7]=='pascal(':
       #     print(self.string[7:-1])
        #    self.string = pascal.Triangle(self.string[7:-1]).TP()
         #   return "bot.send_message(message.chat.id,'" + str(self.string) + "')"

        elif self.string[0:6]=='binom(':
            self.string = binom.nuiton(self.string[5:]).main()
            return "bot.send_message(message.chat.id,'" + str(self.string) + "')"


        else:
            self.string=simple_arithmetic.Arithmetic(self.string).arithmetic()
            return "bot.send_message(message.chat.id,'"+ str(self.string) + "')"

