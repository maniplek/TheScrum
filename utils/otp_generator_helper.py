import math
import random


def otp_genator():
    digits = "123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 4)]
    return OTP