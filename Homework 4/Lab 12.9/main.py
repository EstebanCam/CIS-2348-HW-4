'''
Esteban Camarillo
ID:1636095
Lab: 12.9
CIS 2348
'''


parts = input().split()
name = parts[0]
ans=""
while name != '-1':
    try:
        age = int(parts[1])+1
    except ValueError:
        age=0
    ans = ans+name+" "+str(age)+"\n"
    parts= input().split()
    name = parts [0]
print(ans[:-1])
