import re

with open("log.txt", "r") as file:
    for line in file.readlines():
        datePattern = '((07:[4-5][0-9]:[0-5][0-9])|(0[8-9]:[0-5][0-9])|(1[0-2]:[0-5][1-9]:[0-5][0-9])|(13:[0-3][0-9]:[0-1][0-8])|(13:4[0-3]:[0-2][0-9]))'
        statusPattern = "^(?:(?!jpeg)(?!jpg)(?!png)(?!gif).)*?$"
        methodPattern = '(GET)'
        checkedStatusLine = re.search(statusPattern, line)
        checkedMethodLine = re.search(methodPattern, line)
        checkedDateLine = re.search(datePattern, line)
        if checkedStatusLine and checkedMethodLine and checkedDateLine:
            print(line)
            checkedStatusLine = False
            checkedMethodLine = False
            checkedDateLine = False
