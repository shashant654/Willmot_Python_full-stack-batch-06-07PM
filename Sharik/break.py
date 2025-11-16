# break statement:-
# continue statement:-

# break and continue statemnt are known as jump statement.

# for i in range(6):
#   print(i)


# for i in range(0,6):  # 0,1,2,3,4,5
#                     print(i)

# for i in range(0,6, 1):
#                     print(i)


# by default GAP is 1 (N- 1 )  => 1-1 = 0 , it skips 0 elemnt.
# first parameter => starting point , by deafult = 0
# second parameter => ending point , excluded
# third parameter => gap


# break statement :-
# => it is used to exit from a loop when, the applied condition wll be true.

# => it stops the execution completly , when the applied condition will be perfectly mathced.

# for i in range(0,9):            
#                     if i == 6:
#                        break
#                     print(i)                    
                    


# for i in range(10):
#                     if i == 7:
#                        break
#                     print(i)

# continue statement : -

# => it skips the current iteration and move to next iteration.


# for i in range(0,13):
#                     if i == 8:
#                        continue
#                     print(i)


# for i in range(0,20,2):
#                     print(i)

                    
# first parament = starting point => 0
# second paramenter = ending point => 20 , excluded
# third parameter = Gap (N-1) , 2 , ( 2 - 1 => 1), it skips 1 element

# 0,2,4,6,8,10,12,14,15,17,19

                                        


# for i in range(0,20,2):
#                     if i == 14:
#                        continue            
#                     print(i)


for i in range(0,20,2):
                    if i == 14:
                       break            
                    print(i)
                    
