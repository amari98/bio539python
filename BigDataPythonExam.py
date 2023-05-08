#!/usr/bin/env python3


# Function 1: For total number of possible substrings
def numsubstrings(k, string):
    '''
    Count the number of possible substrings of length k in a given string
    
    Args:
        k: substring length
        string: string of characters
            
    Return: 
        int: total number of all possible substrings of length k based on length of given 
        character string
    '''
    #possible number of combinations of 4 bases (A, C, T, G) for substrings that are length k
    combinations = 4**k
    
    # total number of slots of length k in string 
        #(1-k) accounts for the fact that there are going to be less slots available than the total 
            #number of characters in a string, based on the value chosen for k (for example, a 
            #string that is 9 character long will only have 8 available slots with a length of 2 
            #characters, 7 available slots with a length of 3 characters, etc.)
    slots = len(string) + (1-k)
    
    #we need to know if the total number of possible substrings is limited by 
        #the number of slots available in a string, or by the number of bases (4)
    #if the total number of combinations is less than the number of slots, 
        #return the number of combinations. 
    #if the total number of combinations is greater than the number of slots, 
        #return the number of slots
    if combinations <= slots:
        return combinations
    else:
        return slots
    
    
# Function 2: For observed number of substrings
def observed(k, string):
    '''
    Loop through a string of characters and count the actual observed number of unique substrings 
    of length k in the given string
    
    Args:
        k: substring length
        string: string of characters
        
    Return: 
        int: observed number of unique substrings of length k based on a given string
    '''
    #Total slots of length "k" in string (see note from function #1)
    slots = len(string) + (1-k)
    
    #start an empty list to store unique substrings
    substrings = []
    
    #loop through all slots in the given string length k
    for i in range(slots):
        #If the substring in the ith slot is not already in the list "substrings" then it 
            #is added to substrings with "append"
        if string[i:i+k] not in substrings:
            substrings.append(string[i:i+k])
        #return the length of "substrings" for the total number of unique substrings of 
            #length k in a given string
    return len(substrings)


#Function 3: For linguistic complexity
def ling_complex(string):
    '''
    Loop through all possible and observed substrings of all sizes and determine 
    linguistic complexity for a given string
    
    Args:
        k: substring length
        string: string of characters
        
    Return: 
        int: (sum of all observed substrings of all lengths k)/
             (sum of all possible substrings of all lengths k)
    '''
    #start an empty list to store total observed and possible substrings
    pos = 0
    obs = 0
    
    #loop through all possible and observed substring lengths and add the number of observed 
        #and possible substrings of length k, without overwriting what already eixsts in each list
    for i in range(len(string)):
        k = i + 1
        
        pos = pos + numsubstrings(k, string)
        obs = obs + observed(k, string)
        
    return obs/pos
            
            
        


