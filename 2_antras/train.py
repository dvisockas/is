from data import Data
from net import Net

import pdb

xs, ys = Data.generate()
network = Net(xs, ys, [4, 4])

for idx, x in enumerate(xs):
  outputs = network.forward(x)
  error = ys[idx][0] - outputs[0]

  