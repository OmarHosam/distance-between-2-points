from numpy import sqrt
def main():
    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    y1 = int(input("Enter y1: "))
    y2 = int(input("Enter y2: "))
    
    equation = ((x2-x1)**2)+((y2-y1)**2)
    print(f"Answer without square root(must square root): {equation}\nAfter square root: {sqrt(equation)}")
    print("Remember, The equation is √(x2-x1)²+(y2-y1)²")
    again()

def again():
    choice = input("Again? (y/n): ")
    if (choice.lower() == "y"):
        main()
    else:
        return
    
main()
input("Press any key to exit...")
