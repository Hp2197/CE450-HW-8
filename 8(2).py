#1
class Twice(People):
    def __init__(self, name):
        People.__init__(self, name)
    def say(self, sth):
        return People.say(self, sth) + " " + self.reiterate()

        # gives the recurssion error

#2
class Twice(People):
    def __init__(self, name):
        People.__init__(self, name)
    def say(self, sth):
            return sth + " " + sth

 # it work but it didn't respond in the way we want to respond

 #3
 class Twice(People):
    def __init__(self, name):
        People.__init__(self, name)
    def say(self, sth):
        return People.say(self, sth + " " + sth)

#This one work in the way which we want to work with reiterate method 
