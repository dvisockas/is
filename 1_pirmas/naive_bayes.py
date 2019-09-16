import random
from math import exp, pi, sqrt
from data import Data
from collections import defaultdict

data = Data()
train_data, validation_data = data.get_train_valid()
train_data_by_class = data.get_data_by_classes(train_data)
classes = data.classes()

def get_probablity_of_class(klass):
  return len(train_data_by_class[str(int(klass))]) / len(train_data)

def get_nth_x(num_x, klass):
  return [x[num_x] for x in train_data_by_class[str(int(klass))]]

def get_mean(num_x, klass):
  xs = get_nth_x(num_x, klass)
  return sum(xs) / len(xs)

def get_variance(num_x, klass):
  xs = get_nth_x(num_x, klass)
  mean = get_mean(num_x, klass)
  return sum([((x - mean) ** 2) for x in xs]) / (len(xs) - 1)

def get_probability_of_x(x, num_x, klass):
  mean = get_mean(num_x, klass)
  sigma = get_variance(num_x, klass)
  exp_degree = (((x - mean)**2) * -1 ) / (2 * sigma)
  return (1 / sqrt(2 * pi * sigma)) * exp(exp_degree)

def get_prior(input_vector, klass):
  class_evidence = get_probablity_of_class(klass)
  for index, feature in enumerate(input_vector):
    class_evidence *= get_probability_of_x(feature, index, klass)
  return class_evidence

def get_evidence(input_vector):
  return sum([get_prior(input_vector, klass) for klass in classes])

for row in validation_data:
  x1, x2, y = row
  input_vector = [x1, x2]
  class_prediction = get_prior(input_vector, y) / get_evidence(input_vector)
  print(f'Real: {y}, confidence of prediction: {round(class_prediction, 2)}')