import datetime
import time
# n=datetime.datetime.now()#print current date year month time
# print(f"{n:%Y-%m-%d %H:%M}")
# print(n)
#
# import time
# n=print(time.ctime())#print current time
#
# n=print(time.gmtime())#print current time
#
# for i in range(5):
#     time.sleep() #print each element afer a time delay
#     print(i)




import time
# define the countdown func.
# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end="\n")
#         time.sleep(1)
#         t -= 1
#
#     print('Fire in the hole!!')
#
#
# # input time in seconds
# t = input("Enter the time in seconds: ")
#
# # function call
# countdown(int(t))
h=2
m=0
s=h*60
for i in range(s+1):
    if h<10 and m<10:
        print(f'0{h}:0{m}')
    elif h<10 and m>=10:
        print(f'0{h}:{m}')
    elif h>=10 and m<10:
        print(f'{h}:0{m}')
    elif h>=10 and m>=10:
        print(f'{h}:{m}')
    time.sleep(60)#print each element afer a time delay
    if m==0:
        m=60
        h=h-1
    m=m-1












