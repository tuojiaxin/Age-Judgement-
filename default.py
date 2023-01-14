from datetime import datetime
# 获取当前年份(now_year)
now_year = datetime.now().year
# 获取当前月份(now_month)
now_month = datetime.now().month
# 获取当前日期(now_day)
now_day = datetime.now().day

# 定义平闰判断函数(leap_year)
def leap_year(i):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        return True
    else:
        return False

# 闰年每个月天数
days_leap = (366, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# 平年每个月天数
days_common = (365, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

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
if leap_year(birth_year) is True:
    month_days = days_leap[birth_month]
else:
    month_days = days_common[birth_month]
# 获取用户出生日期(birth_day)
birth_day = int(input("你的出生日期："))
# 判断输入日期是否合规
while birth_day > month_days or birth_day < 1:
    print("你确定输入的日期正确？")
    # 重新获取用户出生日期(birth_day)
    birth_day = int(input("请重新输入你的出生日期："))

# 判定输入日期为过去
if now_year > birth_year or\
        now_year == birth_year and now_month > birth_month or\
        now_year == birth_year and now_month == birth_month and now_day >= birth_day:
    # 计算自出生到现在的年数、月数、日数
    age_year = now_year - birth_year
    age_month = now_month - birth_month
    age_day = now_day - birth_day
    if age_month < 0:
        age_year = age_year - 1
        age_month = age_month + 12
    if age_day < 0:
        age_month = age_month - 1
        age_day = age_day + month_days
    # 计算出生距今天数
    days_year = 0
    days_month = 0
    for the_year in range(birth_year + 1, now_year):
        if leap_year(the_year) is True:
            days_year = days_year + days_leap[0]
        else:
            days_year = days_year + days_common[0]
    if now_month >= birth_month:
        for the_month in range(birth_month + 1, now_month):
            if leap_year(birth_year) is True:
                days_month = days_month + days_leap[the_month]
            else:
                days_month = days_month + days_common[the_month]
    else:
        for the_month in range(1, now_month) or range(birth_month + 1, 13):
            if leap_year(birth_year) is True:
                days_month = days_month + days_leap[the_month]
            else:
                days_month = days_month + days_common[the_month]
    days = days_year + days_month + age_day
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
在这个世界生活了{age_year}年{age_month}个月{age_day}天（{days}天）
{massage}''')
    # 生日彩蛋
    if age_month == 0 and age_day == 0:
        print(f'''
今天正好是你的{age_year}岁生日呐
祝你生日快乐哦^o^''')
# 判定输入时间为未来
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
    # 计算出生距今天数
    days_year = 0
    days_month = 0
    for the_year in range(now_year + 1, birth_year):
        if leap_year(the_year) is True:
            days_year = days_year + days_leap[0]
        else:
            days_year = days_year + days_common[0]
    if birth_month >= now_month:
        for the_month in range(now_month + 1, birth_month):
            if leap_year(birth_year) is True:
                days_month = days_month + days_leap[the_month]
            else:
                days_month = days_month + days_common[the_month]
    else:
        for the_month in range(1, birth_month) or range(now_month + 1, 13):
            if leap_year(birth_year) is True:
                days_month = days_month + days_leap[the_month]
            else:
                days_month = days_month + days_common[the_month]
    days = days_year + days_month + age_day
    # 输出信息
    print(f'''
暂时还没出生呐
你将会在{birth_year}年{birth_month}月{birth_day}号出生
还有{age_year}年{age_month}个月{age_day}天（{days}天）就会降临世界''')

# 2023.1.14
# 增加详细天数计算
# 修复bug:当输入年份月份和当前年份月份相同时，日数进位出错
