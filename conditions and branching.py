
#Note == must be used in conditionals NOT = since '=' defines functions

#conditions and banching 

#conditional operators return boolean (true/false)

a=6

print('6', a==6)
print('5' , a==5) #== means is exactly equal to which is false for 5

i=5
print (i>2) 

2!=6 #this is the inequality sign so output is true since 2 is not equal to 6


#branching
age = 12
if age > 18:
    print ('you can enter')
elif age==18:
    print ('got to revolution')    
else: print ('move on')

#logic operators take boolean value and replace it with another boolean

# 'or' logic operator
league = 1982

if (league < 1980) or (league > 1989):
    print('league won in 70s or 90s')
else:
    print('league won in 80s')    

# 'and' logic operator    
league = 1970
if (league >1979) and (league <1990):
    print ('album made in 1980s')
else: 
    print ('league won in 70s')

#not logic operator    
album_year = 1983

if not (album_year == '1984'):
    print ("Album year is not 1984")
print('')
print('')
print('')
print('')


album_year = 1970
if album_year < 1980 or album_year == 1991 or album_year == 1993:
    print ("this album came out already")
    
    





