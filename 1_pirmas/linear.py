import random
from data import Data

data = Data('data.txt').load()

w1, w2, b = [(random.randint(0,100) / 100) for i in list(range(0, 3))]

lr = 0.01
num_epochs = 1000
epochs = range(1, num_epochs)

def output(x1, x2):
  o = x1 * w1 + x2 * w2 + b
  return 1 if o > 0 else -1

for epoch in epochs:
  for row in data:
    x1, x2, y = row
    y_hat = output(x1, x2)
    error = y - y_hat
    w1 = w1 + (lr * error * x1)
    w2 = w2 + (lr * error * x2)
    b = b + (lr * error)

for row in data:
  x1, x2, y = row
  predicted = output(x1, x2)
  print(f'Real: {int(y)}, predicted: {round(predicted, 100)}')
