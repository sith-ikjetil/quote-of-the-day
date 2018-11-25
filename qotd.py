import http.client
from xml.dom.minidom import parse
import xml.dom.minidom

conn = http.client.HTTPSConnection("www.quotedb.com")
conn.request("GET", "/quote/quote.php?action=random_quote_rss")
response = conn.getresponse()
xxml = response.read() 

xxstart = str(xxml).find("<rss")
xxend = str(xxml).find("</rss>")
xxml = str(xxml)[xxstart:xxend+6]

DOMTree = xml.dom.minidom.parseString(xxml)
collection = DOMTree.documentElement.getElementsByTagName("item")

print("== Quote of the Day ==")
for e in collection:
    print( e.getElementsByTagName("description")[0].childNodes[0].data )
    print( "    :: " + e.getElementsByTagName("title")[0].childNodes[0].data )
    break
