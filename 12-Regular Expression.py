import re  # it is used for searching in texts

string = 'search this inside of this text please'

print('search' in string)
a = re.search('this',string)
print(a)  # it shows in which number of string location we have the word
print(a.span())
print(a.start())

pattern = re.compile('this')  # whit pattern we can use in a lot of places
print(pattern.search(string))
print(pattern.findall(string))  # we find the patter in all times it appear
print(pattern.fullmatch(string))  # it should be the exact string not more not less
print(pattern.match(string))  # it search the first part of the string

print(re.search(r'([a-zA-Z]).([t])',string))  # find a specific set of characters in string text
pattern = re.compile(r'([a-zA-Z]).([t])')
print(pattern.search(string).group())  # it gives the match only and search pattern in string

print(re.search(r'^search',string))  # if it start with search
string = 'a@b.com'
print(re.search(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',string))  # find the email addresses
# email start with any thing,letters,numbers,under score,.,+,-
# the + sign means it can have any length and continue
# the \ sign means it should be a . and if dont have it, it continue to accept any thing
# the $ sign means should end
