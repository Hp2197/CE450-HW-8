class People():
  def __init__(self, name):         
    self.name = name
    self.sth = "I am reading lecture handout!" 
  def say(self, sth):
    self.sth = sth   
    return sth 
  def ask(self, sth):         
    return self.say("Would you please " + sth) 
  def greet(self):         
    return self.say("Hi, this is " + self.name) 
  def reiterate(self):
    return self.say(self.sth)
  def ask(self, sth):
    return self.say("Would you please " + sth)