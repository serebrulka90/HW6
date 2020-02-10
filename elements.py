def sumNumberParts(number):
    strNumber = str(number)
    result = 0
    for numberPart in strNumber:
       result += int(numberPart)
    return result

print(sumNumberParts(12345))