def main():
    num_str = input("")
    if len(num_str) != 5 or not num_str.isdigit():
        print("输入错误: 请输入5位数字")
        return
    if num_str == num_str[::-1]:
        print("是回文数")
    else:
        print("不是回文数")


if __name__ == "__main__":
    main()
