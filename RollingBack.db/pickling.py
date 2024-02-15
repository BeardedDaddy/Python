import pickle

#pickling
carlist = ['Toyota', 'BMW', 'Audi', 'Suzuki', 'Honda']
# open a file to store the pickle of cars
with open('carlist.pkl','wb') as carpickle: # To open you need parameters, the file name and the 
    pickle.dump(carlist, carpickle) # Dump is the functions that creates the pickle file. It takes two agruements.
    # The first is the file we want to pickle and the second arguement is the file object.
    
