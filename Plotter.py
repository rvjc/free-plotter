#############################################################
#
# Plotter 1.0 Copyright (C) RVJ Callanan 2012
#
# This is FREE software, licensed under the GNU GPLv3
# See: <http://www.gnu.org/licenses/>.
#
#############################################################

#############################################################
# IMPORTS
#############################################################

from turtle import *
from math import *

#############################################################
# GLOBAL CONSTANTS
#############################################################

# Turtle Coordinates

TXMIN = -200
TXMAX = +200
TYMIN = -200
TYMAX = +200

TXUNITS = 40
TYUNITS = 40

TXLEN = TXMAX - TXMIN
TYLEN = TYMAX - TYMIN

# Graph Coordinate Defaults

DEFAULT_GXUNITS  = 1.0
DEFAULT_GYUNITS  = 1.0
DEFAULT_GXCENTER = 0.0
DEFAULT_GYCENTER = 0.0

# Grid 

GRIDX = TXLEN/TXUNITS
GRIDY = TYLEN/TYUNITS

# Function settings

MAX_FUNCTIONS    = 3
FUNCTION_COLORS  = "red", "blue", "forestgreen"

#############################################################
# GLOBAL VARIABLES
#############################################################

# Main settings

functions = None    # array of functions to plot

gxunits  = None     # grid units used on X axis
gyunits  = None     # grid units used on Y axis
gxcenter = None     # X coordinate at screen center
gycenter = None     # Y coordinate at screen center

# Derived settings

gxdp = None         # X axis decimal places
gydp = None         # Y axis decimal places

gxlen = None        # total span of X axis
gylen = None        # total span of Y axis

gxmin = None        # left-most X coordinate
gxmax = None        # right-most X coordinate
gymin = None        # bottom-most Y coordinate
gymax = None        # top-most Y coordinate

#############################################################
# FUNCTIONS
#############################################################

def GetSettings():

    global functions, gxunits, gyunits, gxcenter, gycenter

    a = input("Choose Sample(S) or Custom(C) Settings (default = C): ")

    print()
    
    if a == 's' or a == 'S':
        GetSampleSettings()
    else:
        GetCustomSettings()

#############################################################

def GetSampleSettings():

    print("SAMPLE FUNCTIONS")
    print()
    print("1. Linear")
    print("2. Quadratic")
    print("3. Cubic ")
    print("4. Reciprocal")
    print("5. Sin, Cos and Tan")
    print("6. Square Wave with 2 Frequencies")
    print("7. Square Wave with 3 Frequencies")
    print("8. Square Wave with 4 Frequencies")
    print("9. Square Wave with 5 Frequencies")
    print()

    a = input("Select Sample (default = 1): ")

    if a == '1':
        SampleSettings1()
    if a == '2':
        SampleSettings2()
    elif a == '3':
        SampleSettings3()
    elif a == '4':
        SampleSettings4()
    elif a == '5':
        SampleSettings5()
    elif a == '6':
        SampleSettings6()
    elif a == '7':
        SampleSettings7()
    elif a == '8':
        SampleSettings8()
    elif a == '9':
        SampleSettings9()
    else:
        SampleSettings1()

    print()

#############################################################

def SampleSettings1():

    global functions, gxunits, gyunits, gxcenter, gycenter

    functions =  "3", \
                 "x", \
                 "-x"

    gxunits  = 1.0
    gyunits  = 1.0
    gxcenter = 0.0
    gycenter = 0.0

#############################################################

def SampleSettings2():

    global functions, gxunits, gyunits, gxcenter, gycenter

    functions = "pow(x,2) - 2*x - 1", \
                "-pow(x,2) + 2*x + 1"
               
    gxunits  = 1.0
    gyunits  = 5.0
    gxcenter = 1.0
    gycenter = 1.0

#############################################################

def SampleSettings3():

    global functions, gxunits, gyunits, gxcenter, gycenter

    functions = "pow(x,3) - 2*pow(x,2) - 2*x + 1", \
                "-pow(x,3) + 2*pow(x,2) + 2*x - 1"

    gxunits  = 0.65
    gyunits  = 5.0
    gxcenter = 0.65
    gycenter = 0.0

#############################################################

def SampleSettings4():

    global functions, gxunits, gyunits, gxcenter, gycenter

    functions = "1/x",

    gxunits  = 1.0
    gyunits  = 2.0
    gxcenter = 0.0
    gycenter = 0.0

