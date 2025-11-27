print("*")         #OUTPUT:- *


n=int(input("Enter the number:"))
print("* "*n)                # #OUTPUT:- * * * * * * * * * * 


n=int(input("Enter the number:"))
for i in range(n):                  #OUTPUT:-        *
    print("*")                      #                *
                                    #                *
                                    #                *
                                    #                *
                                    #                *
                                    #                *
                                    #                *
                                    #                *
                                    #                *
   


n=int(input("Enter the number:"))
for i in range(n):
    print("*",end=" ")            #OUTPUT:- * * * * * * * * * *


n=int(input("Enter the number:")) #OUTPUT:-* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
for i in range(n):                 #        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    for j in range(n):
        print("*",end=" ")

                                  

n=int(input("Enter the number:"))     #OUTPUT:-*
for i in range(n):                          # *
    for j in range(n):                      # *
        print("*")                          # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                            # *
                                           

n=int(input("Enter the number:"))
for i in range(n):                           
    for j in range(n):
        print("*",end=" ")
    print()
# OUTPUT:-  * * * * * * * * * * 
        # * * * * * * * * * *
        # * * * * * * * * * *
        # * * * * * * * * * *
        # * * * * * * * * * *
        # * * * * * * * * * * 
        # * * * * * * * * * *
        # * * * * * * * * * *
        # * * * * * * * * * *
        # * * * * * * * * * *

n=int(input("Enter the number:"))       #kyuki sabhi me rows(i) same h but sabhi colum(j) me i+1 ke barabar * h 
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
# OUTPUT:- 
# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * * 
    
n=int(input("Enter the number:"))        
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

# OUTPUT:l- 
# * * * * * * * * * * 
# * * * * * * * * *
# * * * * * * * *
# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
    
n=int(input("Enter the number:"))   
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
# OUTPUT:- 
#                     * 
#                   * *
#                 * * *
#               * * * *
#             * * * * *
#           * * * * * *
#         * * * * * * *
#       * * * * * * * * 
#     * * * * * * * * *
#   * * * * * * * * * *


n=int(input("Enter the number:"))   
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range (i,n):
        print("*",end=" ")
    print()
# OUTPUT:- 
#   * * * * * * * * * * 
#     * * * * * * * * *
#       * * * * * * * *
#         * * * * * * *
#           * * * * * *
#             * * * * *
#               * * * *
#                 * * *
#                   * *
#                     * 
    

rows = 10
for i in range(1, rows):
    for j in range(1,rows):  
        print("*",end=" ")
    print(" ") # New line ke liye

# OUTPUT:-
# * * * * * * * * *  
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *  
# * * * * * * * * *

rows = 10
for i in range(1, rows):
    for j in range(i):  
        print("*",end=" ")
    print(" ") # New line ke liye
    
# OUTPUT:-
# *  
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *


rows = 10
for i in range(rows,0,-1):
    for j in range(i):  
        print("*",end=" ")
    print(" ") # New line ke liye

# OUTPUT:-
# * * * * * * * * * *  
# * * * * * * * * *
# * * * * * * * *
# * * * * * * *
# * * * * * *  
# * * * * *
# * * * *
# * * *
# * *
# *


n=int(input("Enter the number:"))   
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):            #ISME SE +1 HATANE PER PIRAMID BAN JAYEGA
        print("*",end=" ")            
        
    for j in range(i+1):
        print("*",end=" ")
    print()
# OUTPUT:-
#                     * * 
#                   * * * *
#                 * * * * * *
#               * * * * * * * *                  # JISME BICH WALA 1 LINE JYADA H ISKE JUST UPER KA COMMENT 
#             * * * * * * * * * * 
#           * * * * * * * * * * * *
#         * * * * * * * * * * * * * *
#       * * * * * * * * * * * * * * * * 
#     * * * * * * * * * * * * * * * * * *
#   * * * * * * * * * * * * * * * * * * * * 


n=int(input("Enter the number:"))   
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
        
    for j in range(i+1):
        print("*",end=" ")
    print()
# OUTPUT:- 
#                     * 
#                   * * *
#                 * * * * *
#               * * * * * * *
#             * * * * * * * * *              #YE 1,3,5,7.....WISH PIRAMID H
#           * * * * * * * * * * *
#         * * * * * * * * * * * * *
#       * * * * * * * * * * * * * * * 
#     * * * * * * * * * * * * * * * * *
#   * * * * * * * * * * * * * * * * * * *


n=int(input("Enter the number:"))   
for i in range(n):
    for j in range(i,n):           #YE 1 ,2, 3 .. WISH PIRAMID H 
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
# OUTPUT:- 
#           * 
#          * *
#         * * *
#        * * * *
#       * * * * *
#      * * * * * *
#     * * * * * * *
#    * * * * * * * *
#   * * * * * * * * * 

         
n=int(input("Enter the number:"))   
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range (i,n):         # yaha n-1 karne per pick point mil jayega 
        print("*",end=" ")
        
    for j in range(i,n):
        print("*",end=" ")
    print()
