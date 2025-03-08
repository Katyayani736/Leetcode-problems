''' 
A very different solution for the classic reverse the string prolem. 
My approach was to reduce the time complexity to O(n/2) [it is O(n) I KNOW].
It all resulted in O(n^2) because of the string concatenation provided by python.
Still I will post this because i love this solution of mine and it is not available anywhere on the internet.
The intuition behind it was to run the loop from half the middle index to start and concatenate accordingly in a new variable.
'''

s=input()
def reverse_string(s):
    s1=''
    l=len(s)
    if l%2==0:
        for i in range(l//2,l):#even
            s1=s[i]+s1+s[-i-1]
            #print(s1)
    else:
        s1=s1+ s[l//2]
        for i in range(l//2+1,l):#odd
            s1=s[i]+s1+s[-i-1]
            #print(s1)
    print("Reversed String:", s1)
print("Original String:", s)
reverse_string(s)
