hour , minute = map(int, input().split())
MINUTE_PER_HOUR = 60
minutes = hour * MINUTE_PER_HOUR + minute - 45

new_hour = (minutes // MINUTE_PER_HOUR) % 24
new_min = minutes % MINUTE_PER_HOUR

print(new_hour, new_min)