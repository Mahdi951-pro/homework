'''             NAME: Abid Al Mahdi
                ROLL: 148                                             '''


#1*2+3*4+5*6+.........+47*48

a=1
s=0
n=97
while a<=n:
    s=s+a*(a+1)
    a=a+2
print(s);


#2,up2+4,up2+6,up2+.........+80,up2

i=1
s=0
n=80
while i<=n:
    s=s+a*i+i
    i=i+2
print(s);


#2,up2+4,up2+6,up2+.........+n,up2

a=1
s=0
n=int(input());
while a<=n:
    s=s+a*(a+1)
    a=a+2
print(s);


#2,up10+4,up10+6,up10+.........+n,up10

a=1
s=0
n=int(input());
while a<=n:
    s=s+pow(a,10)
    a=a+2
print(s);


#(2*1),up3+(4*2),up3+(8*3),up3+.............+(32*5),up3

a=2
s=0
h=32
b=1
while a<=n:
    s=s+(a*b)+(a*b)*(a+b)
    a=a*2
    b=b+1
print(s);