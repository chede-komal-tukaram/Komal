list =[]

#[]- squre bracket
#() - round bracket
#{} - curly bracket

"""
a = 10
print(a,type(a))

colors = ['Red','Green','Blue','Black','Pink']
print(colors,type(colors))

avalue = 'welcome'
avalue[0]

print(colors[0])        #Red
print(colors[4])        #Pink
print(colors[-1])       #Pink
print(colors[3])        #Black

print (colors[0:3])     #Red,Green,Blue"""


##=========================================================================================
'''
colors = ['Red','Green','Blue','Black','Pink']
newitem = 'white'
colors[3] = newitem     #item assignement
colors[4] = 'Yellow'
print(colors,type(colors))

#avalue ='welcome'
#avalue[3] = 'd'         #TypeError: 'str' object does not support item assignment

#Mutable :- Means changable/we can modify
#Immutable :- non changable / we can't modify

#string - Immutable      # Item assignment is not allowed.
#List - Mutable          #Item assignment is allowed.

#we can not change single or few element/item from list.
#however we can replace whole string

#List - we can change single or few element/item from list.

avalue = 'welcome'
print(avalue)
avalue = 'weldone'
print(avalue)'''

##============================================================================================

'''
avalue = 'welcome'
print(avalue)                   #welcome
result = avalue.replace('c','d')
print(avalue)                   #welcome
print(result)                   #weldome

avalue = 'welcome'
print(avalue[::1])              #welcome
print(avalue[::-1])             #emoclew
print(avalue[::2])              #wloe
print(avalue[::-2])             #eolw


colors =['Red','Green','Blue','Black','Pink']

print(colors[::1])              #['Red', 'Green', 'Blue', 'Black', 'Pink']
print(colors[::-1])             #['Pink', 'Black', 'Blue', 'Green', 'Red']
print(colors[::2])              #['Red', 'Blue', 'Pink']
print(colors[::-2])             #['Pink', 'Blue', 'Red']'''