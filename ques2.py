"""Write a program that takes length and width as 
input from the user.
- If both are equal → print area (l × w)
- If different → print perimeter 2 × (l + w)

Example:
Input:  l=5, w=5
Output: Area = 25

Input:  l=4, w=7
Output: Perimeter = 22"""

def value(l, w):
    if l == w:
        return l * w
    else:
        return 2 * (l + w)
    
print(value(4, 6))