import matplotlib.pyplot as plt

def generate_pie_chart():
  labels = ['a','b','c','d']
  values = [100,200,300,400]
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
   generate_pie_chart(labels, values)