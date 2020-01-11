from data import Data
from net import Net

epochs = 10000
xs, ys = Data.generate()
network = Net(xs, ys, [4, 4], lr=0.001)

for epoch in range(0, epochs):
  epoch_errors = []

  for idx, x in enumerate(xs):
    outputs = network.forward(x)
    error = min(round(ys[idx][0] - outputs[0], 5), 2) ** 2 / 2
    epoch_errors.append(error)
    network.backward(error)

  if epoch % 100 == 0:
    print(f'Epoch {epoch}')
    print(f'Error: {sum(epoch_errors) / len(epoch_errors)}')
    