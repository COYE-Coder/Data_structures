# An e-commerce website is trying out a new marketing strategy. 
# On its homepage, there is a list of products, 
# and the plan is to have on-sale items (S) alternate with regular-priced items (R). 
# A programmer is given the task to do this as efficiently as possible. 
# The programmer can pick any product and recode it to be either on-sale or regular-priced. 
# Each value that is changed counts as a swap. 
# Given the initial status of the items, 
# what is the minimum number of swaps needed to recode the website 
# so that no two adjacent items have the same sale status? 
# For example, if the initial ordering of items is status = "SSSRSR". 
# In the first swap, the programmer chooses the second item and recodes it to be regular-priced. 
# The item order then becomes "SRSRSR", which completes the task. 
# Therefore, the minimum number of swaps needed by the programmer is 1.
# As another example, the initial string is 'RSRSSR'. 
# The most efficient change is the make the S at the 5th position R, 
# and the R at the 6th position S. 
# This results in the string 'RSRSRS' after two swaps. 
# Returns: int: the minimum number of swaps needed to complete the task 

def minimumSwaps(status):
    binary = []
    for c in status:
        if c == "S":
            binary.append(0)
        elif c == "R":
            binary.append(1)
    
    print("Status: {}".format(status))
    first_index_triple = []
    first_index_double = []
    #First find Triples and Doubles
    i = 0
    j = 1

    #Doesn't find quadruples or duplicates of arbitrary length
    while (i + 2) < len(binary):

        #Possibly iterate over arbitrary length consecutive duplicates
        while binary[i] == binary[j]:

            if binary[i] == binary[i+1] == binary[i+2]:
                first_index_triple.append(i)
                i += 2
            elif binary[i] == binary[i+1]:
                first_index_double.append(i)
                i += 1
            i += 1

      

        
    print("Triples: {}".format(first_index_triple))
    print("Doubles: {}".format(first_index_double))
    num_changes = len(first_index_triple)
    for d in first_index_double:
        if binary[d:] < binary[:d]:
            num_changes += len(binary[d:]) + 1
        else:
            num_changes += len(binary[:d]) + 1
    return num_changes


status = "SSSSRRRSS"

minimumSwaps(status)