from types import ClassMethodDescriptorType


class Colors:
  grey = (28,28,28)
  lColor = (255,127,0)
  iColor = (0,255,255)
  jColor = (0,0,255)
  oColor = (255,255,0)
  sColor = (255,58,58)
  tColor = (170,0,170)
  zColor = (0,255,0)
  lg = (127, 127, 127)
  l = (155,80,0)
  i = (0,155,155)
  j = (0,0,180)
  o = (155,155,0)
  s = (100,0,0)
  t = (120,0,120)
  z = (0,120,0)


  #dont have to make an instance of the class
  @classmethod
  def get_color(cls):
    return [cls.grey, cls.lColor, cls.iColor,  cls.jColor, cls.oColor, cls.sColor, cls.tColor, cls.zColor]

  @classmethod
  def get_border(cls):
    return [cls.lg, cls.l, cls.i, cls.j, cls.o, cls.s, cls.t, cls.z]