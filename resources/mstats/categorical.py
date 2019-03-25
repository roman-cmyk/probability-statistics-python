# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:28:58 2019

@author: Miguel Ángel Vélez
"""


#------------------------------------------------------------------------------------------------#
#-------------------------------- Categorical Data Analysis -------------------------------------#
#------------------------------------------------------------------------------------------------#

def get_x2(oi, ei):
    """
    Function to calculate the statistical test for the categorical data analysis,
    it is a chi squared value.
    
    Parameters:
    --------------------------
    oi : list
        Frequency from the observed events.
    ei : list
        Frequency from the expected events.
    
    Returns:
    --------------------------
    x2 : double
        Chi squared value which represents the calculated statistical test.
    """
    k = len(oi)
    x2 = sum([((oi[x] - ei[x])**2 / ei[x]) for x in range(k)])
    return x2

def get_ei(oi, pi):
    """
    """
    n = sum(oi)
    ei = [(n * pi[x]) for x in range(len(oi))]
    
    return ei

#------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------#