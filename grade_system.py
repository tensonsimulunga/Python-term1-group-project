marks = []

for i in range(1, 6):
    while True:
        mark = float(input(f"Enter mark {i} (0 - 100): "))
        if 0 <= mark <= 100:
            marks.append(mark)
            break
        else:
            print("❌ Invalid mark! Enter between 0 and 100.")average = sum(marks) / 5
print("Average:", round(average, 2))
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
