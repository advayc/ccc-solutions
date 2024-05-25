def local_time(t, c):
    lt = t + c

    if lt > 2400:
        lt -= 2400
    elif lt < 0:
        lt += 2400

    if lt % 100 >= 60:
        lt = (lt // 100 * 100 + 100) + (lt % 100 - 60)

    return lt

OttawaTime = int(input())

print(local_time(OttawaTime, 0), "in Ottawa")
print(local_time(OttawaTime, -300), "in Victoria")
print(local_time(OttawaTime, -200), "in Edmonton")
print(local_time(OttawaTime, -100), "in Winnipeg")
print(local_time(OttawaTime, 0), "in Toronto")
print(local_time(OttawaTime, 100), "in Halifax")
print(local_time(OttawaTime, 130), "in St. John's")
