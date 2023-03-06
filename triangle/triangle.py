def equilateral(sides):
    a = sides[0] 
    b = sides[1]
    c = sides[2]
    
    
    while a + b >= c and b + c >= a and a + c >= b:
        if sum(sides) == 0:
            return False
        elif a == b and b == c and c == a:
            return True
        else:
            return False
    return False
    

def isosceles(sides):
    a = sides[0] 
    b = sides[1]
    c = sides[2]


    while a + b >= c and b + c >= a and a + c >= b:
        if sum(sides) == 0:
            return False
        elif (a==b) or (b==c) or (c==a):
            return True
        
        else:
            return False
        
    return False

def scalene(sides):
    a = sides[0] 
    b = sides[1]
    c = sides[2]


    while a + b >= c and b + c >= a and a + c >= b:
        if sum(sides) == 0:
            return False
        elif (a==b) or (b==c) or (c==a):
            return False
        
        else:
            return True
        
    return False


