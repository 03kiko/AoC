import re
def day5_function_part1(input):
    def cargo_maker(input):   
        cargo=[]
        for drawing in input:
            if ' 1' in drawing:
                n_stacks=(len(drawing)-3)//4 #-3 is the len of ' \n'
                break
        for i in range(n_stacks):
            cargo.append([])
        input.seek(0)
        for draw in input:
            if ' 1' in draw:
                break
            letters=re.findall('[A-Z]',draw)
            for i in range(len(draw)):
                if draw[i] in letters:
                    cargo[(i-1)//4]+=draw[i]
        for i in range(n_stacks):
            cargo[i].reverse()
        return cargo

    def move_crates(input):
        cargo=cargo_maker(input)
        for line in input:
            if 'move' not in line:
                continue
            moves=re.findall('\d+',line)
            from_stack=int(moves[1])-1
            to_stack=int(moves[2])-1
            cargo[to_stack]+=cargo[from_stack][-int(moves[0]):]
            cargo[from_stack]=cargo[from_stack][:-int(moves[0])]
        return cargo

    final_cargo=move_crates(input)
    answer=''
    for i in range(len(final_cargo)):
        answer+=final_cargo[i][-1]
    return answer
print(day5_function_part1(open('input.txt','r')))