#оставление в списке только уникальных аргументов, последняя задача, что была на семинареое
from itertools import count


num =[1, 5, 2, 3, 5, 1, 5, 5, 3, 10]
res = list(filter(lambda x: list(num).count(x) == 1, num))
#res = [i for i in num if x.count(i)  == 1] 
print(res)