import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


def distance_from_coordinates(data_point1,data_point2):
    
    return abs(math.sqrt((data_point2[0] - data_point1[0])**2 + (data_point2[1] - data_point1[1])**2))
    

data = pd.read_csv("ML_G1_lab4_dataset.csv")

number_of_centroids = 2
coordinates_of_centroid =list(list())
color_of_centroid = [6,7]



epochs = 100
i = 0

# parsed data
parsed_data =list(zip(data['x'], data['y'],data['color']))



while( i < epochs):
    
    # calculating distance between the all the data points and all the centroids
    for i in parsed_data:
        smallest_coordinate = 0
        for j in coordinates_of_centroid:
            
            old_distance = 
            new_distance = distance_from_coordinates(i, j)
            
            if new_distance<old_distance:
                smallest_coordinate = new_distance
            
            
    
    
    i = i + 1


#plotting the data

x = parsed_data
y = data['y']
colors = data['color']

plt.scatter(x,y, c= colors)

#plt.show()




