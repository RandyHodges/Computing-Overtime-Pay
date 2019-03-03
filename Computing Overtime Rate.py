hrs = input("Enter your hours")
rate = input("Enter your rate")
fh = float(hrs)
fr = float(rate)
if hrs > 40 :
    # print (fr, fh) fr = Flat Rate, fh = Flat Rate
    reg = fr * fh
    otp = (fr + 1.5) * (fh + 0)
    # print (reg, otp)
    xp = reg + otp
else:
    pay = float(fr * fh)
print("pay":, xp)
