def is_report_safe(line):
    report = line.split()
    isIncrease = None

    for i in range(len(report) - 1):
        adj = int(report[i]) - int(report[i + 1])
        if abs(adj) > 3 or abs(adj) < 1:
            return False
        if isIncrease is not None:
            if adj < 0 and isIncrease:
                return False
            elif adj > 0 and isIncrease is False:
                return False
        else:
            isIncrease = adj > 0

    return True

sum = 0
with open('../inputs/day2.txt', 'r') as file:
    for line in file:
        if is_report_safe(line):
            sum=sum+1
print(sum)
