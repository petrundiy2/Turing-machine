inp = open('rules', 'r')
line = input()
state = [0]*24
hyate = [0]*24
bone = [0]*24
btwo = [0]*24
kuda = [0]*24
for i in range(24):
    s=inp.readline()
    A = s.split(' ')
    bone[i] = A[0]
    state[i] = A[1]
    btwo[i] = A[3]
    hyate[i] = A[4]
    kuda[i] = A[5]
sost='q1'
kek=[0]*len(line)

for j in range(5):
    if (sost=='q1') or (sost=='q2') or (sost=='q3') or (sost=='q4') or (sost=='q5'):
        for i in range(24):
            if bone[i]==line[j] and state[i]==sost:
                lum = i
                if btwo[lum]=='*':
                    kek[j]=' '
                else:
                    kek[j]=btwo[lum]


                sost = hyate[lum]
                break

    elif sost=='no':
        print(kek)
        break
print(kek)
