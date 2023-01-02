#NHÓM SỐ 03 DHKL16A1HN
#22174600029 - PHẠM KHÁNH HUYỀN
#22174600030 - PHẠM THỊ THU TRANG
#22174500033 - NGUYỄN VĂN THANH
#22174600031 - NGUYỄN THỊ HÀ MÂY
#22174600032 - NGUYỄN THỊ THUYÊN

import os
import csv
_path="files/ds_can_bo.csv"
lst_canbo=[]
print("CHƯƠNG TRÌNH QUẢN LÝ CÁN BỘ")
while True:
    # Menu chương trình
    print("1: Mở file ds_can_bo.csv") 
    print("2: Nhập thêm thông tin cán bộ")
    print("3: Lưu thông tin cán bộ vào file ds_can_bo.csv")
    print("4: Sắp xếp các cán bộ theo chiều tăng dần của lương. In ra kết quả trước và sau")
    print("5: Thoát chương trình")
    chon=int(input("Chọn chức năng cần thực hiện: "))
    if chon==1:
        f=open(_path,'r', encoding ='utf-8')
        for i in csv.reader(f):
            lst_canbo.append({'Ma_can_bo':i[0],'Ten_can_bo':i[1], 'He_so_luong':i[2],'Chuc_vu':i[3],'Phu_cap':i[4],\
            'Luong':i[5]})
        f.close()
        print('Đã mở file ds_can_bo.csv')


    elif chon==2:
        macb = input('Nhập mã cán bô:')
        tencb = input('Nhập tên cán bộ:')
        hsl = float(input('Nhập hệ số lương:'))
        a = input("Chức vụ cán bộ: Giám đốc(chọn 1), Trưởng phòng(chọn 2), khác(chọn phím bất kì)  ")
        if a=="1":
            chucvu = 'Giam doc'
        elif a=="2":
            chucvu = 'Truong phong'
        else:
            chucvu = 'Khac'
        if chucvu == 'Giam doc':
            phucap = 10000000
        if chucvu == 'Truong phong':
            phucap = 5000000
        if chucvu == 'Khac':
            phucap = 2000000
        luong = float((hsl*1500000)+phucap)
        lst_canbo.append({'Ma_can_bo':macb, 'Ten_can_bo':tencb, 'He_so_luong':hsl,\
             'Chuc_vu':chucvu, 'Phu_cap':phucap, 'Luong':luong})
        print(lst_canbo)

    elif chon == 3:
        f=open(_path,'w',newline='', encoding = 'utf-8')
        csv.writer(f).writerow(['Ma_can_bo','Ten_can_bo',\
         'He_so_luong','Chuc_vu','Phu_cap', 'Luong'])
        for cb in lst_canbo:
            csv.writer(f).writerow([cb['Ma_can_bo'],\
            cb['Ten_can_bo'], cb['He_so_luong'],cb['Chuc_vu'], cb['Phu_cap'],cb['Luong']])
        f.close()
        print("Đã lưu file ds_can_bo.csv !")

    elif chon==4:
        luong = sorted(lst_canbo,reverse=True, key=lambda x: x['Luong'])
        print("Danh sách trước khi sắp xếp:")
        print('{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}'.format('Ma_can_bo','Ten_can_bo',\
         'He_so_luong','Chuc_vu','Phu_cap', 'Luong'))
        for x in lst_canbo:
            print('{:^18}{:^18}{:^18}{:^18}{:^18}'.format(x['Ma_can_bo'],\
            x['Ten_can_bo'], x['He_so_luong'],x['Chuc_vu'], x['Phu_cap'],x['Luong']))
        print("Danh sách cửa hàng sau khi sắp xếp: ")
        print('{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}'.format('Ma_can_bo','Ten_can_bo',\
         'He_so_luong','Chuc_vu','Phu_cap', 'Luong'))
        for x in luong:
            print('{:^18}{:^18}{:^18}{:^18}{:^18}'.format(x['Ma_can_bo'],\
                        x['Ten_can_bo'], x['He_so_luong'],x['Chuc_vu'], x['Phu_cap'],x['Luong']))
    elif chon==5:
        break
    

 
