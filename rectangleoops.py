#!/usr/bin/python
# -*- coding: utf-8 -*-


class Rectangle:

    def CalculateArea(self):
        print 'enter width'
        print 'enter breath'

        self.s = float(input())
        self.r = float(input())
        area = self.s * self.r
        return area

    def CalculatePerimeter(self):
        perimeter = 2 * (self.s + self.r)
        return perimeter


c = Rectangle()
x = c.CalculateArea()
y = c.CalculatePerimeter()
print 'AREA OF A rectangle IS =%f' % x
print 'perimeter rectangle IS =%f' % y
class Rectangle:
     def CalculateArea(self):
          print("enter width")
          print("enter breath")
          
          self.s=float(input())
          self.r=float(input())
          area=self.s*self.r
          return(area)
     def CalculatePerimeter(self):
          perimeter=2*(self.s+self.r)
          return(perimeter)
c=Rectangle()
x=c.CalculateArea()
y=c.CalculatePerimeter()
print("AREA OF A rectangle IS =%f"%(x))
print("perimeter rectangle IS =%f"%(y))

                 
     
