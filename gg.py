# r = requests.get('http://website.com/file.txt'.format(x))
# with open('data.txt', 'a') as f:
#     if 'word' in line:
#         f.write('\n')
#         f.writelines(str(r.text))
#         f.write('\n')
#
# import re
# import  requests as q
# r = requests.get('http://website.com/file.txt'.format(x))
# with open('data.txt', 'a') as f:
#     for l in f.readlines():
#         if re.search(r'\bword\b', l):
#             f.writelines(str(l))
#             f.write('\n')
#
#
# import urllib2
# for line in urllib2.urlopen("http://www.myhost.com/SomeFile.txt"):
#     print (line)

#
# import requests
#
# response = requests.get("http://www.gutenberg.org/files/10/10-0.txt")
# # response.encoding = "utf-8"
# hehe = response.text
# print(hehe)
import re
import urllib.request

# response = urllib.request.urlopen("http://www.gutenberg.org/files/10/10-0.txt")
# print(response)
# lines = response.readlines()
# for line in response.readlines():
page = urllib.request.urlopen("http://www.gutenberg.org/files/10/10-0.txt").read()
text_list = page.decode('utf-8').split('\n')
print(text_list)
with open('data.txt', 'a') as f:
    #     print()
    for line in text_list:
        #     print(line)
        if re.search(r'\bcannot\b', line):
            f.writelines(str(line))
            f.write('\n')
