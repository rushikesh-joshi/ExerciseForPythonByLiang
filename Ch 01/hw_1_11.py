# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 12:18:10 2018

@author: Rushikesh
"""

styledEquation = """
The US Census Bureau projects population based on the following assumptions:
    One birth every 7 seconds
    One death every 13 seconds
    One new immigrant every 45 seconds
    
Assume the current population is 312032486 and one year has 365 days.
What will be the population of US after 5 years.
"""
print(styledEquation)

print ("projected population after 5 years  = %.0f" 
       %  ( 312032486 
           + (
                   (( 5 * 365 * 24 * 60 * 60 )//7) 
                   - (( 5 * 365 * 24 * 60 * 60 )//13)
                   + (( 5 * 365 * 24 * 60 * 60 )//45)
            )
           )
    )

