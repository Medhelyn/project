"""

rows = 6

     *
    **
   ***
  ****
 *****
******

"""

rows = 6

for row in range(1, rows+1):
     for star in range(1, row+1):
          if (star <= rows-row):
               print(" ", end="*")
          else:
               print("*", end=" ")
     print()

 # MASE SLH