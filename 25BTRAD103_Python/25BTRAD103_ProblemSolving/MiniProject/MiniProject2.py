# OTP Generator

import random

OTP = random.randint(100000, 999999)

print("Generated OTP:", OTP)

USER_OTP = int(input("Enter the OTP: "))

if OTP == USER_OTP:
    print("OTP VERIFIED")
else:
    print("INVALID OTP")




