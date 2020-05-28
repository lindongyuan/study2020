#第一种方式：导入整个模块的方法
'''
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

#第二种方式：导入特定模块（其中某个函数）的方法
from pizza import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#第三种方式：使用as给函数指定别名
import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')

#导入模块中的所有函数
from pizza import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
'''
