import numpy as np

expected = np.array([0, 1, 2, 3, 4])
prediction = np.array([0, 0.9, 2, 3, 5])
average = np.array([2, 2, 2, 2, 2])

def r_squared(y_expected, y_prediction):
	avg = np.average(y_expected)
	difference_from_average = y_expected - avg
	difference_from_prediction = y_expected - y_prediction
	total_sum = np.sum(difference_from_average ** 2)
	residual_sum = np.sum(difference_from_prediction ** 2)
	return (1 - (residual_sum / total_sum))

def adjusted_r_squared(y_expected, y_prediction, degree):
	r2 = r_squared(y_expected, y_prediction)
	n = y_expected.size
	return 1 - ((1 - r2)*(n - 1))/(n - degree - 1)

print(r_squared(expected, expected))
print(r_squared(expected, prediction))
print(r_squared(expected, average))
print(adjusted_r_squared(expected, expected, 1))
print(adjusted_r_squared(expected, prediction, 1))
print(adjusted_r_squared(expected, average, 1))
print(adjusted_r_squared(expected, expected, 2))
print(adjusted_r_squared(expected, prediction, 2))
print(adjusted_r_squared(expected, average, 2))
print(adjusted_r_squared(expected, expected, 3))
print(adjusted_r_squared(expected, prediction, 3))
print(adjusted_r_squared(expected, average, 3))