import matplotlib.pyplot as plt

# Đọc dữ liệu từ file
time_steps = []
values = []

with open('./graph/data3.txt', "r") as file:
    for line in file:
        parts = line.strip().split(". ")  # Tách dữ liệu theo định dạng "{thứ tự}. {giá trị}"
        time_steps.append(int(parts[0]))  # Thứ tự dòng
        values.append(float(parts[1]))   # Giá trị ngẫu nhiên

# Vẽ biểu đồ
plt.figure(figsize=(10, 6))
plt.plot(time_steps, values, marker="o", color="blue", label="Predicted")
plt.xlabel("Time Steps", fontsize=12)
plt.ylabel("Predicted Value", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig('./graph/model.png')
plt.show()
