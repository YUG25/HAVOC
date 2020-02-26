#!/usr/bin/python
# -*- coding: utf-8 -*-


class Square:

    def CalculateArea(self):
        print 'enter side'
        self.s = float(input())
        area = self.s * self.s
        return area

    def CalculatePerimeter(self):
        perimeter = 4 * self.s
        return perimeter


c = Square()
x = c.CalculateArea()
y = c.CalculatePerimeter()
print 'AREA OF A SQAURE IS =%f' % x
print 'perimeter SQAURE IS =%f' % y
class Square:
     def CalculateArea(self):
          print("enter side")
          self.s=float(input())
          area=self.s*self.s
          return(area)
     def CalculatePerimeter(self):
          perimeter=4*self.s
          return(perimeter)
c=Square()
x=c.CalculateArea()
y=c.CalculatePerimeter()
print("AREA OF A SQAURE IS =%f"%(x))
print("perimeter SQAURE IS =%f"%(y))

                 
