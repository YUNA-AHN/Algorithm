palin = ''
while palin != '0':
    palin  = input()
    if palin == '0':
        break
    else: 
        if palin == palin[::-1]:
            print('yes')
        else:
            print('no')