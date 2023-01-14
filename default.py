from datetime import datetime
# 获取当前年份(now_year)
now_year = datetime.now().year
# 获取当前月份(now_month)
now_month = datetime.now().month
# 获取当前日期(now_day)
now_day = datetime.now().day

# 定义平闰判断函数(leap_year)
def leap_year(i):
    rem_4 = i % 4
    rem_100 = i % 100
    rem_400 = i % 400
    if rem_4 == 0 and rem_100 != 0 or rem_400 == 0:
        return True
    else:
        return False

print("请在下方输入")
# 获取用户出生年份(birth_year)
birth_year = int(input("你的出生年份："))

# 获取用户出生月份(birth_month)
birth_month = int(input("你的出生月份："))
# 判断输入月份是否合规
while birth_month not in range(1, 13):
    print("你确定输入的月份正确?")
    # 重新获取用户出生月份(birth_month)
    birth_month = int(input("请重新输入你的出生月份："))

# 计算用户出生月天数(month_days)
if birth_month in (4, 6, 9, 11):
    month_days = 30
elif birth_month == 2:
    if leap_year is True:
        month_days = 29
    else:
        month_days = 28
else:
    month_days = 31

# 获取用户出生日期(birth_day)
birth_day = int(input("你的出生日期："))
# 判断输入日期是否合规
while birth_day > month_days or birth_day < 1:
    print("你确定输入的日期正确？")
    # 重新获取用户出生日期(birth_day)
    birth_day = int(input("请重新输入你的出生日期："))

if now_year >= birth_year:
    # 计算自出生到现在的时间
    age_year = now_year - birth_year
    age_month = now_month - birth_month
    age_day = now_day - birth_day
    if age_month < 0:
        age_year = age_year - 1
        age_month = age_month + 12
    if age_day < 0:
        age_month = age_month - 1
        age_day = age_day + month_days

    # 判断用户的年龄阶段
    if age_year > 120:
        massage = "恭喜您修仙成功"
    elif age_year >= 18:
        massage = "已经是成年人了"
    else:
        massage = "还是未成年人呢"
    # 输出信息
    print(f'''
你出生于{birth_year}年{birth_month}月{birth_day}号
在这个世界生活了{age_year}年{age_month}个月{age_day}天
{massage}''')
    # 生日彩蛋
    if age_month == 0 and age_day == 0:
        print(f'''
今天正好是你的{age_year}岁生日呐
祝你生日快乐哦^o^''')
else:
    # 计算自出生到现在的时间
    age_year = birth_year - now_year
    age_month = birth_month - now_month
    age_day = birth_day - now_day
    if age_month < 0:
        age_year = age_year - 1
        age_month = age_month + 12
    if age_day < 0:
        age_month = age_month - 1
        age_day = age_day + month_days
    # 输出信息
    print(f'''
暂时还没出生呐
你将会在{birth_year}年{birth_month}月{birth_day}号出生
还有{age_year}年{age_month}个月{age_day}天就会降临世界''')

# 2023.1.13
# 增加生日彩蛋
# 自定义平闰年判断函数
