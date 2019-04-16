def cutSticks(n):
    cuts = 0
    x=1
    while 1==1:
        if n == 1:
            break
        if n % 2 == 0:
            n = n/2

        elif n % 2 == 1:
            n = (n+1)/2

        cuts = cuts + 1
    print(cuts)

stick = 8
cutSticks(stick)
