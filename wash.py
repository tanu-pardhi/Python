w=float(input())
if w>0 and w<=2000:
    print("15 min")
elif w>2000 and w<=5000:
    print("30 min")
elif w>5000 and w<1000:
    print("45 min")
else:
    print("Overweight")