###         Question: NumPy-Based Data Normalization Pipeline           ###
import numpy as np

data = np.array([10, 20, 30, 40])

mean = data.mean()

std = data.mean()

normalized = (data - mean) / std

reshaped = normalized.reshaped(2, 2)

