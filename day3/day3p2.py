import re

with open('../inputs/day3.txt', "r") as file:
    text = file.read()

pattern = "^(?!.*don't\(\)[^d]*?do\(\)).*$"

pattern2 = r"mul\(\s*\d+\s*,\s*\d+\s*\)"
subText = re.findall(pattern, text)
print(subText)

matches = re.findall(pattern, text)
sum=0
for match in matches:
    numbers = re.findall(r'\d+', match)
    sum=sum+int(numbers[0])*int(numbers[1])

print(sum)

