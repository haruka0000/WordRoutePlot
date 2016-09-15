from pyquery import PyQuery
a = 'https://www.google.co.jp/search?q=井上麻里奈'
q = PyQuery(url=a)

for elem in q:#q.find('a.entry-link'):
#PyQuery
    q2 = PyQuery(elem)
    print(q2.text())
    print(q2.attr('href'))
    
#lxml
#    print elem.text
#    print elem.get('href')
