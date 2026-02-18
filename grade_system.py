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
