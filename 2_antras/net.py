from neuron import Neuron

class Net(object):
  def __init__(self, inputs, outputs, hidden_dimensions, lr = 0.1, activation = 'sigmoid'):
    self.input_size = len(inputs[0])
    self.output_size = len(outputs[0])
    self.hidden_dimensions = hidden_dimensions
    self.create_neurons()
    self.lr = lr

  def create_neurons(self):
    dims = self.hidden_dimensions
    self.layers = []

    for idx, layer in enumerate(dims):
      in_count = self.input_size if idx == 0 else dims[idx - 1]

      layer_neurons = [Neuron(in_count) for layer in dims]

      self.layers.append(layer_neurons)

    self.layers.append([Neuron(dims[-1], activation = 'linear')])

  def forward(self, input_vector):
    outs = input_vector

    for layer in self.layers:
      tmp_outs = []

      for neuron in layer:
        tmp_outs.append(neuron.forward(outs))

      outs = tmp_outs

    return outs

  def backward(self, error):
    # Reverse
    for lx, layer in enumerate(self.layers[::-1]):
      y = map(lambda i: i.inputs, layer)
      delta_base = self.lr * sum(sum(y, []))

      for neuron in layer:
        if layer == self.layers[-1]: # last layer
          neuron.delta = error * delta_base * neuron.activate_derivative(neuron.last_output)
        else:
          previous_layers_error = sum([neuron.delta for neuron in self.layers[-1:lx]])
          if layer == self.layers[0]: # first layer
            delta_base = self.lr * sum(neuron.inputs) * previous_layers_error
            neuron.delta = delta_base * neuron.activate_derivative(neuron.last_output)
          else:
            neuron.delta = delta_base * neuron.activate_derivative(neuron.last_output) * previous_layers_error 

        new_weights = [0] * len(neuron.weights)
        for idx, weight in enumerate(neuron.weights):
          weight_diff = self.lr * neuron.delta
          new_weights[idx] = weight + weight_diff
          
        neuron.weights = new_weights