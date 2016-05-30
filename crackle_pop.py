# GOAL
# Write a program that prints out the numbers 1 to 100 (inclusive)

# RULES
# If the number is divisible by 3, print Crackle instead of the number.  
# If it's divisible by 5, print Pop.
# If it's divisible by both 3 and 5, print CracklePop.

def crackle_pop():

    number = 1

    while number != 101:
        
        if number % 3 == 0 or number % 5  == 0:
        	if number % 3 == 0 and number % 5  == 0:
        		print "CracklePop"
        	elif number % 3 == 0:
        		print "Crackle"
        	else:
        		print "Pop"
        
#        elif number % 3 == 0:
 #       	print "Crackle"
  #      	number += 1
        
   #     elif number % 5 == 0:
    #    	print "Pop"
     #   	number += 1
        
        else:
        	print number
        
        number += 1
        	    
crackle_pop()