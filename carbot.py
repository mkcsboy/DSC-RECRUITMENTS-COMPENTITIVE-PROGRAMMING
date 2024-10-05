def carbot():
    bottles=int(input())
    s,m,l,xl=6,12,24,48
    no_xl=no_l=no_m=no_s=0
    while bottles>=s:
        if (bottles>=xl):
            no_xl=bottles//xl
            bottles-=(no_xl*xl)
        elif (bottles>=l):
            no_l=bottles//l
            bottles-=(no_l*l)
        elif (bottles>=m):
            no_m=bottles//m
            bottles-=(no_m*m)
        elif (bottles>=s):
            no_s=bottles//s
            bottles-=(no_s*s)
        else:
            break
    if bottles>0:
        no_s+=1
    print(no_xl,"xl,",no_l,"large,",no_m,"medium,",no_s,"small")
carbot()
