
bill = int(input("Please enter bill: $ "))
tip = float(input("Please enter tip: % "))

tip = ( bill *  tip )// 100
total = bill + tip


border = "=" * 30

print(border)
print(f"=   Results : Price {total} $   =")
print(f"=   Results : Tip {tip} $      =")

print(border)