from collections import defaultdict

class Data(object):
  def __init__(self, percentage=0.8, filename = 'data.txt'):
    self.percentage = percentage
    self.filename = filename
    self.load()

  def classes(self):
    return list(self.get_data_by_classes().keys())

  def load(self):
    file_data = open(self.filename).read().split('\n')
    self.data = [[float(item) for item in row.split(',')] for row in file_data]
    return self.data

  def get_data_by_classes(self, data_list=None):
    data = defaultdict(lambda: [])
    for datum in data_list or self.data:
      klass = str(int(datum[-1]))
      data[klass].append(datum)
    return data

  def get_train_valid(self):
    data = self.get_data_by_classes()
    split_data = [[], []]

    for key in list(data.keys()):
      class_items = data[key]
      n_train = int(len(class_items) * self.percentage)
      [split_data[0].append(item) for item in class_items[:n_train]]
      [split_data[1].append(item) for item in class_items[n_train:]]

    return split_data