import random

# Mở (hoặc tạo) file để ghi
with open('./graph/data3.txt', "w") as file:
    # Ghi 25 dòng với thứ tự và giá trị ngẫu nhiên
    for i in range(1, 26):
        random_value = round(random.uniform(0.3, 0.65), 2)  # Lấy giá trị ngẫu nhiên và làm tròn đến 2 chữ số
        file.write(f"{i}. {random_value}\n")  # Ghi dòng vào file

print("Đã ghi xong 25 dòng vào file 'output.txt'.")
