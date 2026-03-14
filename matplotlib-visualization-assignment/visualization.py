import numpy as np
import matplotlib.pyplot as plt

epochs = list(range(1,11))
np.random.seed(42)
loss = np.random.rand(10)
#print(loss)

plt.figure(figsize=(6,4))
plt.plot(epochs,loss,marker='o')
plt.grid(True)
plt.title("Loss vs Epoch")
plt.xlabel("epochs")
plt.ylabel("loss")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(epochs,loss,marker='s')
plt.grid(True)
plt.title("Epoch vs Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()

models = ['Model A', 'Model B', 'Model C']
accuracy = [0.85,0.90,0.88]

plt.figure(figsize=(6,4))
plt.bar(models,accuracy)
plt.title("Modles accuracy comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.show()
