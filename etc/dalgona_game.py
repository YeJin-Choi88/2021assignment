n = int(input("정수를 입력하시오 : "))
a = []    # 빈 리스트 생성
a_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(n):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(n):
        line.append('*')     # 안쪽 리스트에 0 추가
    a.append(line)         # 전체 리스트에 안쪽 리스트를 추가
m = 0
while(True):
    num_list = list(map(str, input().split()))
    if(len(num_list)>1):
        x1 = int(num_list[0])
        y1 = int(num_list[1])
        x2 = int(num_list[2])
        y2 = int(num_list[3])

        for i in range(x2-x1+1):
            for j in range(y2-y1+1):
                a[x1+i][y1+j]='0'
    elif(len(num_list)==1):
        x1 = num_list[0]

    
    if(x1 == 'E'):
        for i in range(n):
            for j in range(n):
                if a[i][j]=='0':
                    a[i][j]=a_list[m-1] 
        break
    m += 1   
    num_list = []



for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print("") 