#############################################################

def SampleSettings5():

    global functions, gxunits, gyunits, gxcenter, gycenter

    functions =  "sin(x)", \
                 "cos(x)", \
                 "tan(x)"

    gxunits  = 1.0
    gyunits  = 1.0
    gxcenter = 0.0
    gycenter = 0.0

#############################################################

def SampleSettings6():

    global functions, gxunits, gyunits, gxcenter, gycenter

    functions =  "sin(2*x) + sin(6*x)/3",

    gxunits  = 0.5
    gyunits  = 0.2
    gxcenter = 0.0
    gycenter = 0.0

#############################################################

def SampleSettings7():

    global functions, gxunits, gyunits, gxcenter, gycenter

    functions =  "sin(2*x) + sin(6*x)/3 + sin(10*x)/5",

    gxunits  = 0.5
    gyunits  = 0.2
    gxcenter = 0.0
    gycenter = 0.0

#############################################################

def SampleSettings8():

    global functions, gxunits, gyunits, gxcenter, gycenter

    functions =  "sin(2*x) + sin(6*x)/3 + sin(10*x)/5 + sin(14*x)/7",

    gxunits  = 0.5
    gyunits  = 0.2
    gxcenter = 0.0
    gycenter = 0.0

#############################################################

def SampleSettings9():

    global functions, gxunits, gyunits, gxcenter, gycenter

    functions =  "sin(2*x) + sin(6*x)/3 + sin(10*x)/5 + sin(14*x)/7 + sin(18*x)/9",

    gxunits  = 0.5
    gyunits  = 0.2
    gxcenter = 0.0
    gycenter = 0.0
    
#############################################################

def GetCustomSettings():

    global functions, gxunits, gyunits, gxcenter, gycenter

    print("CUSTOM SETTINGS")

    print()
    print("Note: Settings may be adjusted to fit graph constraints.")
    print()
   
    functions = GetFunctions()

    print()

    gxunits = GetFloat("Grid X Units", DEFAULT_GXUNITS)
    gyunits = GetFloat("Grid Y Units", DEFAULT_GYUNITS)
    
    gxcenter = GetFloat("Grid Center X", DEFAULT_GXCENTER)
    gycenter = GetFloat("Grid Center Y", DEFAULT_GYCENTER)

    print()

#############################################################

def GetFunctions():

    f = []
    
    i = 1

    while i <= MAX_FUNCTIONS:
        
        a = input("Function No. " + str(i) + ": ")
        
        if a == "":
            
            if i == 1:
                print("At least one function is required!")
                continue
            else:
                break

        else:
            
            f.append(a)

        i = i + 1
        
    return f

#############################################################

def GetFloat(description,default):

    while True:

        a = input(description + " (default = " + str(default) + "): ")
                      
        if a == "":
            f = default
        else:
            try:
                f = float(a)
            except:
                print("Invalid, try again!")
                continue

        break

    return f

#############################################################

def ProcessSettings():

    # Processes main settings and calculates derived settings

    global gxunits, gyunits, gxcenter, gycenter
    global gxdp, gydp, gxlen, gylen, gxmin, gxmax, gymin, gymax

    gxunits, gxcenter, gxdp = Normalise(gxunits, gxcenter)
    gyunits, gycenter, gydp = Normalise(gyunits, gycenter)
 
    gxlen = GRIDX * gxunits
    gylen = GRIDY * gyunits

    gxmin = gxcenter - gxlen/2
    gxmax = gxcenter + gxlen/2
    gymin = gycenter - gylen/2
    gymax = gycenter + gylen/2

#############################################################

def Normalise(ru, rc):

    # Normalises the raw grid units and center parameters.
    # Grid units need to be represented in the most compact
    # decimal form that meets the required precision. The
    # center must then be an exact multiple of the normalised
    # units. Also returns the number of decimal places used.
    # Negative decimal places imply that rounding has been
    # performed to the left of the decimal point.

    PRECISION = 0.01

    dp = -floor(log10(ru))

    while True:
        nu = round(ru,dp)
        if abs((nu-ru)/ru) <= PRECISION:
            break
        dp = dp + 1

    nc = round(rc/nu)*nu
        
    return nu, nc, dp
 
#############################################################

def InitTurtle():
    
    setup (width=600, height=600)
    mode("logo")
    speed("fastest")
    ht()
    seth(90)
    listen()

#############################################################

def ExitTurtle():

    bye()

#############################################################

