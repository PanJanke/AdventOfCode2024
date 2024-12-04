
# ten testowy pokazuje dokladnie ze posralem przyogotwanie danych wejsciowych
# bo operuje caly czas na stringu a nie zbiorze intow
# niechce mi sie tego juz ruszac
def is_report_safe(line):
    report = line.split()
    print(line)
    isIncrease = None

    for i in range(len(report) - 1):
        print(report[i])
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
with open('../inputs/day2test.txt', 'r') as file:
    for line in file:
        index = is_report_safe(line)
        line.split()
        if index == -1:
            sum = sum + 1
        elif index == False:
            stringA = line[:0] + line[0 + 1:]
            stringB = line[:1] + line[1 + 1:]
            if is_report_safe(stringA) == -1 or is_report_safe(stringB) == -1:
                sum = sum + 1
        else:
            stringC = line[:index] + line[index + 1:]
            if is_report_safe(stringC) == -1:
                sum = sum + 1

print(sum)


