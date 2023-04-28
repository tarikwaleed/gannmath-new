import math

x = 4000  # this is input field from html
y = 4008  # this is input field from html
z = 100  # this is input field from html
w = x * z
r = y * z
e = abs((w**0.5) - (r**0.5)) / 0.005555
while not (43 <= e < 180):
    z = int(input())
    w = x * z
    r = y * z
    e = ((abs(w) ** 0.5) - (abs(r) ** 0.5)) / 0.005555
a = None


if 43 <= e < 58:
    a = 45
elif 58 <= e < 70:
    a = 60
elif 70 <= e < 88:
    a = 72
elif 88 <= e < 106:
    a = 90
elif 106 <= e < 118:
    a = 108
elif 118 <= e < 126.57:
    a = 120
elif 126.57 <= e < 133:
    a = 128.57
elif 133 <= e < 138:
    a = 135
elif 138 <= e < 142:
    a = 140
elif 142 <= e < 145.27:
    a = 144
elif 145.27 <= e < 148:
    a = 147.27
elif 148 <= e < 151.31:
    a = 150
elif 151.31 <= e < 153.29:
    a = 152.31
elif 153.29 <= e < 155:
    a = 154.29
elif 155 <= e < 157.5:
    a = 156
elif 157.5 <= e < 158.2:
    a = 157.5
elif 158.2 <= e < 160:
    a = 158.82
elif 160 <= e < 161.06:
    a = 160
elif 161.06 <= e < 162:
    a = 161.05
elif 162 <= e < 178:
    a = 162
elif 178 <= e < 182:
    a = 180
else:
    a = 1

levels = [0.25, 0.383, 0.5, 0.618, 0.75, 1]
cs = []
for l in levels:
    cs.append((a * 4 * l) / 180)
print(cs)
# results = []
# for c in cs:
#     if x / y > 1:
#         result = round(math.pow(math.sqrt(w) - c, 2) / z, 5)
#     else:
#         result = round(math.pow(math.sqrt(w) + c, 2) / z, 5)
#     results.append(result)
