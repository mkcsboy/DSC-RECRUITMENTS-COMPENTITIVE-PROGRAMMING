def calendar():
    day, year = map(int, input().split(","))
    if (year%4!=0):
        feb=28
    else:
        feb=29
    md=[31,feb,31,30,31,30,31,31,30,31,30,31]
    m= ["January","February","March","April","May","June","July","August","September","October","November","December"]
    xday=day
    for i in range(12):
        if xday<=md[i]:
            print(xday,m[i],year)
            break
        xday-=md[i]
calendar()