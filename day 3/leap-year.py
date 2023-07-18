year = int(input("input the year : "))
if year % 4 == 0 :
   if year % 100 == 0:
       if year % 400 == 0:
         print("this year is lead")
       else:
           print("this year is not lead")
   else :
       print("this year is lead")
       
else:
    print("this year is not lead")