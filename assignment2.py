Math_mark = int (input ("enter math mark "))
Science_mark = int (input ("enter science mark "))
History_mark = int (input ("enter History mark "))
Geography_mark = int (input ("enter Geography mark "))
English_mark = int (input ("enter English mark "))
if Math_mark >= 50:
    print("pass")
else:
    print("fail")
if Science_mark >= 50:
    print("pass")
else:
    print ("fail") 
if History_mark >= 50:
    print("pass")
else:
    print ("fail") 
if Geography_mark >= 50:
    print("pass")
else:
    print("fail")    
if English_mark >= 50:
    print("pass")
else:
    print("fail")

final_average = (Math_mark + Science_mark + History_mark + Geography_mark + English_mark)/5
if final_average >= 85:
    print ("Excellent")
if final_average <= 84 and final_average > 75 :
    print ("very good") 
if final_average <= 74 and final_average > 65 :
    print ("Good")
if final_average <= 64 and final_average >= 50 :
    print ("pass")
if final_average < 50:
    print ("fail")    
if (final_average >= 85 and Math_mark >= 80) or (final_average <85 and Math_mark >= 90) :
    print ("student can join the compitition")
