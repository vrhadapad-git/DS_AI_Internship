import numpy as np
std_score=([[70,80,85],[75,85,95],[80,90,95],[55,98,56],[78,59,98]])
mean_avg=np.mean(std_score,axis=0)
print(mean_avg)
result = mean_avg-std_score
print(result)


#Task 2: The Reshaper (Array Manipulation)
sensor_R=np.arange(24)
print(sensor_R)
print(sensor_R.reshape(4,3,2))
print(sensor_R.reshape(4,2,3))
