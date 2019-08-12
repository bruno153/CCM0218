
# coding: utf-8

# In[2]:

import math
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

def trig(angle, select):
    i = 0
    cosMult = 1
    
    if angle > math.pi / 2:
        if select == 2:
            return trig(angle - math.pi, select)
        return -trig(angle - math.pi, select)
    elif angle < -math.pi / 2:
        if select == 2:
            return trig(angle + math.pi, select)
        return -trig(angle + math.pi, select)
    
    
    angleLibrary = [0.78539816339745, 0.46364760900081, 0.24497866312686, 0.12435499454676,
                    0.06241880999596, 0.03123983343027, 0.01562372862048, 0.00781234106010,
                    0.00390623013197, 0.00195312251648, 0.00097656218956, 0.00048828121119,
                    0.00024414062015, 0.00012207031189, 0.00006103515617, 0.00003051757812,
                    0.00001525878906, 0.00000762939453, 0.00000381469727, 0.00000190734863,
                    0.00000095367432, 0.00000047683716, 0.00000023841858, 0.00000011920929,
                    0.00000005960464, 0.00000002980232, 0.00000001490116, 0.00000000745058,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0]
    '''angleLibrary = [0.785398163397,    0.392699081699,    0.196349540849,    0.0981747704247, 
                    0.0490873852123,   0.0245436926062,   0.0122718463031,   0.00613592315154, 
                    0.00306796157577,  0.00153398078789,  0.000766990393943, 0.000383495196971, 
                    0.000191747598486, 9.58737992429e-05, 4.79368996214e-05, 2.39684498107e-05, 
                    1.19842249054e-05, 5.99211245268e-06, 2.99605622634e-06, 1.49802811317e-06, 
                    7.49014056585e-07, 3.74507028292e-07, 1.87253514146e-07, 9.36267570731e-08, 
                    4.68133785365e-08, 2.34066892683e-08, 1.17033446341e-08, 5.85167231707e-09, 
                    2.92583615853e-09, 1.46291807927e-09, 7.31459039634e-10, 3.65729519817e-10, 
                    1.82864759908e-10, 9.14323799542e-11, 4.57161899771e-11, 2.28580949885e-11, 
                    1.14290474943e-11, 5.71452374714e-12, 2.85726187357e-12, 1.42863093678e-12]'''
    power = 1/4.0
    tmpAngle = 0.0
    exp = range(0,40)
    for i in range(0, 40): #angle finder
        if i >= 23:
            angleLibrary[i] = power
        if tmpAngle < angle: #positive rotation
            exp[i] = 1
            tmpAngle += angleLibrary[i]
            
        elif tmpAngle >= angle: #negative rotation
            exp[i] = -1
            tmpAngle -= angleLibrary[i]
            
        power = power/2.0
    sin = 0
    cos = 1
    c = 1
    for i in range(0, 40): #angle rotations
        sinnew = sin + (cos * c * exp[i])
        cosnew = cos - (sin * c * exp[i])
        sin = sinnew
        cos = cosnew
        c = c/2.0
    
    
    sin = sin * 0.607252935
    cos = cos * 0.607252935
    
    if select == 0:
        return sin
    if select == 1:
        return cos
    if select == 2:
        return sin/cos
    
    return

def sin(angle):
    return round(trig(angle, 0), 5)

def cos(angle):
    return round(trig(angle, 1), 5)

def tan(angle):
    return round(trig(angle, 2), 5)

def sec(angle):
    if trig(angle, 0) == 0: #div by zero exception
        return 
    return round(1/trig(angle, 0), 5)

def csc(angle):
    if trig(angle, 1) == 0: #div by zero exception
        return 
    return round(1/trig(angle, 1), 5)

def cot(angle):
    if trig(angle, 2) == 0: #div by zero exception
        return 
    return round(1/trig(angle, 2), 5)


# In[3]:

def showme(angle):
    print "ANGLE =",angle, "rad"
    print "sine = ", sin(angle)
    print "cosine = ", cos(angle)
    print "tangent = ", tan(angle)
    print "secant = ", sec(angle)
    print "cosecant = ", csc(angle)
    print "cotangent = ", cot(angle)


# In[ ]:



