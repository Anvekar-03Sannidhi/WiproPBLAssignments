#WAP to print prime no.s b/w 10 and 99

for i in range(10, 100):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i, end="\t")
