def start_of_packet_marker_detecter(input):
    previous_chars=[]
    while True:
        char=input.read(1)
        previous_chars.append(char)
        if len(previous_chars)>=14:
            i=0
            for char in previous_chars[-14:]:
                if char in previous_chars[-13+i:]:
                    break
                else:
                    i+=1
                    if i==13:
                        return len(previous_chars)
        if not char:
            break
        

print(start_of_packet_marker_detecter(open('input.txt','r')))