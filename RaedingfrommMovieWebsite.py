from urllib.request import urlopen
import re
url = "https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=F22A2RC934X0Q4NDWHBA&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_7"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
eg = "<a href=\"/title/tt8902990/\"title=\"Shonali Bose(dir.), Priyanka Chopra, Farhan Akhtar\" >The Sky Is Pink</a>"
#find between > and </a>
print(html)
"""
prints last word
titles = []
title = []
istitle = None
for i in html.split():
    if re.findall(r"^\'>", i):
        istitle = True
    elif re.findall(r"</a>$", i):
        istitle = False
    if istitle == True:
        title.append(i)
    elif istitle == False:
        title.append(i)
        istitle = None
        titles.append(title)
        title = []
print(titles)
"""
"""
titles = re.findall((r"> </a>"), html)
title =[]
# print first word, DO NOT CHANGE
for i in titles:
    if i != ' ':
        title += i
    else:
       #  if 'lt=' in title:
        print(title)
        title= ''
"""
titles = re.findall((r"> </a>"), html)
title =[]
quote_count = 0
for i in titles:
    if i == '/"':
        quote_count += 1
        title += i
    else:
        if quote_count % 2 == 1:
            title += i
        else:
            # print(title)
            title = ''
"""
titles = []
title = []
istitle = None
for i in html.split():
    print(i)
    if re.findall(r"^\'>", i):
        istitle = True
    elif re.findall(r"</a>$", i):
        istitle = False
    if istitle == True:
        title.append(i)
    elif istitle == False:
        title.append(i)
        istitle = None
        titles.append(title)
        title = []
titles = re.findall((r"> </a>"), eg)
for i in titles:
    if i != ' ':
        title += i
    else:
        print(title)

        title= ''
"""