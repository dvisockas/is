from data import Data
from net import Net

import pdb

xs, ys = Data.generate()
network = Net(xs, ys, [4, 4])

for idx, x in enumerate(xs):
  outputs = network.forward(x)
  for jdx, output in enumerate(outputs):
    print(ys[idx][jdx] - output)
