n=int(input("Enter a Wavelength: "))
if n<380 or n>750:
    print("Out of Range")
elif 380<=n<450:
    print("Violet")
elif 450<=n<495:
    print("Blue")
elif 495<=n<570:
    print("Green")
elif 570<=n<590:
    print("Yellow")
elif 590<=n<620:
    print("Orange")
elif 620<=n<=750:
    print("Red")
