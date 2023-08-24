T = int(input())
for tc in range(1, T+1):
    text = input()

    for i in range(1, 11):
        if text[:i] == text[i: i+i] == text[i+i: i+i+i]:
            ans = i
            break

    print(f'#{tc} {ans}')