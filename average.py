word = int(input("Please enter Word score: "))
excel = int(input("Please enter Excel score: "))
powerpoint = int(input("Please enter PowerPoint score: "))

total = (word + excel + powerpoint) // 3

if total >= 90:
    grade = "A"
elif total >= 80:
    grade = "B"
elif total >= 70:
    grade = "C"
elif total >= 60:
    grade = "D"
else:
    grade = "F"

border = "=" * 27
print(border)
print(f"=  Average Score : {total:.2f}  =")
print(f"=  Grade         : {grade}      =")
print(border)
