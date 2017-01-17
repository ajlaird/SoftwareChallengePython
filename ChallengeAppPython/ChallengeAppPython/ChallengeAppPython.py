import math 

choice = input("Enter measurement(Feet/Metres):")

if choice == 'Feet' or 'F':
    height = float(input("Enter height:  "))
    width1 = float(input("Enter first width:  "))
    width2 = float(input("Enter second width:  "))
    width3 = float(input("Enter third width:  "))
    width4 = float(input("Enter fourth width:  "))

    s = float (width1+ width2 + width3 + width4) / 2
    floorArea = float(math.sqrt((s - width1) * (s - width2) * (s - width3) * (s - width4)))
    wallArea = float((width1 + width2 + width3 + width4)*height)


    print ("Volume(Metres Cubed):", (floorArea * height) * 3.28)

    print("Area(Metres Squared): ", (floorArea * 3.28))

    print("Paint required(Litres): ", (wallArea * 0.1)*3.28)

if choice == 'Metres' or 'M':
    height = float(input("Enter height:  "))
    width1 = float(input("Enter first width:  "))
    width2 = float(input("Enter second width:  "))
    width3 = float(input("Enter third width:  "))
    width4 = float(input("Enter fourth width:  "))

    s = float (width1+ width2 + width3 + width4) / 2
    floorArea = float(math.sqrt((s - width1) * (s - width2) * (s - width3) * (s - width4)))
    wallArea = float((width1 + width2 + width3 + width4)*height)


    print ("Volume(Metres Cubed):", floorArea * height)

    print("Area(Metres Squared): ", floorArea)

    print("Paint required(Litres): ", wallArea * 0.1)
