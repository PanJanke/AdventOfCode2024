
# prawidlowy wynik to 300 z hakiem
def is_report_safe(report):
    isIncrease = None

    for i in range(len(report) - 1):
        adj = int(report[i]) - int(report[i + 1])
        if abs(adj) > 3 or abs(adj) < 1:
            if isIncrease is None:
                return False
            else:
                return i + 1
        if isIncrease is not None:
            if adj < 0 and isIncrease:
                return i + 1
            elif adj > 0 and isIncrease is False:
                return i + 1
        else:
            isIncrease = adj > 0

    return -1


sum = 0
with open('../inputs/day2.txt', 'r') as file:
    for line in file:
        line=line.split()
        index = is_report_safe(line)

        if index == -1:
            sum = sum + 1
        else:
            if index == False:
                stringA = line[:0] + line[0 + 1:]
                stringB = line[:1] + line[1 + 1:]
                if is_report_safe(stringA) == -1 or is_report_safe(stringB) == -1:
                    sum = sum + 1
            else:
                stringC = line[:index] + line[index + 1:]
                if is_report_safe(stringC) == -1:
                    sum = sum + 1
                    print(stringC)

print(sum)


