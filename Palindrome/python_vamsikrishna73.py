#function to check whether the given numberr is a palindrome

def isPalindrome(s):
    return s == s[::-1]  #returns true or false
 
 

x = int(input("enter a no: "))
x_str = str(x)
ans = isPalindrome(x_str)
 
if ans:
    print("palindrome")
else:
    print("not a palindrome")