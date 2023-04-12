n=int(input("Enter a Frequency: "))
if n<(3*10**9):
    print("Radio Waves")
elif (3*10**9)<=n<(3*10**12):
    print("Micro Waves")
elif (3*10**12)<=n<(4.3*10**14):
    print("Infrared Light")
elif (4.3*10**14)<=n<(7.5*10**14):
    print("Visible Light")
elif (7.5*10**14)<=n<(3*10**17):
    print("Ultraviolet Light")
elif (3*10**17)<=n<(3*10**19):
    print("X-Rays")
elif (3*10**19)<=n:
    print("Gamma Rays")
