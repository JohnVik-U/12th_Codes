n = int(input())
if n%2 == 0:
    if n>2 and n<5:
        print('Not Nice')
    elif n>6 and n<20:
        print('Nice')
    else:
        print('Not Nice')
else:
    print('Nice')