infinity = 0
# Run the loop till the user doesn't ask for exit
while infinity==0:
    # For storing sudoku elements
    inp_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    inp_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    inp_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    inp_4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    inp_5 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    inp_6 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    inp_7 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    inp_8 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    inp_9 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # For inputting the value
    def inp():
        # Inputting the Value in Sudoku
        for i in range(0,9):
            f=1 # for controlling the user inputs
            for j in range(0,9):
                if j>0:
                    f = int(input("You want to add another value(Yes->1 & No->0)"))
                # If user want's to continue entering the value
                if f==1:
                    # For displaying Sudoku board each time while updating it's value
                    def display():
                        print(f" _______________________\n| {inp_1[0]} {inp_1[1]} {inp_1[2]} | {inp_1[3]} {inp_1[4]} {inp_1[5]} | {inp_1[6]} {inp_1[7]} {inp_1[8]} |\n| {inp_2[0]} {inp_2[1]} {inp_2[2]} | {inp_2[3]} {inp_2[4]} {inp_2[5]} | {inp_2[6]} {inp_2[7]} {inp_2[8]} |\n| {inp_3[0]} {inp_3[1]} {inp_3[2]} | {inp_3[3]} {inp_3[4]} {inp_3[5]} | {inp_3[6]} {inp_3[7]} {inp_3[8]} |\n|-----------------------|\n| {inp_4[0]} {inp_4[1]} {inp_4[2]} | {inp_4[3]} {inp_4[4]} {inp_4[5]} | {inp_4[6]} {inp_4[7]} {inp_4[8]} |\n| {inp_5[0]} {inp_5[1]} {inp_5[2]} | {inp_5[3]} {inp_5[4]} {inp_5[5]} | {inp_5[6]} {inp_5[7]} {inp_5[8]} |\n| {inp_6[0]} {inp_6[1]} {inp_6[2]} | {inp_6[3]} {inp_6[4]} {inp_6[5]} | {inp_6[6]} {inp_6[7]} {inp_6[8]} |\n|-----------------------|\n| {inp_7[0]} {inp_7[1]} {inp_7[2]} | {inp_7[3]} {inp_7[4]} {inp_7[5]} | {inp_7[6]} {inp_7[7]} {inp_7[8]} |\n| {inp_8[0]} {inp_8[1]} {inp_8[2]} | {inp_8[3]} {inp_8[4]} {inp_8[5]} | {inp_8[6]} {inp_8[7]} {inp_8[8]} |\n| {inp_9[0]} {inp_9[1]} {inp_9[2]} | {inp_9[3]} {inp_9[4]} {inp_9[5]} | {inp_9[6]} {inp_9[7]} {inp_9[8]} |\n|_______________________|\n")
                    display()
                    # Choosing the position of input
                    y = int(input("Enter the row number: "))
                    x = int(input("Enter the column number: "))
                # If user doesn't want to continue entering the value
                if f==0:
                    break # It'll go to outer 'if f==0' and then exits from the input loop
                # Inputting value row-wise
                def row_input():
                    if y==1:
                        inp_1[x-1] = int(input("What you want to enter: "))
                        if inp_1[x-1]>9 or inp_1[x-1]<1:
                            print("Wrong Input!")
                            inp_1[x-1] = 0
                    elif y==2:
                        inp_2[x-1] = int(input("What you want to enter: "))
                        if inp_2[x-1]>9 or inp_2[x-1]<1:
                            print("Wrong Input!")
                            inp_2[x-1] = 0
                    elif y==3:
                        inp_3[x-1] = int(input("What you want to enter: "))
                        if inp_3[x-1]>9 or inp_1[x-1]<1:
                            print("Wrong Input!")
                            inp_3[x-1] = 0
                    elif y==4:
                        inp_4[x-1] = int(input("What you want to enter: "))
                        if inp_4[x-1]>9 or inp_1[x-1]<1:
                            print("Wrong Input!")
                            inp_4[x-1] = 0
                    elif y==5:
                        inp_5[x-1] = int(input("What you want to enter: "))
                        if inp_5[x-1]>9 or inp_1[x-1]<1:
                            print("Wrong Input!")
                            inp_5[x-1] = 0
                    elif y==6:
                        inp_6[x-1] = int(input("What you want to enter: "))
                        if inp_6[x-1]>9 or inp_1[x-1]<1:
                            print("Wrong Input!")
                            inp_6[x-1] = 0
                    elif y==7:
                        inp_7[x-1] = int(input("What you want to enter: "))
                        if inp_7[x-1]>9 or inp_1[x-1]<1:
                            print("Wrong Input!")
                            inp_7[x-1] = 0
                    elif y==8:
                        inp_8[x-1] = int(input("What you want to enter: "))
                        if inp_8[x-1]>9 or inp_1[x-1]<1:
                            print("Wrong Input!")
                            inp_8[x-1] = 0
                    elif y==9:
                        inp_9[x-1] = int(input("What you want to enter: "))
                        if inp_9[x-1]>9 or inp_1[x-1]<1:
                            print("Wrong Input!")
                            inp_9[x-1] = 0
                    else:
                        print("Row number is wrong, Check once again!")
                # For choosing the correct column to input the value
                if x==1:
                    row_input()
                elif x==2:
                    row_input()
                elif x==3:
                    row_input()
                elif x==4:
                    row_input()
                elif x==5:
                    row_input()
                elif x==6:
                    row_input()
                elif x==7:
                    row_input()
                elif x==8:
                    row_input()
                elif x==9:
                    row_input()
                else:
                    print("Column number is Wrong, Check once again!")
            if f==0:
                break

    inp()
    inputs = [inp_1, inp_2, inp_3, inp_4, inp_5, inp_6, inp_7, inp_8, inp_9]
    
    # Checking for duplicate items                    
    def duplicate():
        # Checking for duplication
        # Checking for Rows
        for i in range(0,9):
            for j in range(0,9):
                if i==0:
                    for k in range(0,9):
                        if inp_1[j] == inp_1[k]:
                            print(f"Duplicate num in row detected at ---> ({j+1}, {k+1}) & ({j+1}, {i+1})")
                elif i==1:
                    for k in range(0,9):
                        if inp_2[j] == inp_2[k]:
                            print(f"Duplicate num in row detected at ---> ({j+1}, {k+1}) & ({j+1}, {i+1})")
                elif i==2:
                    for k in range(0,9):
                        if inp_3[j] == inp_2[k]:
                            print(f"Duplicate num in row detected at ---> ({j+1}, {k+1}) & ({j+1}, {i+1})")
                elif i==3:
                    for k in range(0,9):
                        if inp_4[j] == inp_2[k]:
                            print(f"Duplicate num in row detected at ---> ({j+1}, {k+1}) & ({j+1}, {i+1})")
                elif i==4:
                    for k in range(0,9):
                        if inp_5[j] == inp_2[k]:
                            print(f"Duplicate num in row detected at ---> ({j+1}, {k+1}) & ({j+1}, {i+1})")
                elif i==5:
                    for k in range(0,9):
                        if inp_6[j] == inp_2[k]:
                            print(f"Duplicate num in row detected at ---> ({j+1}, {k+1}) & ({j+1}, {i+1})")
                elif i==6:
                    for k in range(0,9):
                        if inp_7[j] == inp_2[k]:
                            print(f"Duplicate num in row detected at ---> ({j+1}, {k+1}) & ({j+1}, {i+1})")
                elif i==7:
                    for k in range(0,9):
                        if inp_8[j] == inp_2[k]:
                            print(f"Duplicate num in row detected at ---> ({j+1}, {k+1}) & ({j+1}, {i+1})")
                elif i==8:
                    for k in range(0,9):
                        if inp_9[j] == inp_2[k]:
                            print(f"Duplicate num in row detected at ---> ({j+1}, {k+1}) & ({j+1}, {i+1})")
                else:
                    pass

        # Checking for column
        for i in range(0,9):
            for j in range(0,9):
                if i==0:
                    for k in range(0,9):
                        if inputs[j][i] == inputs[k][i]:
                            print(f"Duplicate num in column detected at ---> ({j+1}, {i+1}) & ({k+1}, {i+1})")
                elif i==1:
                    for k in range(0,9):
                        if inputs[j][i] == inputs[k][i]:
                            print(f"Duplicate num in column detected at ---> ({j+1}, {i+1}) & ({k+1}, {i+1})")
                elif i==2:
                    for k in range(0,9):
                        if inputs[j][i] == inputs[k][i]:
                            print(f"Duplicate num in column detected at ---> ({j+1}, {i+1}) & ({k+1}, {i+1})")
                elif i==3:
                    for k in range(0,9):
                        if inputs[j][i] == inputs[k][i]:
                            print(f"Duplicate num in column detected at ---> ({j+1}, {i+1}) & ({k+1}, {i+1})")
                elif i==4:
                    for k in range(0,9):
                        if inputs[j][i] == inputs[k][i]:
                            print(f"Duplicate num in column detected at ---> ({j+1}, {i+1}) & ({k+1}, {i+1})")
                elif i==5:
                    for k in range(0,9):
                        if inputs[j][i] == inputs[k][i]:
                            print(f"Duplicate num in column detected at ---> ({j+1}, {i+1}) & ({k+1}, {i+1})")
                elif i==6:
                    for k in range(0,9):
                        if inputs[j][i] == inputs[k][i]:
                            print(f"Duplicate num in column detected at ---> ({j+1}, {i+1}) & ({k+1}, {i+1})")
                elif i==7:
                    for k in range(0,9):
                        if inputs[j][i] == inputs[k][i]:
                            print(f"Duplicate num in column detected at ---> ({j+1}, {i+1}) & ({k+1}, {i+1})")
                elif i==8:
                    for k in range(0,9):
                        if inputs[j][i] == inputs[k][i]:
                            print(f"Duplicate num in column detected at ---> ({j+1}, {i+1}) & ({k+1}, {i+1})")
                else:
                    pass

        # Checking in Section
        # For Section 1, 4 & 7
        for i in range(0,3):
            # Section 1
            for j in range(0,3):
                for k in range(0,3):
                    if inputs[i][j] == inputs[i][k]:
                        print(f"Duplicate  num in section-1 detected at ---> ({i+1}, {j+1}) & ({i+1}, {k+1})")
            # Section 4
            for j in range(3,6):
                for k in range(3,6):
                    if inputs[i][j] == inputs[i][k]:
                        print(f"Duplicate  num in section-4 detected at ---> ({i+1}, {j+1}) & ({i+1}, {k+1})")
            # Section 7
            for j in range(6,9):
                for k in range(6,9):
                    if inputs[i][j] == inputs[i][k]:
                        print(f"Duplicate  num in section-7 detected at ---> ({i+1}, {j+1}) & ({i+1}, {k+1})")
        
        # For section 2, 5, 8
        for i in range(3,6):
            # Section 2
            for j in range(0,3):
                for k in range(0,3):
                    if inputs[i][j] == inputs[i][k]:
                        print(f"Duplicate  num in section-2 detected at ---> ({i+1}, {j+1}) & ({i+1}, {k+1})")
            # Section 5
            for j in range(3,6):
                for k in range(3,6):
                    if inputs[i][j] == inputs[i][k]:
                        print(f"Duplicate  num in section-5 detected at ---> ({i+1}, {j+1}) & ({i+1}, {k+1})")
            # Section 8
            for j in range(6,9):
                for k in range(6,9):
                    if inputs[i][j] == inputs[i][k]:
                        print(f"Duplicate  num in section-8 detected at ---> ({i+1}, {j+1}) & ({i+1}, {k+1})")
                        
        # For section 3, 6, 9
        for i in range(6,9):
            # Section 3
            for j in range(0,3):
                for k in range(0,3):
                    if inputs[i][j] == inputs[i][k]:
                        print(f"Duplicate  num in section-3 detected at ---> ({i+1}, {j+1}) & ({i+1}, {k+1})")
            # Section 6
            for j in range(3,6):
                for k in range(3,6):
                    if inputs[i][j] == inputs[i][k]:
                        print(f"Duplicate  num in section-6 detected at ---> ({i+1}, {j+1}) & ({i+1}, {k+1})")
            # Section 9
            for j in range(6,9):
                for k in range(6,9):
                    if inputs[i][j] == inputs[i][k]:
                        print(f"Duplicate  num in section-9 detected at ---> ({i+1}, {j+1}) & ({i+1}, {k+1})")

    checks = int(input("Want to check for duplicates!(Yes->1 & No->0)"))
    # If user want's to check it's mistake
    if checks==1:
        duplicate()
    cont = int(input("Want to continue Entering Values!(Yes->1 & No->0)"))
    # If user again wants to entering value
    if cont==0:
        break