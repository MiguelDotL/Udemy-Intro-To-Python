# def milesToKm(miles):
#     km = miles * 1.60934
#     print("%(miles)i miles is equal to %(km)f Km" %locals())
#
# milesToKm(20)

def milesToKm(miles):
    km = round((miles * 1.60934), 2)    # round to 2 decimals
    print("%(miles).2f miles is equal to %(km).2f Km" %locals())

mi = float(input("Please enter miles to be coverted to Km: "))
milesToKm(mi)
