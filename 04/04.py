Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Dimension:
    def_int_(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        pass
class Ellipse(Dimension):
     def_init_(self,a,b):
      Dimension._init_(self,a,b)
      def area(self):
           return 3.14*a*b
class Square( Dimension):
    def_init_(self,c):
         Dimension._init_(self,c)
         def area(self):
         return c*c  
class Rectangle(Dimension):
    def_init_(self,w,h):
        Dimension._init_(self,w,h)
        def area(self):
            return self.x*self.y
class Circle(Dimension):
     def_init_(self,r):
         Dimension._init_(self,r,0)
         def area(self):
             return 3.14*self.x*self.y
d1= Ellipse(10,20)
d2=Square(15.0)
d4=Rectangle(10.0,4.0)
d3=Circle(5.0)
total_area=computer_area(shapes)
print(total_area)
SyntaxError: invalid syntax
>>> 
