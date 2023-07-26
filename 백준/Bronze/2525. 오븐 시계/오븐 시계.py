hour, minute = map(int, input().split())
times = int(input())

minute += times

if minute >= 60:
    hour += minute // 60
    minute %= 60
if hour >= 24:
    hour %= 24
    
print(hour, minute)