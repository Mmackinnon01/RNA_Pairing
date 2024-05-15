def Tabulate_RNA(seq):
    # Below we will instantiate a matrix of nan values with
    #the same dimensions as the length of our sequence.
    # We will then replace all nan values with 0 where i>=j-4
    
    M = generate_empty_matrix(seq)

    # Now that we have prepared our matrix for tabulation,
    # we will loop through the indices of the array
    # starting with the smallest sub-sequences possible 
    # and progressing until we can calculate the optimal
    # value for the entire sequence
                
    for k in range(5, len(seq)):
        for i in range(0, len(seq) - k):
            j = i+k
            t, m = max_over_t(i, j, M, seq)
            M[i,j] = max(M[i,j-1], m)
            
    return M