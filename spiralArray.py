# The following code Prints the spiral order of a nxm array

def spiralArr(arr, b):
    i = 0
    while(i<b):
        if i==0:
            for _ in range(b):
                print(arr[i], end=' ')
                del arr[i]
        else:
            print(arr[b-1],end=' ')
            del arr[b-1]
            print(arr[(2*b)-2],end=' ')
            del arr[(2*b)-2]
        i += 1




if __name__=='__main__':
    a:str = input("Enter the number of rows:")
    b:str = input("Enter the number of columns:")
    arr = []
    main_list = []
    try:
        a = int(a)
        b = int(b)
    except Exception as e:
        print(e)

    for i in range(a):
        li = []
        for j in range(b):
            li.append(input(f"Enter {i},{j} th element:"))
        arr.append(li)
    for i in range(a):
        for j in  range(b):
            main_list.append(arr[i][j])
            print(f'{arr[i][j]} ', end='')
        print('')

    spiralArr(main_list, b)