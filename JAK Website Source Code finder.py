import sys
import urllib.request

#Warning Internet Connection Required
url='https://github.com/' #Write the link of the website between the colons
webpage=urllib.request.urlopen(url)
print(webpage.read())
