x = '01.01.2001'
y = int(x.split('.')[2]) + 14
z = x[:6] + str(y)
print(
    z
)