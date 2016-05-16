inp = open('rules2', 'r')
line = input()
state_old = [0]*10
state_new = [0]*10
bone = [0]*10
btwo = [0]*10
kuda = [0]*10
for i in range(10):
    s=inp.readline()
    A = s.split(' ')
    bone[i] = A[0]
    state_old[i] = A[1]
    btwo[i] = A[3]
    state_new[i] = A[4]
    kuda[i] = A[5]
sost='q1'
kek=[0]*len(line)
for i in range(len(line)):
    kek[i]=line[i]

j=0
while sost!='no':
    for i in range(10):
        if kek[j]==bone[i] and sost==state_old[i]:
            kek[j]=btwo[i]
            sost=state_new[i]
            if kuda[i]=='R':
                j+=1
            else:
                j-=1
print(kek)
