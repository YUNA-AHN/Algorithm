# palin = ''
# while palin != '0':
#     palin  = input()
#     if palin == '0':
#         break
#     else: 
#         if palin == palin[::-1]:
#             print('yes')
#         else:
#             print('no')

while True :
    n = input()
    if n == "0" : break
    print('yes' if n == n[::-1] else 'no')
