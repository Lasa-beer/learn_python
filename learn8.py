# python 字符串
# 字符串是python中最常用的数据类型 我们可以使用引号来创建字符串
# 创建一个字符串很简单，只要为变量分配一个值即可

var1 = 'jiushi '
var2 = 'number '

# Python 访问字符串中的值
# Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
#
# Python 访问子字符串，可以使用方括号来截取字符串，如下实例：

print(var1[3])   # 输出第四个字符
print(var2[1:3])# 输出从第二个开始到 第三个字符

# 字符串格式化输出

print('我是 %s，今年%s岁'%('小明','10'))