# OUTPUT:-
#  * * * * * * * * * * * * * * * * * * * * 
#     * * * * * * * * * * * * * * * * * *
#       * * * * * * * * * * * * * * * *
#         * * * * * * * * * * * * * * 
#           * * * * * * * * * * * *          #THERE ARE NO ANY PICK POINT
#             * * * * * * * * * *
#               * * * * * * * *
#                 * * * * * * 
#                   * * * *
#                     * *



n=int(input("Enter the number:"))   
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range (i,n-1):
        print("*",end=" ")
        
    for j in range(i,n):
        print("*",end=" ")
    print()
# output:-
#   * * * * * * * * * * * * * * * * * * * 
#     * * * * * * * * * * * * * * * * *
#       * * * * * * * * * * * * * * *
#         * * * * * * * * * * * * *
#           * * * * * * * * * * *
#             * * * * * * * * *
#               * * * * * * * 
#                 * * * * *
#                   * * *
#                     *



n=int(input("Enter the number:"))   
for i in range(n):              # yaha per n-1 karne per pick point ban jayga
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
        
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range (i,n-1):
        print("*",end=" ")
        
    for j in range(i,n):
        print("*",end=" ")
    print()
# output:-
#                     * 
#                   * * *
#                 * * * * *
#               * * * * * * *
#             * * * * * * * * * 
#           * * * * * * * * * * *
#         * * * * * * * * * * * * *
#       * * * * * * * * * * * * * * *
#     * * * * * * * * * * * * * * * * * 
#   * * * * * * * * * * * * * * * * * * *     # there are no any pick point
#   * * * * * * * * * * * * * * * * * * *
#     * * * * * * * * * * * * * * * * * 
#       * * * * * * * * * * * * * * *
#         * * * * * * * * * * * * *
#           * * * * * * * * * * * 
#             * * * * * * * * *
#               * * * * * * *
#                 * * * * *
#                   * * *
#                     *    



n=int(input("Enter the number:"))   
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
        
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range (i,n-1):
        print("*",end=" ")
        
    for j in range(i,n):
        print("*",end=" ")
    print()
# output:-
#                     * 
#                   * * *
#                 * * * * *
#               * * * * * * *
#             * * * * * * * * * 
#           * * * * * * * * * * *
#         * * * * * * * * * * * * *
#       * * * * * * * * * * * * * * * 
#     * * * * * * * * * * * * * * * * *
#   * * * * * * * * * * * * * * * * * * *
#     * * * * * * * * * * * * * * * * *
#       * * * * * * * * * * * * * * *
#         * * * * * * * * * * * * *
#           * * * * * * * * * * *
#             * * * * * * * * * 
#               * * * * * * *
#                 * * * * *
#                   * * *
#                     *


n=int(input("Enter the number:"))   
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
        
    for j in range(i+1):
        print("*",end=" ")
    print()
        
    for j in range(i+1):
        print(" ",end=" ")
    for j in range (i,n-1):
        print("*",end=" ")
        
    for j in range(i,n):
        print("*",end=" ")
    print()
# output:-
#                     * 
#   * * * * * * * * * * * * * * * * * * *
#                   * * *
#     * * * * * * * * * * * * * * * * *
#                 * * * * *
#       * * * * * * * * * * * * * * *
#               * * * * * * *
#         * * * * * * * * * * * * * 
#             * * * * * * * * *
#           * * * * * * * * * * *
#           * * * * * * * * * * *
#             * * * * * * * * *
#         * * * * * * * * * * * * *
#               * * * * * * * 
#       * * * * * * * * * * * * * * *
#                 * * * * *
#     * * * * * * * * * * * * * * * * *
#                   * * *
#   * * * * * * * * * * * * * * * * * * *
#                     * 



n=int(input("Enter the number:"))
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# output:-
# * * * * * * * * * * 
# *                 *
# *                 *
# *                 *
# *                 * 
# *                 *
# *                 *
# *                 *
# *                 *
# * * * * * * * * * *


n=int(input("Enter the number:"))
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        elif (i==1 or i==n-2 or j==1 or j==n-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# output:-
# * * * * * * * * * * 
# * * * * * * * * * *
# * *             * *
# * *             * *
# * *             * *
# * *             * *
# * *             * * 
# * *             * *
# * * * * * * * * * *
# * * * * * * * * * *


n=int(input("Enter the number:"))
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        elif (i==1 or i==2 or i==n-2 or i==n-3 or j==1 or j==2 or j==n-2 or j==n-3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# output:-
# * * * * * * * * * * 
# * * * * * * * * * *
# * * * * * * * * * *
# * * *         * * *
# * * *         * * * 
# * * *         * * *
# * * *         * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * * 

