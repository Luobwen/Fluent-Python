# 列表推导

symbols = '$&*#@'
codes = [ord(symbol) for symbol in symbols]
print(codes)

# ============================================================================================

# filter & map 与 列表推导的比较
symbols = '$&*#@'
result1 = [ord(symbol) for symbol in symbols if ord(symbol) > 40]
print(result1)

result2 = list(filter(lambda x: x > 40, map(ord, symbols)))
print(result2)

# ============================================================================================

# 使用列表推导计算笛卡尔积

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# ============================================================================================

# 生成器表达式
# 跟列表推导的区别就是使用圆括号（列表推导使用的是[]）

for tshirt in ('{}, {}'.format(c,s) for c in colors for s in sizes):
    print(tshirt)