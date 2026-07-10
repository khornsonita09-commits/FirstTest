
bill = int(input("Please enter bill: $ "))
tip = float(input("Please enter tip: % "))

tip = ( bill *  tip )// 100
total = bill + tip


border = "=" * 21

print(border)
print(f"=  Results : {tip} $  =")
print(border)