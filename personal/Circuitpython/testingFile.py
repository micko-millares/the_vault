voltage = 10000 * 3.3 / 65536 * 1000
res_rating = 10000

print(round(voltage, 2))


power_mW = voltage ** 2 / res_rating

print(power_mW)

current = voltage / res_rating

print(current)
