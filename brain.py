import remain
import test3
#import pascal
import binom

class Big_father():
    def __init__(self,string):
        self.string=string
        self.string = remain.Arithmetic(self.string).remake_in()
    def __str__(self):

        if self.string[0:2]=='y=':
            if test3.Grafics(self.string[2:]).constructor():
                return "bot.send_message(message.chat.id,'ты даже функцию без ошибок записать не можешь...')"
            else:
                return "bot.send_photo(message.chat.id,open('pic.png', 'rb'))"

      #  elif self.string[0:7]=='pascal(':
       #     print(self.string[7:-1])
        #    self.string = pascal.Triangle(self.string[7:-1]).TP()
         #   return "bot.send_message(message.chat.id,'" + str(self.string) + "')"

        elif self.string[0:6]=='binom(':
            self.string = binom.nuiton(self.string[5:]).main()
            return "bot.send_message(message.chat.id,'{}')".format(self.string)


        else:
            self.string=remain.Arithmetic(self.string).arithmetic()
            return "bot.send_message(message.chat.id,'{}')".format(self.string)
        print(len(str(self.string)))

