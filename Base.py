import time
import random
import board
import adafruit_dotstar as dotstar

# Function of script

Animation = 3
# 1 R B bank wave 
# 2 Solid Color
# 3 Static Color PerBank
# 4 Full Ranbow
dots_len = 42
dots_lum = 0.2


Animation_2_Values = [ 200, 0, 100]
#                       R   G   B
#Animation_3_Values = [ 200, 0, 100, 100, 0, 200, 200, 0, 100]
Animation_3_Values = [ 200, 0, 0, 0, 200, 0, 0, 0,        print("true") 200]
#            Top      R   G   B    Middle R   G  B   Bottom    



# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
dots = dotstar.DotStar(board.SCK, board.MOSI, dots_len, brightness=dots_lum, auto_write=False)










# Left side
bank_A_Start = 0
bank_A_End = 21

#Left Top Side
bank_a_subBank1_Start = bank_A_Start
bank_a_subBank1_End =   7
#Left Middle
bank_a_subBank2_Start = 7
bank_a_subBank2_End =   14
#Left Bottom
bank_a_subBank3_Start = 14
bank_a_subBank3_End =   bank_A_End 

# Right side
bank_B_start = 21
bank_B_End = 42
#Right Top
bank_b_subBank1_Start = 35
bank_b_subBank1_End =   bank_B_End 
#Right Middle
bank_b_subBank2_Start = 28
bank_b_subBank2_End =   35
#Right Bottom
bank_b_subBank3_Start = bank_B_start
bank_b_subBank3_End =   28

# HELPERS
# a random color 0 -> 240
def random_color():
    return random.randrange(0, 60) * 4
#           15-> 210
def random_color_limited():
    return random.randrange(1, 14) * 15

def random_percent():
    return (random.randrange(0, 100) /100)

def random_percent_limits(low = 0,high = 100):
    return (random.randrange(low, high) /100)

def signFlip():
    Output = random.randrange(-1, 2)
    if Output == 0 :
        Output = 1
    return Output

def limit_check(ColorValue=250):
    if ColorValue > 240:
        return False
    else :
        return True

def color_modifi(colorValue=100, Shift_Limit=20):
    Shift = random.randrange(1,Shift_Limit)
    if  limit_check ( ( colorValue + Shift) ) == True :
        Shift = Shift * signFlip()   
        colorValue = abs ( colorValue + Shift)
    else :
        colorValue = abs ( colorValue - Shift)
    return colorValue
    



if Animation == 1 :
    
    # Baseline Color values
    R = random_color()
    B = random_color() 
    G = 0
    L = random_percent_limits(10,int(dots_lum*100))
    while True:

        R = color_modifi(R, 50)
        B = color_modifi(B, 50)
        # Top row Left
        for dot in range(bank_a_subBank1_Start,bank_a_subBank1_End):
            dots[dot] = (R , G, B, L)
        # Sub bank other side     
        for dot in range(bank_b_subBank1_Start,bank_b_subBank1_End):
            dots[dot] = (R , G, B, L)

        #Change values for Middle Bank
        R = color_modifi(R, 30)
        B = color_modifi(B, 30)

        for dot in range(bank_a_subBank2_Start,bank_a_subBank2_End):
            dots[dot] = (R , G, B, L)
        # Sub bank other side     
        for dot in range(bank_b_subBank2_Start,bank_b_subBank2_End):
            dots[dot] = (R , G, B, L)

        R = color_modifi(R, 20)
        B = color_modifi(B, 20)
        # Bottom Bank
        for dot in range(bank_a_subBank3_Start,bank_a_subBank3_End):
            dots[dot] = (R , G, B, L)
        # Sub bank other side     
        for dot in range(bank_b_subBank3_Start,bank_b_subBank3_End):
            dots[dot] = (R , G, B, L)

        dots.show()
        time.sleep(0.06)

if Animation == 2 :
    # Top row Left
    for dot in range(bank_A_Start,bank_B_End):
        dots[dot] = (Animation_2_Values[0], Animation_2_Values[1], Animation_2_Values[2])
    dots.show()

