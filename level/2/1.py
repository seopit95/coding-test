A, B = map(int, input().split())

if not (-10000 <= A <= 10000 and -10000 <= B <= 10000):
    print('-10000 이상 10000 이하로 입력해주세요.')
    exit()

if (A > B):
    print('>')
if (A < B):
    print('<')
if (A == B):
    print('==')