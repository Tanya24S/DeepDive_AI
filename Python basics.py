#Python basics(also comparisons with c++ since that's my ult too)

#to check data type
print(type(50))     output>>int
#variables
a=50   #data type is assigned auto unlike in c++ where int a=50;
#lists
x=[2,3,4,5]
print(x) #prints the whole list(unlike in c++ where you'll have to run a loop for it to print)
len(x) #to check the length, py has self defined functions
x[0] #to access
#slicing in py means you can handle both an element or sublist eg:
x[0:2] #where 2 is not included
x[:-1] #means from 0th index to second last element
#Dictionaries
x={'hello':42} #to print value use x['hello']
x['wello']=22 #to add a new element
#boolean
is_adult=True #or can write
age=25
is_adult= age>18 #this evaluates to true
#if, else, elif
age = 25
if age < 18:
   print("You are a minor.")
elif age >= 18 and age < 65:
   print("You are cooked.")
else:
   print("You are old.")
#for, while loop
for i in [2,4,8]:
   print(i)  #prints the whole list with each element in new line
while i<3:
   print(i)
#If,else,else if in c++ we have if(i<18){}
#for, while loop we have for(int i=0;i<n;i++){}, while(i==true){}
"""for break and continue the working is same(only put syntax ';' after the respt words), if use break the loop breaks then and there,
but if use continue then only that statement dosen't get executed rest loop continues"""
#functions
def hello(object):
   print("hello"+ object+ "world")
hello("beautiful") #function call
#prints: hello beautiful world
"""void repeat(int a, int n){} or vector<int> repeat(vector<int>arr, int n){} in c++
Also to print the above statement in c++, we'll write cout<<"hello"<<object<<"world"; """
#classes(a good way to describe class is a way to define your own data type(other than the integrated ones) and even your own methods)
class name:
