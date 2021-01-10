import re 

txt ="""
     romina bagheri romina@bagheri.com
     darya khalilzadeh darya@khalilzadeh
     arvand azimi arvand@azimi.com
     darya khalilzadeh darya@khalilzadeh
     arvand azimi arvand@azimi.com
     darya khalilzadeh darya@khalilzadeh
     arvand azimi arvand@azimi.com
     darya khalilzadeh darya@khalilzadeh
     arvand azimi arvand@azimi.com
     darya khalilzadeh darya@khalilzadeh
     arvand azimi arvand@azimi.com
     darya khalilzadeh darya@khalilzadeh
     arvand azimi arvand@azimi.com
"""
x = re.search("^a",txt)
print('x',x)