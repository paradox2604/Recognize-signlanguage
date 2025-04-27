import matplotlib.pyplot as plt
import numpy as np


# Khai báo danh sách để lưu dữ liệu
mean_predicted_values = []
mean_prediction_times = []

# Đọc dữ liệu từ file data.txt
with open('./graph/data2.txt', 'r') as f:
    for line in f:
        # Tách các giá trị trên mỗi dòng bằng khoảng trắng
        values = line.strip().split()
        if len(values) == 2:
            mean_predicted_values.append(float(values[0]))  # mean_predicted_value
            mean_prediction_times.append(float(values[1]))  # mean_prediction_time

# Vẽ biểu đồ
plt.figure(figsize=(12, 6))

mean_predicted_value = np.mean(mean_predicted_values)
mean_prediction_time = np.mean(mean_prediction_times)

print(mean_predicted_value, " ", mean_prediction_time)