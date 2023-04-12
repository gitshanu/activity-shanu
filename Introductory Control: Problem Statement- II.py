NIN = 28
Div = 1
sum_of_divisors = 0
while Div < NIN:
    if NIN % Div == 0:
        sum_of_divisors += Div
    Div += 1
if sum_of_divisors > NIN:
    category = "abundant"
elif sum_of_divisors < NIN:
    category = "deficient"
else:
    category = "perfect"
print("The number", NIN, "is", category)
