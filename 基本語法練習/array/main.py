import numpy as np

if __name__ == '__main__':
    x=1
    col=3
    row=0
    number_array=np.zeros([7,7])
    for i in range(49):
        number_array[row][col]=x
        x=x+1
        if x%7==1:
            row=(row+1)%7
        else:
            col=(col+1)%7
            row=(row-1)%7

    for i in range(7):
        for j in range(7):
            print('%3d' % number_array[i][j],end='|')
        print()
        print("－－－－－－－－－－－－－－－－")