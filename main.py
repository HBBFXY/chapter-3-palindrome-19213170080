num = input("请输入一个5位数字:")
if len(num) != 5 or not num.insight():
  print("错误提示")
else:
  if num == num[::-1]:
    print("是回文数")
