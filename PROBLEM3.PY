a = int(input("Enter a number: "))

if a % 2 == 0:
    a -= 1  # reduce to previous odd number

series = []
for i in range(a):
    if len(series) < a:
        series.append(2 * i + 1)

print("Output:", ", ".join(map(str, series)))
