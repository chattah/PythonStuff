hrs = raw_input("Enter Hours:")
rate = raw_input("Rate Per Hour:")

h = float(hrs)
overTimePay = 0

if h <= 40:
    regularPay = h * float(rate)
else:
    regularPay = 40.00 * float(rate)

if h > 40:
    overTimeHours = h - 40.00
    overTimePay = overTimeHours * (float(rate) * 1.5)

pay = regularPay + overTimePay

print pay




