from collections import defaultdict

class Data(object):
  def __init__(self, filename = 'data.txt'):
    self.filename = filename
    self.load()

  def load(self):
    file_data = open(self.filename).read().split('\n')
    self.data = [[float(item) for item in row.split(',')] for row in file_data]

  def get_train_valid(self):
    percentage_train = 0.8
    return self.data_by_classes()

  def data_by_classes(self):
    percent_train = 0.8

    data = defaultdict(lambda: [])
    for datum in self.data:
      klass = str(int(datum[-1]))
      data[klass].append(datum)

    split_data = [[], []]

    for key in list(data.keys()):
      class_items = data[key]
      n_train = int(len(class_items) * percent_train)
      [split_data[0].append(item) for item in class_items[:n_train]]
      [split_data[1].append(item) for item in class_items[n_train:]]

    return split_data