from math import gcd

class RatNum:
  def __init__(self,num,den):
    self.num=num
    self.den=den
  
  def simp(self):
    if type(self.num) == RatNum:
      self = RatNum(self.num.num,self.num.num)/self
    if type(self.den) == RatNum:
      self = self/RatNum(self.den.den,self.den.den)
    div = gcd(self.num,self.den)
    self.num = self.num // div
    self.den = self.den // div
  
  def __add__(self, other):
    new_num = self.num*other.den
    new_den = self.den*other.den
    new_other_num = other.num*self.den
    result = RatNum(new_num+new_other_num*self.den,new_den)
    result.simp()
    return result
  
  def __sub__(self,other):
    other.num=other.num*-1
    return self+(other)
  
  def __mul__(self, other):
    result = RatNum((self.num*other.num),(self.den*other.den))
    return result
  
  def __truediv__(self,other):
    flother = RatNum(other.den,other.num)
    return self*flother
  
  def __float__(self):
    return(self.num/self.den)
  
  def __str__(self):
    return(str(self.num)+"/"+str(self.den))

def phi_calc(count):
  phi = RatNum(1,1)
  one = RatNum(1,1)
  phi_list = [1]
  for i in range(1,count):
    phi = one+one/phi
    phi_list.append(phi)
  return phi_list

def phi_chart(count):
  lst = phi_calc(count)
  for i in range(0,count):
    print("{}. {}".format(i+1,lst[i]))

def pi_calc(x):
  one=RatNum(1,1)
  a=one
  b=RatNum(4,1)
  pi=RatNum(1,1)
  two=RatNum(2,1)
  pi_list=[float(pi)]
  for i in range(x):
    eye=RatNum(i,1)
    pi=a+b/pi
    b=two*eye-one
    a=two
    pi_list.append(float(pi))
  return pi_list
print(pi_calc(20))