with open('F:/sumanth/Python-Code/Python Section1/file.txt') as file:
    line_number = 1
    for line in file:
        print('{}:{}'.format(line_number,line.rstrip()))
        line_number += 1