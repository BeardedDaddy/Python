# sample.py

def read_data():
   return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sample = read_data()

def mean(data):
   return sum(data) / len(data)

average = mean(sample)

python -i sample.py

