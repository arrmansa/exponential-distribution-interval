import random
from math import log, log1p, ceil
p = 0.0000001
print(ceil(log(random.random())/log1p(-p)))
