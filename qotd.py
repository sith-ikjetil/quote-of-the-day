import http.client
from xml.dom.minidom import parse
import xml.dom.minidom

conn = http.client.HTTPSConnection("www.quotedb.com")
conn.request("GET", "/quote/quote.php?action=random_quote_rss")
response = conn.getresponse()
xxml = response.read() 

index = str(xxml).find("<!")
index /= 2

xxml = str(xxml[int(index):])
xxml = xxml[2:]

index = str(xxml).find("<rss")

xxml = str(xxml[int(index):])

index = str(xxml).find("</rss>")
xxml = str(xxml[:index+6])

DOMTree = xml.dom.minidom.parseString(xxml)
collection = DOMTree.documentElement.getElementsByTagName("item")

print("== Quote of the Day ==")
for e in collection:
    print( e.getElementsByTagName("description")[0].childNodes[0].data )
    print( "    :: " + e.getElementsByTagName("title")[0].childNodes[0].data )
    break
