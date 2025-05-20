score = int(input())

if not (0 <= score <= 100):
    print('0이상 100이하로 입력해주세요')
    exit()

if (90 <= score <= 100):
    print('A')
elif (80 <= score <= 89):
    print('B')
elif (70 <= score <= 79):
    print('C')
else:
    print('D')