import numpy as np

# Original point coordinates
x = 0.91
y = 0.91

# Convert the rotation angle to radians (135 degrees)
theta = np.radians(-135)

# Apply the rotation formulas
x_rotated = x * np.cos(theta) - y * np.sin(theta)
y_rotated = x * np.sin(theta) + y * np.cos(theta)

# Print the original and rotated coordinates
print(f"Original Point: ({x}, {y})")
print(f"Rotated Point: ({x_rotated:.2f}, {y_rotated:.2f})")
