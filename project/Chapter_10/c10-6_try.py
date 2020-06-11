while True:
    first_num = input("请输入第一个数字：")
    second_num = input("请输入第二个数字：")
    try:
        sum_num = int(first_num) + int(second_num)
        print(sum_num)
    except ValueError:
        print("此算术只能计算数字")