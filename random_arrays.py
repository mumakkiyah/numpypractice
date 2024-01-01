import numpy as np

# create randomised arrays using np.random.normal and randint
np_height = np.round(np.random.normal(1.75, 0.20, 20),2)
np_weight = np.round(np.random.normal(65, 0.5, 20), 2)
np_age = np.random.randint(19, high=22, size=20, dtype=int)

# stacking all the arrays into rows and columns
np_class_room = np.column_stack((np_height, np_weight, np_age))

# calculating BMI using subsetting
np_bmi = np.round(np_class_room[:,1]/np_class_room[:,0]**2, 2)

# adding the BMI array to the existing np_class_room 3D array
np_class_room_updated = np.column_stack((np_class_room, np_bmi))

# iterating through the np_class_room_updated 3D array using np.nditer to categorize students 
# by lifestyle based on BMI and storing the values into a list lifestyle
lifestyle = []

for x in np.nditer(np_class_room_updated[:,3]):
    if x > 25:
        lifestyle.append('Obese')
    else:
        lifestyle.append('Healthy')

# converting lifestyle into an array np_lifestyle
np_lifestyle = np.array(lifestyle)

# adding the np_lifestyle to the existing np_class_room_updated 4D array
np_stud_stats = np.column_stack((np_class_room_updated, np_lifestyle))

# print the result
print(np_stud_stats)

# Filtering all the healthy and obese students (TBC)
