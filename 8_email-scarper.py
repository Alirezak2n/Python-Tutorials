import re

text = 'how to find a random string in text'

pattern = re.compile('a random string')
result = pattern.search(text)
print(result)

#faghat yedune harf ro az in harfa peyda mikone
pattern2 = re.compile('[abc]')
result = pattern2.search(text)
print(result)

#tu ye range migarde avali ro mide
pattern2 = re.compile('[a-z]')
result = pattern2.search(text)
print(result)

#tu 2ta range migarde avali ro mide
pattern2 = re.compile('[a-zA-Z]')
result = pattern2.search(text)
print(result)

#+ mide kole kalame ro bede
pattern2 = re.compile('[a-zA-Z]+')
result = pattern2.search(text)
print(result)

#harchi k harf ya adad bashe o mide
pattern2 = re.compile('[a-zA-Z0-9]+')
result = pattern2.search(text)
print(result)

#\baraye standard hast k bgim donbale . begard
text2='i am alireza alireza@yahoo.com my email and eli.fk-H@gmail.com'
pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
result = pattern.search(text2)
#search faghat yedune ro migarde
print(result)
result = pattern.findall(text2)
print(result)