# q05 날짜 문자열 분해하기

a = "20260823Sunny"
year = a[:4]
month = a[4:6]
day = a[6:8]
weather = a[8:]

print(year, month, day, weather, '\n' + str(year) + "년", str(month) + "월", str(day) + "일의 날씨는", str(weather) + "입니다.")
print(a[::-1])