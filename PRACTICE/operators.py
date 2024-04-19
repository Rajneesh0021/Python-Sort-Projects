''' 
#operators => Arithmetic operators-> +(addition), -(subtraction), *(multiply), %(modulus){return remainder}, /(division), **(exponential), //(floor division){retuens round value of the division ex.=> 4//3 it will give 1 not 1.333}

            =>Assignment operators-> =, +=, -=, *= , /=, %=, //=, **=, &=,|=,^=,>>=,<<= 
            =>comparison operator
            =>logical operator
            =>identity operator
            =>membership operator
            =>bitwise operator
'''
#Arithmetic operators
x=4
y=3
print('sum ', x+y)
print('subtraction ', x-y)
print('multiplicatiopn ', x*y)
print('modulus(remainder) ', x%y)
print('division ', x/y)
print('exponential(power) ', x**y)
print('floor division ', x//y)

# Assignment operators
z=x
print('= ', z)
z+=x
print('+= ', z)
z-=x
print('-= ', z)
z*=x
print('*= ', z)
z/=x
print('/= ', z)
z%=y
print('%= ', z)
z//=x
print('//= ', z)

z**=y
print('**= ', z)

z=None
x="he"
# z&=x
# print('&= ', z)

# z|=x
# print('|= ', z)

# z^=x
# print('^= ', z)

# z>>=x
# print('>>= ', z)

# z<<=x
# print('<<= ', z)