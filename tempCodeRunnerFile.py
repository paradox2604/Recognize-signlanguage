import matplotlib.pyplot as plt

# Khai báo danh sách để lưu dữ liệu
window_slide_values = []
mean_predicted_values = []
mean_prediction_times = []

# Đọc dữ liệu từ file data.txt
with open('./graph/data.txt', 'r') as f:
    for line in f:
        # Tách các giá trị trên mỗi dòng bằng khoảng trắng
        values = line.strip().split()
        if len(values) == 3:
            window_slide_values.append(int(values[0]))  # windowSlide
            mean_predicted_values.append(float(values[1]))  # mean_predicted_value
            mean_prediction_times.append(float(values[2]))  # mean_prediction_time

# Vẽ biểu đồ
plt.figure(figsize=(12, 6))

# Biểu đồ 1: mean_predicted_value theo windowSlide
plt.subplot(1, 2, 1)
plt.plot(window_slide_values, mean_predicted_values, marker='o', color='b', label='Mean Predicted Value')
plt.xlabel('Window Slide')
plt.ylabel('Mean Predicted Value')
plt.title('Mean Predicted Value')
plt.grid(True)
plt.legend()

# Biểu đồ 2: mean_prediction_time theo windowSlide
plt.subplot(1, 2, 2)
plt.plot(window_slide_values, mean_prediction_times, marker='o', color='r', label='Mean Prediction Time')
plt.xlabel('Window Slide')
plt.ylabel('Mean Prediction Time (seconds)')
plt.title('Mean Prediction Time')
plt.grid(True)
plt.legend()

# Hiển thị biểu đồ
plt.tight_layout()
plt.savefig('./graph/Sliding Window.png')
plt.show()
