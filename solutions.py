# Задача от Яндекса №1
'''
a = str(input())
b = str(input())

data1 = [int(x) for x in a.split()]
data2 = [int(x) for x in b.split()]

sec_minute = 60
sec_hour = 60 * sec_minute
sec_day = 24 * sec_hour
year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sec_year = 365 * sec_day

def SEC(data):
    month = int(data[1])
    SEC_YEAR = data[0] * sec_year
    SEC_MOUNTH = sum(year[0:month-1]) * sec_day
    SEC_DAY = data[2] * sec_day
    SEC_HOUR = data[3] * sec_hour
    SEC_MINUTE = data[4] * sec_minute
    SEC_SEC = data[5]

    SEC_SUM = SEC_YEAR + SEC_MOUNTH + SEC_DAY + SEC_HOUR + SEC_MINUTE + SEC_SEC
    return SEC_SUM


day = (SEC(data2) - SEC(data1)) // sec_day
sec = (SEC(data2) - SEC(data1)) % sec_day
print(day, sec)

# print((SEC(data2)//sec_day) - (SEC(data1)//sec_day))
# print(sec_live, day)
#

# Введите дату начала   980 2 12 10 30 1            1001 5 20 14 15 16
# Введите дату конца    980 3 1 10 31 37            9009 9 11 12 21 11
#                       дней  17 секунд  96         дней  2923033 секунд  75955
'''

# Задача от Яндекса №2
'''
a = str(input())
b = str(input())
c = str(input())

NMQ = [int(x) for x in a.split()]
N_A = [int(x) for x in b.split()]
M_B = [int(x) for x in c.split()]

                                    # проверка повторяющихся элементов в списке
def Tree(n):
    c = []
    for i in n:
        if n.count(i) > 1:
            c.append(i)
    return list(set(c))

iter = 0

while iter != NMQ[2]+1:

    q = str(input())
    Q = [x for x in q.split()]

    if Q[1] == 'A':

        if int(Q[0]) == 1:
            N_A.append(int(Q[2]))
        elif int(Q[0]) == -1:
            N_A.remove(int(Q[2]))
    else:
        if int(Q[0]) == 1:
            M_B.append(int(Q[2]))
        else:
            M_B.remove(int(Q[2]))

    print(len((list(set(N_A) ^ set(M_B))) + (Tree(N_A) + Tree(M_B))), end=' ')

    iter += 1

# 2 5 10
# 1 2
# 1 2 3 4 5
# 1 A 3
# 1 A 4
# 1 A 5
# 1 A 6
# 1 A 7
# -1 A 1
# 1 B 7
# -1 A 6
# -1 B 1
# 1 A 7
'''

# Задача от Яндекса №3
