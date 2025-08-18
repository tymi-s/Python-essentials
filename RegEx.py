# regex is a regullar expression. it is a sequence of characters that forms a search pattern.
# regex can be used to check whether certain string contains a specyfic search pattern.

import re
t = "This is a text in which i will search for pattern"

x = re.search("in",t)# checks if t contains in
y = re.search("^This",t)#checks if it starts with This
z = re.search("pattern$",t)#checks if it starts with This
w = re.search("^This.*pattern$",t)#checks if t starts with This and ends with pattern
print(x)
print(y)
print(z)
print(w)
print(type(z))

#available functions in re module:
"""
findall - Returns a list containing all matches
search - Returns a Match object if there is a match anywhere in the string
split - Returns a list where the string has been split at each match
sub - Replaces one or many matches with a string

"""

#characters to use in match keys:
r"""

Character	Description	Example	Try it
[] - A set of characters	"[a-m]"	
\ - Signals a special sequence (can also be used to escape special characters)	"\d"	
. - Any character (except newline character)	"he..o"	
^ - Starts with	"^hello"	
$ - Ends with	"planet$"	
* - Zero or more occurrences	"he.*o"	
+ - One or more occurrences	"he.+o"	
? - Zero or one occurrences	"he.?o"	
{} - Exactly the specified number of occurrences	"he.{2}o"	
| - Either or	"falls|stays"	
() - Capture and group	 

"""

#functions:

s = "String to search in"

#findall() - returns a list containing all matches
print(re.findall("i",s))

#search() - searches for a match and returns a MATCH OBJECT if match was found:

print(re.search("i",s))

#split() - returns a list where string has been split at each match

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#sub() - replaces match witch a desired string

ttt = "Martyna looks bad today"
ttt=re.sub("bad","good",ttt)
print(ttt)


