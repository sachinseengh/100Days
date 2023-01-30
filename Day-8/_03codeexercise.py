height=int(input("Enter the height of wall\n"))
weight=int(input("Enter the width of wall\n"))

def cancalc(h,w):
    area=h*w
    totalcan=round(area/5)
    print(f"you should buy {totalcan} can ")
cancalc(height,weight)