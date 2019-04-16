from turtle import *
from datetime import datetime

def run(n):
    if n%4: return 0
    if not n%1000: return 1
    if not n%100: return 0
    return 1

def wa():
    pass

def prpr(year,month,day):
    if month>12 or month<1: return 'code_2'
    ans = 166
    if run(year): L = [31,29,31,30,31,30,31,31,30,31,30,31]
    else: L = [31,28,31,30,31,30,31,31,30,31,30,31]
    while year > 2019:
        ans += (356+run(year))
        year -= 1
    for i in range(1,month):
        ans += L[i-1]
    ans += day
    return ans

def this_year_dec(n):
    return n+135

def main():
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    if year == 2018: s = this_year_dec(day)
    else: s = prpr(year,month,day)
    if month == 7 and day == 18:
        return('周年纪念日！！')
    return('今天是第%d天了，太太爱你哟( *￣▽￣)((≧︶≦*)' % s)

print('')
p = main()
print(p)
print('\n\n\n')
print('≧▽≦*o'*5)
print('≧▽≦*o'*5)
print('≧▽≦*o'*5)

reset()
speed('fast')
IN_TIMES = 40
TIMES = 20
for i in range(TIMES):
    right(360/TIMES)
    forward(200/TIMES)
    for j in range(IN_TIMES):
        right(360/IN_TIMES)
        forward(400/IN_TIMES)
up()
goto(-50,0)
down()
write("\n%s\n\n\n" % p, font = ("Courier", 12, "bold"))
s = Screen()
s.exitonclick()
