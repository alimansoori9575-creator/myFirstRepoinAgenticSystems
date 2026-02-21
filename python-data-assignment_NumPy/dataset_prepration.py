###         Question: NumPy-Based Dataset Preparation Pipeline          ###
import numpy as np

np.random.seed(42)
data = np.random.rand(100, 3)

mean = data.mean(axis=0)
std = data.std(axis=0)

normalized = (data - mean) / std
#print(normalized)     # This is to see what is the actual value
training_set = normalized[:80]
test_set = normalized[80:]
training_set[0, 0] = 9.111
#print(normalized)   # and this is to demonstrate view behavior and to show chaned value

print('Original data shape:', data.shape)
print('Mean shape:', mean.shape)
print('standard deviation shape:', std.shape)
print('Training data shape:', training_set.shape)
print('Test data shape:', test_set.shape)
print('Note: Modifying the slice (training_set) affected the original array (normalized)')






