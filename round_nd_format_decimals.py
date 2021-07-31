amount = 12618.98
interest_rate = 0.0013
interest = amount * interest_rate
print("interest is: ", interest)
print("\ninterest is: ", round(interest, 2))
print("\ninterest is: ", format(interest, ".2f"))           #format(item, format-specifier)


#format-specifier
"""
    width.precisionf: format(52.7, 10.2f)           [size = 10 , precision after decimal = 2]

    %: format(0.054, 10.2%)                         [10.2% causes number to be multiplied by 100 and displayed as percentage]

    
"""