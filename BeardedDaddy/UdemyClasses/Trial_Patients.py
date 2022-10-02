# trial_1 = {'Bob', 'Charlie', 'Georgia', 'John'}
# trial_2 = {'Anne', 'Charlie', 'Eddie', 'Georgia'}
# # print(trial_1 | trial_2)
# # print(trial_1 & trial_2)
# check_set = trial_1.intersection(trial_2)
# print(check_set)

farm_animals = {'sheep', 'hen', 'cow', 'horse', 'goat'}
wild_animals = {'loin', 'elephant', 'tiger', 'goat', 'panther', 'horse'}
potential_rides = {'donkey', 'horse', 'camel'}

# intersection = farm_animals & wild_animals & potential_rides
# print(intersection)
# intersection = farm_animals, wild_animals, potential_rides
# print(intersection)

mounts = farm_animals.intersection(wild_animals, potential_rides)
print(mounts)
