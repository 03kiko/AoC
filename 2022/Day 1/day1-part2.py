def most_cal(input):
    elf_cal=[]
    sum=0
    elf_counter=0
    for x in input:
        if x!='\n':
            sum+=int(x)
        else: 
            elf_counter+=1
            elf_cal+=[[elf_counter,sum]]
            sum=0
    elf_cal=sorted(elf_cal,key=lambda x:x[1],reverse=True)
    total_top_3=0
    for i in range(0,3):
        total_top_3+=elf_cal[i][1]
    return total_top_3
print(most_cal(open('input.txt','r')))