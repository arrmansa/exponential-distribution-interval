import random
from math import log, log1p, ceil
p = 0.00000000001
print(ceil(log(random.random())/log1p(-p)))
