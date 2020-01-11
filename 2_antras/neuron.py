import pdb
from math import exp
from random import random

def activations(weight_bias):
  return {
    'tanh': tanh,
    'sigmoid': sigmoid,
  }

def tanh(x):
  return (2 / ( 1 + exp( -1 * x ) ))-1

def tanh_(x):
  return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

def sigmoid(x):
  return 1 / (1 + exp(-x))

def sigmoid_(x):
  return sigmoid(x) * (1 - sigmoid(x))

class Neuron(object):
  def __init__(self, inputs, activation = 'sigmoid'):
    self.activation = activation
    self.weights = [random() for weight in list(range(0, inputs))]
    self.bias = random()
    self.last_output = 0
    self.delta = 0

  def forward(self, ins):
    weighted_values = [self.weights[idx] * x_in for idx, x_in in enumerate(ins)]
    weight_bias = sum(weighted_values) + self.bias
    self.last_output = self.activate(weight_bias)
    self.inputs = ins
    return self.last_output
  
  def activate_derivative(self, input):
    output = 1
    if self.activation == 'tanh':
      output = tanh_(output)
    elif self.activation == 'sigmoid':
      output = sigmoid_(output)
    
    return output

  def activate(self, weight_bias):
    output = weight_bias
    if self.activation == 'tanh':
      output = tanh(output)
    elif self.activation == 'sigmoid':
      output = sigmoid(output)
  
    return output
