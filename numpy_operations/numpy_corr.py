import numpy as np

study_hours = np.array([1, 2, 3, 4, 5, 6])
marks = np.array([40, 45, 55, 60, 70, 80])

print("Correlation:")
print(np.corrcoef(study_hours, marks))