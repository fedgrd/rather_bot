"""
Fetch "never have I ever" question statements.
Author: Federioc
"""

#import urllib2 to fetch data from website
import urllib2

response = urllib2.urlopen('http://conversationstartersworld.com/never-have-i-ever-questions/')
html = response.read()

#html list to store statements
html_list = []
#write html into a text file
with open("statements.txt", "w") as f:
    f.write(html)
#use the text file to clean the data fetched
searchfile = open("statements.txt", "r")
for line in searchfile:
    if "<p>&#8230" in line and "</a>" not in line:
        html_list.append(line)
searchfile.close()

html_list = [w.replace('<p>&#8230;', '') for w in html_list]
html_list = [w.replace('</p>', '') for w in html_list]
html_list = [w.replace(str(w), 'Never have I ever' + str(w)) for w in html_list]

for i in html_list:
    print i
