from BigDataPythonExam import *


#Function 1 testing:
def test_numsubstrings():
    test = 'ATTTGGATT'
    k = 2
    actual_output = numsubstrings(k, test)
    expected_output = 8
    
    assert actual_output == expected_output #only return an output if there is an error
  
    #running this will not return an error, there are 8 possible slots 
        #of k length 2 in the test string
    
def test_numsubstrings():
    test = 'ATTTGGATT'
    k = 10
    actual_output = numsubstrings(k, test)
    expected_output = 'substring length k is longer than test string'
    
    assert actual_output == expected_output #only return an output if there is an error
    
    #running this will return an error because the substring length is longer than the test string
    
#Function 2 testing:
def test_observed():
    test = 'ATTTGGATT'
    k = 2
    actual_output = observed(k, test)
    expected_output = 5

    assert actual_output == expected_output #only return an output if there is an error
    
    #running this will not return an error, there are 5 unique observed substrings
        #of k length 2 in the test string
    
def test_observed():
    test = 'ATTTGGATT'
    k = 10
    actual_output = observed(k, test)
    expected_output = 'substring length k is longer than test string'

    assert actual_output == expected_output #only return an output if there is an error
    
    #running this will return an error because the substring length is longer than the test string
    
# Function 3 testing
def test_ling_complex():
    test = 'ATTTGGATT'
    actual_output = ling_complex(test)
    expected_output = .875
    
    assert actual_output == expected_output #only return an output if there is an error
    
    #running this will not return an error because the proportion of all observed substrings 
    #and possible substrings for the test string is equivalent to the expected output (35/40 = .875)
    
    