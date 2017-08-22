#first program. An alarm that pops up every 2hours and prompts you to take a break from ur pc
import webbrowser #webrowser and time is a module in the python standard library
import time
count=0 #set the count to 0
break_count =3 #we're taking 3 breaks
print ("Yoo, The program started on" +time.ctime()) #print out the current time when the program started running
while(count < break_count): #while the initial count is less than 3, sleep for 10 secs
 time.sleep(10)
 webbrowser.open('http://www.tutorialspoint.com/python/python_while_loop.htm') #trigger your browser 
count=count+1 #increase count
