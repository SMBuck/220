import math

print("\t\t\tMethods of Calculating Mean")
variables = eval(input("Enter the values to be entered: "))
my_sum = 0
har_sum = 0
geo_sum = 1

for i in range(1, variables + 1):
    values = eval(input("Enter value: "))
    my_exp = math.pow(values, 2)
    my_sum = my_sum + my_exp
    div = 1 / values
    har_sum = har_sum + div
    geo_sum = geo_sum * values

mean = my_sum / variables
rms = math.sqrt(mean)
rms_average = round(rms, 3)

har_total = variables / har_sum

geo_total = math.pow(geo_sum, 1 / variables)
geo_round = round(geo_total, 3)
print(rms_average)
print(har_total)
print(geo_round)












