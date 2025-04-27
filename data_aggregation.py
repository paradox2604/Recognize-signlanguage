import os

# Đường dẫn tới các file cần tổng hợp
source_dir = './datatrain_40/lable{}/'
# Đường dẫn đến thư mục chứa các file tổng hợp
destination_dir = './datatrain_40/total/'

# Tạo thư mục đích nếu chưa tồn tại
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Tên các file cần tạo mới
trainx_file = os.path.join(destination_dir, 'trainx.txt')
trainy_file = os.path.join(destination_dir, 'trainy.txt')
testx_file = os.path.join(destination_dir, 'testx.txt')
testy_file = os.path.join(destination_dir, 'testy.txt')

# Mở các file tổng hợp để ghi dữ liệu
with open(trainx_file, 'w') as trainx, \
     open(trainy_file, 'w') as trainy, \
     open(testx_file, 'w') as testx, \
     open(testy_file, 'w') as testy:

    # Duyệt qua tất cả các label (từ 0 đến 4)
    for label in range(5):
        # Duyệt qua tất cả các version (từ 1 đến 6)
        for version in range(1, 7):
            # Đường dẫn tới các file train và test của từng label/version
            data_file_path = source_dir.format(label) + f'trainx_{label}_v{version}.txt'
            label_file_path = source_dir.format(label) + f'trainy_{label}_v{version}.txt'
            data_test_file_path = source_dir.format(label) + f'testx_{label}_v{version}.txt'
            label_test_file_path = source_dir.format(label) + f'testy_{label}_v{version}.txt'
            
            # Đọc và ghi dữ liệu huấn luyện (trainx, trainy)
            if os.path.exists(data_file_path) and os.path.exists(label_file_path):
                with open(data_file_path, 'r') as data_file, \
                     open(label_file_path, 'r') as label_file:
                    trainx.writelines(data_file.readlines())
                    trainy.writelines(label_file.readlines())
            
            # Đọc và ghi dữ liệu kiểm tra (testx, testy)
            if os.path.exists(data_test_file_path) and os.path.exists(label_test_file_path):
                with open(data_test_file_path, 'r') as data_test_file, \
                     open(label_test_file_path, 'r') as label_test_file:
                    testx.writelines(data_test_file.readlines())
                    testy.writelines(label_test_file.readlines())

print("Hoàn thành tổng hợp các file dữ liệu và nhãn.")
