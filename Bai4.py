"""
- Input: Số lượng chi nhánh, số học viên đi học của từng lớp trong một chi nhánh
- Output: 
    + Trạng thái của từng lớp nếu dữ liệu hợp lệ 
    + Thông báo lỗi nếu nhập số âm
    + Thông báo lớp vắng toàn bộ nếu số học viên đi học bằng 0
"""

branch_count = int(input("Nhập số lượng chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"Chi nhánh {branch}:")
    
    for class_num in range(1, 3):
        while True:
            students_count = int(input(f"Nhập số học viên đi học của lớp {class_num}: "))
            if students_count < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
            else:
                break
        
        if students_count == 0:
            print(f"Chi nhánh {branch} - Lớp {class_num}: Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
        elif students_count >= 20:
            print(f"Chi nhánh {branch} - Lớp {class_num}: Lớp học ổn định")
        else:
            print(f"Chi nhánh {branch} - Lớp {class_num}: Lớp cần được nhắc nhở theo dõi")