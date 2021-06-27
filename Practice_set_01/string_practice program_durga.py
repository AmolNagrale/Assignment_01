# Reversed string

# 1.approch by using slicing

# s = "Team brain work is most popular classes"
# print(s[::-1])

# 2. approche by using reversed() function

# s = "Team brain work is most popular classes"
# 
# r = reversed(s)
# 
# #for i in r:
# #    print(i)
# output = ''.join(r)
# print(output)

#==========================================================

# #3. by using while loop
# str = input("Enter the valid string :")
# #s = "Amol"
# output = ''
# i = len(str)-1
# while i >= 0:
#     output = output + str[i]
#     i = i - 1
# print(output)

#==========================================================

# 4. WAP on reveres odrer of words

# s = input("Enter a string : ")
# l = s.split()    # to saperate a individual words
# l2 = l[::-1]     # to reversed a input words
# output = ''.join(l2) # for a output in a single line (by default we are getting output in list form)
# print(output)

#=========================================================

# 5. WAP to reverse internal content of each word

# s = " Durga software solution "
# l = s.split() # for spliting each words
# l2 = []       # for storing after append operation
# for word in l: # for iteration
#     l2.append(word[::-1]) # After reverse operation store value in l2
# output = ' '.join(l2)    # for output in single line instate list form[------]
# print(output)

#=================================================================================

# 6. WAP to reverse every second word of a string

# s = "one two three four five six"
# l = s.split() # split a word for individual operation
# i = 0        # take variable for iteration
# l1 = []      # empty list for output collection
# while i<len(l):   # condition for iteration
#     if i%2 == 0:  
#         l1.append(l[i]) # once condition is satisfy value will store at l1
#     else:
#         l1.append(l[i][::-1]) # if condition is not satisfied even value reversed the position & store into l1
#     i += 1    
# #print(l1)
# output = ' '.join(l1)
# print(output)

#==================================================================================

# # 7. WAP to print the charecters present at even index and odd index saperately for the given string
# 
# s = "Durga software"
# i = 0
# print("The charecter present at odd index :")
# while i<len(s):
#     print(s[i]) # it can be filter even & odd charecter from string
#     i +=2
# 
# i = 1
# print("The charecter present at even index :")
# while i<len(s):
#     print(s[i]) # it can be filter even & odd charecter from string
#     i +=2

# Alternate option by using for loop

# s = "durgasoft"
# 
# for i in range(len(s)):
#     
#     if i%2 == 0:
#         
#         print("The even number of charecters is ",s[i])
#     else: 
#         print("The odd number of charecters on given string is",s[i])

#=======================================================================
 
 # WAP to sort charecters of the sting, first alphabets, symbol & followed by digit
 
#s = "A1D2FT3GHB489"
# s = input("Enter only alphanumeric string ti sort :")
# Alphabets = [] # Take empty list storing sorted elements
# Digits = [] # Take empty list storing sorted elements
#  
# for ch in s: 
#     if ch.isalpha(): # for sorting alphabets
#         Alphabets.append(ch) # for storing it on Alphabets
#     else:
#         Digits.append(ch) # for storing it on Digits
# output = ''.join(sorted(Alphabets)+sorted(Digits)) # for joining concatenate sorted elements
# print(output)

#=======================================================================

s = 'abcdefghijk'
for i in s:
    #if i%2==0:
    print(i)


         

    