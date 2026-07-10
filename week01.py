print("Your hour is : 60 minutes")
seconds = int(input("Please enter seconds: "))

total_minutes = seconds // 60
border = "=" * 35

total_seconds = seconds % 60
print(border)
print(f"=  Results : {total_minutes} minute {total_seconds} seconds  =")
print(border)