class Data(object):
  def __init__(self, filename):
    self.filename = filename

  def load(self):
    file_data = open(self.filename).read().split('\n')
    return [[float(item) for item in row.split(',')] for row in file_data]


