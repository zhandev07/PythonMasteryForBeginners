from matplotlib import pyplot as plt
import numpy as np

# Create sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# First subplot
ax1.plot(x, y1, color="red")
ax1.set_title("Sine Wave")

# Second subplot
ax2.plot(x, y2, color="green")
ax2.set_title("Cosine Wave")

plt.show()