if Animation == 3 :
    # Top row Left
    for dot in range(bank_a_subBank1_Start,bank_a_subBank1_End):
        dots[dot] = (Animation_3_Values[0] , Animation_3_Values[1], Animation_3_Values[2])
    # Sub bank other side     
    for dot in range(bank_b_subBank1_Start,bank_b_subBank1_End):
        dots[dot] = (Animation_3_Values[0] , Animation_3_Values[1], Animation_3_Values[2])

    for dot in range(bank_a_subBank2_Start,bank_a_subBank2_End):
        dots[dot] = (Animation_3_Values[3] , Animation_3_Values[4], Animation_3_Values[5])
        # Sub bank other side     
    for dot in range(bank_b_subBank2_Start,bank_b_subBank2_End):
        dots[dot] = (Animation_3_Values[3] , Animation_3_Values[4], Animation_3_Values[5])

        # Bottom Bank
    for dot in range(bank_a_subBank3_Start,bank_a_subBank3_End):
        dots[dot] = (Animation_3_Values[6] , Animation_3_Values[7], Animation_3_Values[8])
        # Sub bank other side     
    for dot in range(bank_b_subBank3_Start,bank_b_subBank3_End):
        dots[dot] = (Animation_3_Values[6] , Animation_3_Values[7], Animation_3_Values[8])
    dots.show()

if Animation == 4 :
    
    # Baseline Color values
    R = random_color()
    B = random_color() 
    G = random_color()
    L = random_percent_limits(10,int(dots_lum*100))
    while True:
        
        R = color_modifi(R, 30)
        B = color_modifi(B, 30)
        G = color_modifi(G, 30)
        # Top row Left
        for dot in range(bank_a_subBank1_Start,bank_a_subBank1_End):
            dots[dot] = (R , G, B, L)
        # Sub bank other side     
        for dot in range(bank_b_subBank1_Start,bank_b_subBank1_End):
            dots[dot] = (R , G, B, L)

        #Change values for Middle Bank
        R = color_modifi(R, 30)
        B = color_modifi(B, 30)
        G = color_modifi(G, 30)

        for dot in range(bank_a_subBank2_Start,bank_a_subBank2_End):
            dots[dot] = (R , G, B, L)
        # Sub bank other side     
        for dot in range(bank_b_subBank2_Start,bank_b_subBank2_End):
            dots[dot] = (R , G, B, L)

        R = color_modifi(R, 30)
        B = color_modifi(B, 30)
        G = color_modifi(G, 30)
        # Bottom Bank
        for dot in range(bank_a_subBank3_Start,bank_a_subBank3_End):
            dots[dot] = (R , G, B, L)
        # Sub bank other side     
        for dot in range(bank_b_subBank3_Start,bank_b_subBank3_End):
            dots[dot] = (R , G, B, L)

        dots.show()
        time.sleep(0.06)


if Animation == 5 :
    
    # Baseline Color values
    R = random_color()
    B = random_color() 
    G = 0
    while True:

        R = color_modifi(R, 50)
        B = color_modifi(B, 50)
        # Top row Left
        for dot in range(bank_a_subBank1_Start,bank_a_subBank1_End):
            dots[dot] = (R , G, B)
        # Sub bank other side     
        for dot in range(bank_b_subBank1_Start,bank_b_subBank1_End):
            dots[dot] = (R , G, B)

        #Change values for Middle Bank
        R = color_modifi(R, 30)
        B = color_modifi(B, 30)

        for dot in range(bank_a_subBank2_Start,bank_a_subBank2_End):
            dots[dot] = (R , G, B)
        # Sub bank other side     
        for dot in range(bank_b_subBank2_Start,bank_b_subBank2_End):
            dots[dot] = (R , G, B)

        R = color_modifi(R, 20)
        B = color_modifi(B, 20)
        # Bottom Bank
        for dot in range(bank_a_subBank3_Start,bank_a_subBank3_End):
            dots[dot] = (R , G, B)
        # Sub bank other side     
        for dot in range(bank_b_subBank3_Start,bank_b_subBank3_End):
            dots[dot] = (R , G, B)

        dots.show()
        time.sleep(0.06)