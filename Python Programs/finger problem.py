N=int(input())
if N%8==1:
    print(N , "ends in the finger 1")
elif N%4==2 or N%8==0:
     print(N , "ends in the finger 2")
elif N%4==3:
     print(N , "ends in the finger 3")
elif N%4==0 or N%4==2:
     print(N , "ends in the finger 4")
elif N%4==1:
     print(N , "ends in the finger 5")