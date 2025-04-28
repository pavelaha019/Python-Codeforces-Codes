#Name : Pavel Ahammed 
#Id : 221074002

def unique_substrings(string, k):
  
    substrings = set()
    
   
    for i in range(len(string) - k + 1):
        substrings.add(string[i:i + k])
    
   
    return list(substrings)


string = input("Enter a string: ")
k = int(input("Enter length k: "))

if k > len(string) or k <= 0:
    print("Invalid input! 'k' should be between 1 and the length of the string.")
else:

    result = unique_substrings(string, k)
    print("Unique substrings of length", k, ":", result)

