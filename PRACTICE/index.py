# one line comment => using # we use one line comment

print('hello\nworld !!')


#multiple line comment

'''cnkjvd
 dnmcvkfndvkjd
 mvlkd
 multiple line comments'''

# Indentation error=> in python it checks the spacing of in coding so if there is something that did not have proper indentation python will throw the error'''

'''print("hellos")
       print("hdfjgvjfdg")'''
       


# REPL in terminal we use REPL by writing `py` it will open a python repl
'''we can perform all sort of mathematical operations and other things that python supports'''

#varialbe declaration and rules
w=True
x=9
y="hello"
z=8.4


'''rules for variable naming variables can only have alphabets, numbers and underscore but variables cannot start with number .
   variables in python are dynamically typed so no need to tell the type of variable.
   Types of variable => float=2.3, integer=2, string="hello", boolean=true or false and null=none'''
x=2
print(x)


# type of any variable
'''we use type() to check the type of any variable'''
print(type(x))

# use + or , to concate
print("this is " , x)

# seperator 
'''seperator should be written ninside the print it will not work if it is outside the print operator , if outside the print it will be treated as avariable'''
print(w,x,y,z,sep="=>")


# Data types in Python

''' data types  1->Numeric ->Integer= #whole numbers like =>1, 100, -699, -45
                            ->Float = #Descimal numbers like =>1.9, 9.3, -8.9
                            ->Complex Number =# one number is imaginary called comlex numbers where one number is imaginary like =>8+k, 9+3j
                2->Dictionary = # stored in key value pairs =>{"name":"ram","class":12}
                3->Boolean= # Bolean means either True or False
                4-> Set = # unordered collection of unique values =>{"banana","apple","orange"}
                5->sequence Type ->String = # alpahbets or numbers that we can keen in "" or '' like =>"hello" , 'world
                                ->Tuple = # sequence data that we store in curly brackets => {3,6,7889,65}
                                ->List=# sequnce data that we store in  square brackets =>[1,7,8,3]
                6->none
                                '''


# ASCII and unicode values
# ascii=American standard code for information interchange
#ord() is used to get the ASCII representation of any one character
print(ord('A')) #ans=65 which is the ASCII representation of 'A'
#chr() is used to get the character from ascii value
print(chr(65)) #ans=A which is the character value of ascii value 65



# Input taking from terminal

name =input('enter name ') #input always takes pareameters as string that are given in terminal
print(name)

#Type casting => (it is used to chang the type of any variable )

age =int(input('enter age '))
print(age, type(age))

# Exircise  write a program to print the sum of two number

num1= int(input('enter first number : '))

num2= int(input('enter second number : '))
print('your sum is: ', num1+num2)