'''
구매한 각 물건의 가격과 개수
구매한 물건들의 총 금액
'''

recipt_price = int(input()) # 영수증에 적힌 금액
N = int(input()) # 물건 종류 수

total = 0
for _ in range(N): # N번 순회
    price, product = map(int, input().split())
    total += price * product # 가격 * 개수

if total == recipt_price:
    print('Yes')
else:
    print('No')