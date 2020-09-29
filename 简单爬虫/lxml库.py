import re

from lxml import etree

from lxml import etree
text = ''' <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div> '''


# HTML自动修复缺失的</li>
html = etree.HTML(text)

# 直接获取属性，由于href标签缺失可能导致错位，需要改进为获取标签对象再获取属性

li_elements = html.xpath('//li[@class="item-1"]')

for li_element in li_elements:
    print(etree.tostring(li_element).decode())
    href = li_element.xpath('./a/@href')[0] if len(li_element.xpath('./a/@href')) > 0 else None
    title = li_element.xpath('./a/text()')[0] if len(li_element.xpath('./a/text()')) > 0 else None
    item = {'href': href, 'title': title}
    print(item)


