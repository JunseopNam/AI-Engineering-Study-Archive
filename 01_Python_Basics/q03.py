# q03 초를 시,분,초로 바꾸기

seconds = 3725
minutes = seconds // 60
hours = minutes // 60

real_seconds = seconds % 60
real_minutes = minutes % 60

print(str(hours) + '시간', str(real_minutes) + '분', str(real_seconds) + '초')