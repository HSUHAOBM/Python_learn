# 統一編號驗證
def company_vat_checker(serial):
    # 檢查長度 及 是否有非數字
    if len(serial) != 8 or not serial.isdigit():
        return False

    # Step1 統編每位數乘以一個固定數字固定值 ,乘以 [1,2,1,2,1,2,4,1]
    # Step2 所得值取出十位數及個位數,並將十位數與個位數全部結果值加總,如果統編第七碼為7 值輸出為0
    # ex 04595257
    #   0   4   5   9   5   2   5   7
    # x 1   2   1   2   1   2   4   1
    # ================================
    #   0   8   5   1   5   4   2   7   個 位
    #               8           0       十 位
    #   0   8   5   9   5   4   2   7   個 + 十
    #   0 + 8 + 5 + 9 + 5 + 4 + 2 + 7 = 40 % 5 =0

    # ex 10458570
    #   1   0   4   5   8   5   7   0
    # x 1   2   1   2   1   2   4   1
    # ================================
    #   1   0   4   1   8   1   2   0   個 位
    #               0       0   8       十 位
    #   1   0   4   1   8   1   0   0   個 + 十 （個位）
    #   0   0   0   0   0   0   1   0   個 + 十 （十位）
    #   加總 第七位 分別取 0 or 1
    #   1 + 0 + 4 + 1 + 8 + 1 + 1 + 0 = 16 % 5 =1
    #   1 + 0 + 4 + 1 + 8 + 1 + 0 + 0 = 15 % 5 =0

    serial_list = list(serial)
    coeff = [1, 2, 1, 2, 1, 2, 4, 1]

    # Define a list with 8 zeros
    multiple = [0] * 8

    count = 0
    while count < 8:
        temp = int(serial_list[count]) * coeff[count]
        # 判斷第七位數 如果為7 值 = 0
        if(int(serial_list[count]) == 7 and count == 6):
            multiple[count] = 0
        else:
            multiple[count] = temp if temp < 10 else (temp // 10) + (temp % 10)
        count = count + 1
    total = sum(multiple)

    # Step3 判斷結果
    # 第一種:加總取5的餘數為0
    # 第二種:加總取5的餘數不為0 檢查統編的第6碼為7 加總值+1取5的餘數為0
    # 第三種:不符合以上規則
    if (total % 5 == 0):
        return True
    elif ((total + 1) % 5 == 0 and serial[6] == '7'):
        return True
    else:
        return False

if __name__=='__main__':
    # 位數不足
    print (company_vat_checker('5312539'))   # false
    # 符合
    print (company_vat_checker('53212539'))  # true
    print (company_vat_checker('04595257'))  # true
    print (company_vat_checker('04595252'))  # true
    print (company_vat_checker('61194605'))  # true
    print (company_vat_checker('82554400'))  # true
    print (company_vat_checker('38965019'))  # true
    print (company_vat_checker('82551213'))  # true
    print (company_vat_checker('17713903'))  # true
    print (company_vat_checker('61432901'))  # true
    # 符合 且第 7碼 = 7
    print (company_vat_checker('10458570'))  # true
    print (company_vat_checker('10458574'))  # true
    print (company_vat_checker('10458575'))  # true
    print (company_vat_checker('99381678'))  # true
    print (company_vat_checker('72373274'))  # true
    print (company_vat_checker('14605472'))  # true
    # 不符合
    print (company_vat_checker('12222539')) # false