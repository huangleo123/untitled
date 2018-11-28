#2.3.1修改字符串的大小写
#2.3.2拼接字符串
#2.3.3使用制表符或者换行符添加空白
#2.3.4删除空白
#2.3.5使用字符串的时候避免语法错误 注意使用单双引号来区分引用加引用
##########2.3.1##################
message = "This is a string"
print(message.title())  #首字母大写
print(message.upper())  #字符串全小写
print(message.lower())  #字符串全大小

###########2.3.2##################
message_a = "a"
message_b = "b"
print(message_a+message_b)

###########2.3.3##################
#输入转义字符使得输出更美观
#################################
name ="李先生"
content = "此致"
content_1 = "敬礼"
print(name+content+content_1)
print(name+"\n"+"\t"+content+"\n"+content_1)

###########2.3.3##################
#删除字符串中的空白，相当于整理输入
#string.lstrip() 左删除空白
#string.rstrip() 右边
#string.strip() 左右删除空白
#################################
head_null_string = " 开头是一个空白"
end_null_sting = "结尾是一个空白 "
half_null_string = "中间是一个 空白"
all_null_string = " 全 是 空 白 的 字 符 串 "
print(head_null_string)
print(head_null_string.lstrip())
print("\\\\\\\\\\\\\\\\")
print(end_null_sting)
print(end_null_sting.rstrip())
print("\\\\\\\\\\\\\\\\")
print(all_null_string)
print(all_null_string.strip())
