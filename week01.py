from unittest import result

word = int(input("Please enter word: "))
exel = int(input("Please enter exel: "))
powerpoint = int(input("Please enter powerpoint: "))

total = ( word + exel + powerpoint ) // 3

border = "=" * 36
print(border)
print(f"=   Results : Average is : {float(total)}    =")
print(border)