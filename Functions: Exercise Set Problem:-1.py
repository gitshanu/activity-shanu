a=float(input("Enter price: "))
b=input('Are you a Prime member : ')
def discount(a,b):
    if b=='yes' or b=='Yes' or b=='YES':
        d1=0.15*a
        c=a-d1
        bfd=0.08*c
        f_p=c-bfd
        return (f_p)
    else:
        s=0.08*a
        r=a-s
        return(r)
print(discount(a,b))
