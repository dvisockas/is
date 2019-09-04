import random
from data import Data

data = Data('data.txt').load()

w1, w2, b = [(random.randint(0,100) / 100) for i in list(range(0, 3))]

# Learning rate could be found in a similar fashion to weights and bias
lr = 0.001

def output(x1, x2):
  return x1 * w1 + x2 * w2 + b

for i in list(range(0, 10)):
  for row in data:
    x1, x2, y = row
    y_hat = output(x1, x2)
    error = y_hat - y
    w1 = w1 + (lr * error * x1)
    w2 = w2 + (lr * error * x2)
    b = b + (lr * error)

for row in data:
  x1, x2, y = row
  predicted = output(x1, x2)
  print(f'Real: {y}, predicted: {round(predicted, 4)}')
