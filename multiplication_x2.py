inp = open('rules2', 'r')
line = input()
state_old = [0]*9
state_new = [0]*9
bone = [0]*9
btwo = [0]*9
kuda = [0]*9
for i in range(9):
    s=inp.readline()
    A = s.split(' ')
    bone[i] = A[0]
    state_old[i] = A[1]
    btwo[i] = A[3]
    state_new[i] = A[4]
    kuda[i] = A[5]
sost='q1'
kek=[0]*(len(line)+1)
for j in range(len(line)):
    for i in range(3):
        if bone[i]==line[j] and state_old[i]==sost:
            lum = i
            kek[j+1]=btwo[lum]
            sost = state_new[lum]
kek[0]='*'
kek.pop()

k=len(kek)

while k!=0:
    for i in range(9):
        if bone[i]==kek[k-1] and state_old[i]==sost:
            kek[k-1]=btwo[i]
            sost = state_new[i]
            k-=1
print(kek)
