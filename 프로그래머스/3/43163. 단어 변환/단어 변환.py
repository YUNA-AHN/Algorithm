def solution(begin, target, words):
    from collections import deque
    answer = 0
    word_len = len(begin)
    lst_len = len(words)
    condition = False
    
    # words에 target 존재하는지 체크
    if target in words:
        visited = [0] * lst_len
        que = deque()
        que.append((begin, 0))
        
        while que:
            now, cnt = que.popleft()
            for idx in range(lst_len):
                # 이전에 체크한 단어가 아니어야 함 / 다른 글자 수 uncor
                if visited[idx] == 0:
                    uncor = 0
                    # 단어 길이만큼 순회하면서 다른 글자 체크
                    for i in range(word_len):
                        if now[i] != words[idx][i]:
                            uncor += 1
                    # 한 글자만 다르다면?!
                    if uncor <= 1:
                        # 만약 target이랑 같다면 break
                        if words[idx] == target:
                            answer = cnt + 1
                            condition = True
                            break
                        else:
                            visited[idx] = 1
                            que.append((words[idx], cnt+1))
                if condition:
                    break
                    
    return answer