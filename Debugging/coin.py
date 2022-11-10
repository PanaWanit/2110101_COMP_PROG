# -*- coding: utf-8 -*-
import math

# find greatest common divisor
# of given inputs a and b
def gcd(a,b): 
  if(b==0 or a==0): 
    return a+b
  return gcd(b, a%b)


if __name__ == '__main__':
  # na : amount of coin_a
  # nb : amount of coin_b
  # find such a case that T = a*na + b*nb 
  # print na, nb if possible, else print IMPOSSIBLE

  print('Input: coin_a coin_b target_value')
  print('Input: ', end= '')
  a, b, T = [int(x) for x in input().split(' ')]

  if a==0 and b==0:
    print("IMPOSSIBLE")
    quit()
  # T cannot be composed by coin_a and coin_b 
  # if it cannot be divided by their greatest common divisor


  if(T % gcd(a, b) != 0):
    print("IMPOSSIBLE")
  

  else:
    ch=0
    na = 0  
    yes = False
    if b==0:
        a,b = b,a
        ch=1
    while(not yes and T-a*na>=0):
      if (T - a*na) % b == 0:
        nb = (T - a*na)//b
        yes = True
        break
      na += 1


  if(yes and ch==0):
    print(f"na: {na}, nb: {nb}")
  elif(yes and ch==1):
    print(f"na: {nb}, nb: {na}")
  else:
    print("IMPOSSIBLE")
