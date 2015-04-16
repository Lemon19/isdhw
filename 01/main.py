for a in range(1,10):
        print(" "*7*a,end="")
        for b in range(a,10):
            s=str.format("{0:1}*{1:1}={2:<3}",a,b,a*b)
            print(s,end="")
        print()
