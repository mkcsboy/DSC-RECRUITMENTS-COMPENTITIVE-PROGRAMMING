def ascword():
    a=input()
    words=a.split()
    sort=sorted(words,key=len)
    end=' '.join(sort)
    print(end)
ascword()