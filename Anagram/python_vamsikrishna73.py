#function to check if two strings are anagrams or not

def check_anagram(s1, s2):
     
    if(sorted(s1)== sorted(s2)):   #the strings are sorted before they are compared
        print("anagrams")
    else:
        print("not anagrams")        
         

string_1 =input("enter a string: ")
string_2 =input("enter a string: ")
check_anagram(string_1, string_2)