def EvalY(x,fx):

    # Evaluates Y for the specified function in terms of X.
    # The function string is supplied by the user and has to
    # be evaluated using the special Python eval function which
    # executes a string as if it were part of a normal program.
    # It is possible that the user may supply invalid syntax or
    # cause a run-time error (e.g. divide-by-zero). Therefore
    # function errors are trapped and a value of None returned.

    try:
        y = eval(fx)
        
    except:
        y = None
        
    return y

#############################################################

def Convert(ival,imin,ilen,omin,olen):

    # Converts input value to equivalent output value based on
    # min and len settings for input and output domains.
    # This generic function is x,y and domain agnostic. It is
    # a worker function used by Gx(), Gy(), Tx() and Ty().

    return omin + (ival - imin) * olen/ilen

#############################################################

def Gx(tx):

    # Returns graph equivalent of supplied turtle X coordinate

    return Convert(tx, TXMIN, TXLEN, gxmin, gxlen)

#############################################################

def Gy(ty):

    # Returns graph equivalent of supplied turtle Y coordinate

    return Convert(ty, TYMIN, TYLEN, gymin, gylen)

#############################################################

def Tx(gx):

    # Returns turtle equivalent of supplied graph X coordinate

    return Convert(gx, gxmin, gxlen, TXMIN, TXLEN)

#############################################################

def Ty(gy):

    # Returns turtle equivalent of supplied graph Y coordinate
    # Since gy is produced by a user-defined function, we must
    # cater for an illegal value. The protocol is to use None
    # to indicate illegal values in both gy and ty domains.

    if gy == None:
        ty = None
    else:
        ty = Convert(gy, gymin, gylen, TYMIN, TYLEN)    

    return ty

#############################################################

def FmtDp(v,dp):

    # Formats value with supplied number of decimal places

    if dp < 0:
        dp = 0        

    return format(v, " ." + str(dp) + "f")
    
#############################################################

def DrawLine(tx1,ty1,tx2,ty2):
    
    pu()
    goto(tx1, ty1)
    pd()
    goto(tx2, ty2)
    pu()

################################################

def DrawText(tx,ty,txt,align, font=("Arial", 8, "normal")):
  
    pu()
    goto(tx,ty-6)
    write(txt, False, align, font)

#############################################################

def DrawGrid():

    # Draws grid lines and units

    color("lightgrey")

    # Vertical grid lines

    for tx in range(TXMIN, TXMAX+1, TXUNITS):
        
        gx = Gx(tx)
        gxf = FmtDp(gx,gxdp)
        
        if abs(gx/gxunits) < 0.5:
            color("black")
        else:
            color("lightgrey")

        DrawLine(tx, TYMIN, tx, TYMAX)

        color("black")
        DrawText(tx, TYMIN-15, gxf, "center")
        DrawText(tx, TYMAX+15, gxf, "center")

    # Horizontal grid lines
        
    for ty in range(TYMIN, TYMAX+1, TYUNITS):
        
        gy = Gy(ty)
        gyf = FmtDp(gy,gydp)

        if abs(gy/gyunits) < 0.5:
            color("black")
        else:
            color("lightgrey")

        DrawLine(TXMIN, ty, TXMAX, ty)

        color("black")  
        DrawText(TXMIN-15, ty, gyf, "right")
        DrawText(TXMAX+15, ty, gyf, "left")

#############################################################

def DrawEquation(fx,c,tx,ty):

    # Draws function equation in specified color left-aligned
    # at specified turtle coordinates

    color(c)
    DrawText(tx, ty, "y = " + fx, "left")

#############################################################

def DrawAllEquations():

    # Draws all function equations in different colors

    tx = TXMIN
    ty = TYMAX + 70

    for i in range(len(functions)):

        fx = functions[i] 
        c = FUNCTION_COLORS[i]

        DrawEquation(fx,c,tx,ty)

        ty = ty - 15

#############################################################

def DrawGridSettings():

    # Draws all function equations in different colors

    color("black")

    units_text  = "Grid Units: " + FmtDp(gxunits,gxdp) + "  x " + FmtDp(gyunits,gydp)
    center_text = "Grid Center: " + "( " + FmtDp(gxcenter,gxdp) + " , " + FmtDp(gycenter,gydp) + " )"
    
    DrawText(TXMIN, TYMIN-50, units_text, "left")
    DrawText(TXMAX, TYMIN-50, center_text, "right")

#############################################################

