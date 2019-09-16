import random
from data import Data

train_data, validation_data = Data().get_train_valid()

w1, w2, b = [(random.randint(0,100) / 100) for i in list(range(0, 3))]

lr = 0.01
num_epochs = 1000
epochs = range(1, num_epochs)

print(f'Training with learning rate {lr} for {num_epochs} epochs')
print(f'Training samples: {len(train_data)}')
print(f'Validation samples: {len(validation_data)}')

def output(x1, x2):
  o = x1 * w1 + x2 * w2 + b
  return 1 if o > 0 else -1

for epoch in epochs:
  for row in train_data:
    x1, x2, y = row
    y_hat = output(x1, x2)
    error = y - y_hat
    w1 = w1 + (lr * error * x1)
    w2 = w2 + (lr * error * x2)
    b = b + (lr * error)

for row in validation_data:
  x1, x2, y = row
  predicted = output(x1, x2)
  print(f'Real: {int(y)}, predicted: {round(predicted, 100)}')
