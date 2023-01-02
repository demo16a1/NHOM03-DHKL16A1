
import csv
_path="files/ds_can_bo.csv"
lst_canbo = []
#Mở file ds_can_bo.csv
def mo_flie_can_bo(_path,lst_canbo):
    try:
        f=open(_path,'r', encoding ='utf-8')
        for i in csv.reader(f):
            if i[0]=='Ma_can_bo':
                continue
            lst_canbo.append({'Ma_can_bo' : i [ 0 ], 'Ten_can_bo' : i [ 1 ], 'He_so_luong' : i [ 2 ], 'Chuc_vu' : i [ 3 ], 'Phu_cap' : i [ 4 ],\
            'Luong' : i [ 5 ]})
        f.close()
        return 1
    except Exception as ex1:
        print('Không mở được file hợp lệ ', ex1)
    return

#hàm thêm thông tin cán bộ
def them_tt_canbo(lst_canbo):
    print('Menu  thông tin cán bộ:')
    while True:
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

        tt = input('Bạn có muốn tiếp tục thêm thông tin? (Chọn phím số 1):')
        if tt != "1":
            break
    return
them_tt_canbo(lst_canbo)

#Hàm in danh sách cán bộ
def in_ds_canbo(lst_canbo):
    print('{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}'.format('Ma_can_bo','Ten_can_bo',\
         'He_so_luong','Chuc_vu','Phu_cap', 'Luong'))
    
    for cb in lst_canbo:
        print('{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}'.format(cb['Ma_can_bo'],\
            cb['Ten_can_bo'], cb['He_so_luong'],cb['Chuc_vu'], cb['Phu_cap'],cb['Luong']))
    return
in_ds_canbo(lst_canbo)

#-----Hàm lưu danh sánh cán bộ
def luu_ds_canbo(_path,lst_canbo):
    try:
        f=open(_path,'w',newline='', encoding = 'utf-8')
        csv.writer(f).writerow(cb['Ma_can_bo'],\
            cb['Ten_can_bo'], cb['He_so_luong'],cb['Chuc_vu'], cb['Phu_cap'],cb['Luong'])
        for cb in lst_canbo:
            csv.writer(f).writerow([cb['Ma_can_bo'],\
            cb['Ten_can_bo'], cb['He_so_luong'],cb['Chuc_vu'], cb['Phu_cap'],cb['Luong']])
        f.close()
        return 1
    except Exception as ex1:
        return 0
luu_ds_canbo(_path,lst_canbo)


#Hàm xóa cán bộ theo mã cán bộ
def xoa_cb(lst_canbo):
    while True:
        a=input("Nhập mã cán bộ cần xoá: ")
        for cb in lst_canbo:
            if cb['Ma_can_bo']==a:
                vi_tri= lst_canbo.index(cb)
                del(lst_canbo[vi_tri])
                print("Danh sách cán bộ sau khi xoá: ")
                print('{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}'.format('Ma_can_bo','Ten_can_bo',\
         'He_so_luong','Chuc_vu','Phu_cap', 'Luong'))
                for cb in lst_canbo:
                    print('{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}'.format(cb['Ma_can_bo'],\
            cb['Ten_can_bo'], cb['He_so_luong'],cb['Chuc_vu'], cb['Phu_cap'],cb['Luong']))           
        tt=int(input("Bạn có muốn tiếp tục không ? số bất kì: có; 0: không "))
        if tt==0:
            break
    return

#Thêm vào danh sách một cán bộ sao cho vẫn đảm bảo thứ tự sắp xếp

#----Bắt đầu chương trình quản lý cán bộ
print("CHƯƠNG TRÌNH QUẢN LÝ CÁN BỘ:")
while True:
    print("1: Mở file quản lí cán bộ")
    print("2: Thêm thông tin cán bộ")
    print("3: In danh sách cán bộ")
    print("4: Lưu file quản lí cán bộ")
    print("5: Xoá cán bộ theo mã cán bộ")
    print("6: Thoát chương trình")
    chon=int(input('Chọn chức năng cần thực hiện: '))
    if chon==1:
        mo_flie_can_bo(_path,lst_canbo)
    elif chon==2:
        them_tt_canbo(lst_canbo)
    elif chon==3:
        in_ds_canbo(lst_canbo)
    elif chon==4:
        luu_ds_canbo(_path,lst_canbo)
    elif chon==5:
        xoa_cb(lst_canbo)
    elif chon==6:
        break
        
