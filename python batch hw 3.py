
"""
HOMEWORK_3  : FRIENDSHIP LOVE CALCULATOR
NAME        : AHER SAURABH SANTOSH
BATCH       : PYTHON
GUIDE BY    : BHAVSAR SIR
DATE        : 24/7/2022 (11:13 PM) 
DESCRIPTION : CALCULATE THE NUMBER OF LETTERS LOVE IN BOTH AND  
"""

#>>> Here I declared variables 
#>>> few are string few are integer
name1="None"
name2="None"
capitalize_name1=""
capitalize_name2=""
sum_of_num1 = 0
sum_of_num2 = 0
concat_name = ""
 
#>>> NOTE::Take Names of both Friends
name1 =input("ENTER NAME:>")
name2 =input("ENTER NAME:>")
print("\n")

#>>> Capitallize Both the Names using Upper() function
capitalize_name1 = name1.upper()
capitalize_name2 = name2.upper()


#>>> Check Both Letters are capital by printing them
print(capitalize_name1)
print(capitalize_name2) 

#count letters love in both using COUNT() function
a,b,c,d=0,0,0,0
a = capitalize_name1.count('L')
b = capitalize_name1.count('O')
c = capitalize_name1.count('V')
d = capitalize_name1.count('E')
#print(a,b,c,d)


p,q,r,s=0,0,0,0
p = capitalize_name2.count('L')
q = capitalize_name2.count('O')
r = capitalize_name2.count('V')
s = capitalize_name2.count('E')
#print(p,q,r,s)



#>>> Compute letters of both name
sum_of_num1 = a+b+c+d
sum_of_num2 = p+q+r+s

#print(sum_of_num1)
#print(sum_of_num2)


#>>> Concatination done but here unneccesarily space get added
#>>> Problem is    : Space get added because of space
#>>> How to Solve? : TRY to convert int into string 
concat_names = sum_of_num1 + sum_of_num2
#>>> print("Your Friendship Percentage is => ",sum_of_num1,sum_of_num2)


#>>> Converting INT to STRING
#>>> SOLUTION: I used here str(object) ----> string
#>>> Hence int got converted into string and ready for concatination
string1 = ""
string2 = ""
#>>> print(type(string1))
string1 = str(sum_of_num1)
string2 = str(sum_of_num2)
#>>> print(type(string1))




#___________________________DISPLAY_______________________________________________
print("----------------------------------------------------------------------------")
print("Your Friendship Percentage is => "+string1+""+string2)
print("----------------------------------------------------------------------------")
