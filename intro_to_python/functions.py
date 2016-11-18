# -------- greeter --------
# def greeter(greeting, name):
#     print("%(greeting)s %(name)s" %locals())
#
# greeter("Hola", "Jose")


# -------- tax calculator --------

def taxCalc(cost, taxRate):
    cost = float(cost)
    # print(cost)
    taxRate = float(taxRate)
    # print(taxRate)
    total = (cost * (1 + taxRate))
    # print(total)
    print("%(cost).2f, with a tax rate of %(taxRate).2f brings you to a total of %(total).2f" %locals())
    print("%.2f, with a tax rate of %.2f brings you to a total of %.2f" %(cost, taxRate, total))


taxCalc(20, .06)


# -------- BUILT IN PYTHON FUNCTUONS --------

# abs(num) ### absolute value of num

# bool(val) ### returns boolean value of val

# dir(dataType) ### dir() = .methods in Ruby

# help(array.count)  ### man for .count() on array data type
