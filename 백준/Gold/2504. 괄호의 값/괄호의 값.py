from collections import deque
import sys
input = sys.stdin.readline

arr = list(input().strip())

stack = deque()

condition = True

for oper in arr:
    # 닫는 기호가 아니라면 스택에 입력
    if oper not in [')',']']:
        stack.append(oper)
    else:
        try:
            # 닫는 기호가 들어온다면
            # 소괄호
            if oper == ')':
                top = 0
                nums = deque()
                while top != '(':
                    # top이 여는 괄호라면
                    if stack[-1] == '(':
                        top = stack.pop()
                        if nums: # nums가 1개일때 2개일떼 0개일때
                            stack.append(sum(nums) * 2)
                        else:
                            stack.append(2)
                    # top이 숫자라면 여는 괄호 만들 때까지
                    elif str(stack[-1]).isdigit():
                        top = stack.pop()
                        nums.append(top)
                    else:
                        condition = False
                        break
                if condition == False:
                    break
            # 대괄호
            elif oper == ']':
                top = 0
                nums = deque()
                while top != '[':
                    # top이 여는 괄호라면
                    if stack[-1] == '[':
                        top = stack.pop()
                        if nums: # nums가 1개일때 2개일떼 0개일때
                            stack.append(sum(nums) *3)
                        else:
                            stack.append(3)
                    # top이 숫자라면 여는 괄호 만들 때까지
                    elif str(stack[-1]).isdigit():
                        top = stack.pop()
                        nums.append(top)
                    else:
                        condition = False
                        break
                if condition == False:
                    break
        except:
            condition = False
            break
try:
    if condition:
        print(sum(stack))
    else:
        print(0)

except:
    print(0)