def DrawFunction(fx,c):

    # Plots function using specified color
        
    color(c)

    # Always pen-up until we have moved
    # to the first/leftmost plot position       

    pu()
    
    # Now plot Y for each turtle X position

    p1ty = 0
    p2ty = 0

    for tx in range(TXMIN,TXMAX+1):

        # Calculate current gx an gy values

        gx = Gx(tx)
        gy = EvalY(gx,fx)
        
        # Calculate current Turtle Y value
      
        ty = Ty(gy)

        # We need to handle situations where
        # Turtle Y value is illegal (None) or
        # out-of-bounds. It is actually quite
        # complicated to cater for all equations.
        # The solution below gives a reasonable
        # graphical representation most of the
        # time and ensures that some value is
        # plotted even if it means clipping.

        if ty != None:
            if ty < TYMIN:
                ty = TYMIN
            elif ty > TYMAX:
                ty = TYMAX
        else:
            if p1ty == TYMIN:
                ty = TYMIN
            elif p1ty == TYMAX:
                ty = TYMAX
            elif p2ty > p1ty:
                ty = TYMAX
            elif p2ty < p1ty:
                ty = TYMIN
            elif p1ty > 0:
                ty = TYMAX
            elif p1ty < 0:
                ty = TYMIN
            else:
                ty = 0

        # Now move to next position
         
        goto(tx,ty)
        
        # Always pen-down after we have moved
        # to the first/leftmost plot position       

        if tx == TXMIN:
            pd()
       
        # Update previous turtle coordinates
         
        p2ty = p1ty
        p1ty = ty

#############################################################

def DrawAllFunctions():

    # Plots all user-supplied functions in different colors

    for i in range(len(functions)):

        fx = functions[i] 
        c = FUNCTION_COLORS[i]

        DrawFunction(fx,c)

#############################################################

def DrawDone():

    # Indciates that all graphs have been plotted

    color("Red")
    DrawText(0, TYMIN-50, "Done", "center")

#############################################################

def MainLoop():

    global functions, gxunits, gyunits, gxcenter, gycenter

    newplot = True

    while newplot:

        print()
        print("NEW PLOT")
        print()

        GetSettings()
        
        newplot = False
        curplot = True

        while curplot:

            ProcessSettings()

            print("Plot Started")

            InitTurtle()

            DrawGrid()
            DrawAllEquations()
            DrawGridSettings()
            DrawAllFunctions()
            DrawDone()
            done()

            ExitTurtle()

            print("Plot Completed")
            print()

            print("OPTIONS")
            print()
            print("Q  = Quit")
            print("N  = New Plot")
            print("L  = Pan Left")
            print("R  = Pan Right")
            print("U  = Pan Up")
            print("D  = Pan Down")
            print("I  = Zoom In")
            print("O  = Zoom Out")
            print("IH = Zoom In Horizontally")
            print("IV = Zoom In Vertically")
            print("OH = Zoom Out Horizontally")
            print("OV = Zoom Out Vertically")
            print()
            
            a = input("Choose Option (ENTER = Replot): ")

            if a == "Q" or a == "q":
                curplot = False
                
            elif a == "N" or a == "n":
                curplot = False
                newplot = True

            elif a == "L" or a == "l":
                gxcenter = gxcenter - gxunits

            elif a == "R" or a == "r":
                gxcenter = gxcenter + gxunits
            
            elif a == "U" or a == "u":
                gycenter = gycenter + gyunits

            elif a == "D" or a == "d":
                gycenter = gycenter - gyunits

            elif a == "I" or a == "i":
                gxunits = gxunits/2
                gyunits = gyunits/2
            
            elif a == "O" or a == "o":
                gxunits = gxunits*2
                gyunits = gyunits*2

            elif a == "IH" or a == "ih" or a == "Ih" or a == "iH":
                gxunits = gxunits/2

            elif a == "IV" or a == "iv" or a == "Iv" or a == "iV":
                gyunits = gyunits/2

            elif a == "OH" or a == "oh" or a == "Oh" or a == "oH":
                gxunits = gxunits*2

            elif a == "OV" or a == "ov" or a == "Ov" or a == "oV":
                gyunits = gyunits*2

#############################################################
# START OF PROGRAM
#############################################################

print("PLOTTER V1.0 by RVJ Callanan")
print("This is FREEE software released under the GPLv3")
MainLoop()
exit()

#############################################################
# END OF PROGRAM
#############################################################

