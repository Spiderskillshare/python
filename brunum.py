def passs(bfor):
    fil = open('999.txt', 'a')
    fil.write('\n' + bfor + str(num) )
    fil.close()
a=11
b=101
c=1001
d=10001
e=100001
f=1000001
g=10000001

fil = open('999.txt', 'w')
fil.write("cleared by cyber spider")
fil.close()
for num in range(1,999999):
    if num < a:
        passs('0000001')
        print('.')
    elif num < b:
        passs('000001')
        print('..')
    elif num < c:
        passs('00001')
        print('...')
    elif num < d:
        passs('0000')
        print('....')
    elif num < e:
        passs('000')
        print('.....')
    elif num < f:
        passs('00')
        print('......')
    elif num < g:
        passs('0')
        print('.......')

for num in range(10000000, 99999999):
    print(num)
    fil = open('999.txt', 'a')
    fil.write(str(num)+'\n')
    fil.close()
print('done here"s it\n' )
