import pandas

def read_csv(file_name):
    data = pandas.read_csv(file_name, header=None)
    return data