class Keypad():
  def __init__(self, *args):
    self.buttons = {}
    for ar in args:
      self.buttons[ar.pos] = ar

  def press(self, info):
    try:
      self.buttons[info].pressed += 1
      return self.buttons[info].key
    except:
      print('Dude!, Button doesnt exist')
      pass
  def type(self, type_ip):
    try:
      res = ""
      for i in type_ip:
        self.buttons[i].pressed += 1
        res += self.buttons[i].key
      return res
    except:
      print('Button doesnt exist')
      pass
class Button(): # Button class
  def __init__(self, pstn, ky):
    self.pos = pstn
    self.key = ky
    self.pressed = 0