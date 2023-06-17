import pickle

restored_data = pickle.load(open('data.p', 'rb'))
print(restored_data)