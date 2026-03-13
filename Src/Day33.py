import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
X = np.array([
    [2,3],
    [3,4],
    [5,6],
    [6,7],
    [7,8],
    [8,5]
])

y = np.array([0,0,1,1,1,0])
new_point = np.array([[5,5]])
for k in [1,3,5]:
    
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X,y)
    
    prediction = model.predict(new_point)
    
    print(f"k = {k}, Prediction = {prediction[0]}")
    
plt.scatter(X[:,0], X[:,1], c=y, cmap='coolwarm', s=100)

plt.scatter(new_point[:,0], new_point[:,1], color='green', s=200, marker='X')

plt.title("KNN Nearest Neighbors Example")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()

import numpy as np

# Two numeric vectors
A = np.array([3, 4])
B = np.array([0, 0])

print("Vector A:", A)
print("Vector B:", B)
# Euclidean distance
euclidean = np.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)

print("Euclidean Distance:", euclidean)
# Manhattan distance
manhattan = abs(A[0]-B[0]) + abs(A[1]-B[1])

print("Manhattan Distance:", manhattan)