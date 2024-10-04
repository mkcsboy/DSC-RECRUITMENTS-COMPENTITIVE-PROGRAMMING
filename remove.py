def remove():
    inlist=input().strip("[]")
    l=inlist.split(',')
    outlist=[]
    for i in l:
        if int(i) not in outlist:
            outlist.append(int(i))
    print(outlist)
remove()