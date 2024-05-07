import os

# Hàm để thêm vận động viên mới vào danh sách
def them_vdv(danh_sach):
    mavdv = input("Nhập mã số VĐV (chỉ chứa số): ")
    if not mavdv.isdigit():
        print("Mã số VĐV chỉ được chứa số. Vui lòng nhập lại.")
        return

    for vdv in danh_sach:
        if vdv['MaVDV'] == mavdv:
            print("Mã số VĐV đã tồn tại. Vui lòng nhập lại.")
            return

    hoten = input("Nhập họ và tên VĐV: ")
    if not hoten.replace(" ", "").isalpha():
        print("Họ và tên không được chứa số hoặc bỏ trống. Vui lòng nhập lại.")
        return

    ngaysinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
    phai = input("Nhập phái (Nam/Nữ): ")
    montg = input("Nhập môn thể thao tham gia: ")
    if not montg.replace(" ", "").isalpha():
        print("Môn thể thao không được chứa số hoặc bỏ trống. Vui lòng nhập lại.")
        return

    vdv_moi = {'MaVDV': mavdv, 'HoTen': hoten, 'NgaySinh': ngaysinh, 'Phai': phai, 'MonTG': montg}
    danh_sach.append(vdv_moi)
    cap_nhat_file(danh_sach)
    print("Vận động viên đã được thêm thành công.")


# Hàm để sửa thông tin của vận động viên trong danh sách
def sua_vdv(danh_sach):
    mavdv = input("Nhập mã số VĐV cần sửa thông tin: ")
    for vdv in danh_sach:
        if vdv['MaVDV'] == mavdv:
            print("Thông tin cũ của vận động viên:")
            print(vdv)
            vdv['HoTen'] = input("Nhập họ và tên mới: ")
            vdv['NgaySinh'] = input("Nhập ngày sinh mới (dd/mm/yyyy): ")
            vdv['Phai'] = input("Nhập phái mới (Nam/Nữ): ")
            vdv['MonTG'] = input("Nhập môn thể thao tham gia mới: ")
            cap_nhat_file(danh_sach)
            print("Thông tin vận động viên đã được cập nhật thành công.")
            return
    print("Không tìm thấy vận động viên có mã số", mavdv)

# Hàm để xoá vận động viên khỏi danh sách
def xoa_vdv(danh_sach):
    mavdv = input("Nhập mã số VĐV cần xoá: ")
    for vdv in danh_sach:
        if vdv['MaVDV'] == mavdv:
            danh_sach.remove(vdv)
            cap_nhat_file(danh_sach)
            print("Vận động viên đã được xoá khỏi danh sách.")
            return
    print("Không tìm thấy vận động viên có mã số", mavdv)

# Hàm để xem danh sách các vận động viên theo môn tham gia
def xem_danh_sach_mon(danh_sach):
    mon = input("Nhập môn thể thao muốn xem danh sách vận động viên: ")
    danh_sach_mon = [vdv for vdv in danh_sach if vdv['MonTG'] == mon]
    print("Danh sách các vận động viên tham gia môn", mon, ":")
    for vdv in danh_sach_mon:
        print(vdv)
    print("Tổng số vận động viên tham gia môn", mon, "là:", len(danh_sach_mon))

# Hàm để cập nhật dữ liệu vào file
def cap_nhat_file(danh_sach):
    with open("DuLieu.txt", "w", encoding="utf-8") as file:
        for vdv in danh_sach:
            file.write(','.join(vdv.values()) + '\n')

# Hàm để xóa toàn bộ dữ liệu trong file
def xoa_du_lieu_trong_file():
    if os.path.exists("DuLieu.txt"):
        os.remove("DuLieu.txt")
        print("Dữ liệu trong file đã được xoá.")
    else:
        print("File không tồn tại.")

# Hàm chính của chương trình
def main():
    danh_sach_vdv = []

    # Đọc dữ liệu từ file nếu file tồn tại
    if os.path.exists("DuLieu.txt"):
        with open("DuLieu.txt", "r", encoding="utf-8") as file:
            for line in file:
                vdv_info = line.strip().split(',')
                if len(vdv_info) >= 5:
                    vdv = {'MaVDV': vdv_info[0], 'HoTen': vdv_info[1], 'NgaySinh': vdv_info[2], 'Phai': vdv_info[3], 'MonTG': vdv_info[4]}
                    danh_sach_vdv.append(vdv)
                else:
                    print("Dòng không hợp lệ:", line.strip())

    while True:
        print("\n----- Menu -----")
        print("1: Thêm vận động viên")
        print("2: Sửa thông tin vận động viên")
        print("3: Xoá vận động viên")
        print("4: Xem danh sách các vận động viên theo môn tham gia")
        print("5: Xem dữ liệu thô trong file")
        print("6: Xoá toàn bộ dữ liệu trong file")
        print("0: Thoát khỏi chương trình")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == "1":
            them_vdv(danh_sach_vdv)
        elif lua_chon == "2":
            sua_vdv(danh_sach_vdv)
        elif lua_chon == "3":
            xoa_vdv(danh_sach_vdv)
        elif lua_chon == "4":
            xem_danh_sach_mon(danh_sach_vdv)
        elif lua_chon == "5":
            print("----- Dữ liệu thô trong file -----")
            if os.path.exists("DuLieu.txt"):
              with open("DuLieu.txt", "r", encoding="utf-8") as file:
                    print(file.read())
            else:
                print("File không tồn tại.")
        elif lua_chon == "6":
            xoa_du_lieu_trong_file()
        elif lua_chon == "0":
            print("Đã thoát khỏi chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    main()
