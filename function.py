#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#@title Mixed Number Function
def user_fraction():

    """takes a user input of several mixed numbers, seperated via a comma,
    and turns each into an improper fraction"""

    from fractions import Fraction as frac
    import re
    # re is used to split the resulting input into seperate items
    # these are further split into numbers but unfortunately
    #python counts even spaces as a list item
    # swo I split them further down and just get numbers which I can
    # assign via index the fraction stays as 3/4 for example
    # but frac accepts / and knows it is a fraction
    s = input('your mixed numbers: ')
    re.split(',| /| |',s)
    re.findall(r'\b\d+\b', s)
    s = s.replace(',','').split(' ')
    a = frac(s[1])
    b = frac(s[3])

    #calculate the improper fraction by multiplying the whole number
    #with the denominator and adding the numerator then printing the resulting
    #number and the denominator seperated by a comma. Frac knows that this then
    # is a fraction and returns the improper fraction.
    im_fraction = frac((int(s[0])*a.denominator + a.numerator) , a.denominator)
    im_fraction1 = frac((int(s[0])*b.denominator + b.numerator) , b.denominator)
    x = im_fraction
    y = im_fraction1
    print()
    print(f'{x} <> {y}',  end=" ")
    print()

    print()
    print
    return()


user_fraction()

