from xml.etree import ElementTree as ET
#from xml.dom import minidom

doc = ET.parse('account_chart_skr49.xml').getroot()
data = doc.find('data')

out = open('account_chart_skr94.csv', 'w+')
out.write('id;parent_id;code;name;type;user_type\n')
print doc
for s in data.findall('record'):
    if s.get('model') == 'account.account.template':
        line = s.get('id') + ";"
        try:
            line += s.find(".//field[@name='parent_id']").get('ref')
        except (TypeError, AttributeError):
            pass
        line += ";"
        line += s.find(".//field[@name='code']").text + ";"
        line += s.find(".//field[@name='name']").text + ";"
        line += s.find(".//field[@name='type']").text + ";"
        line += s.find(".//field[@name='user_type']").get('ref') + ";"
        line += "\n"
        out.write(line.encode('utf8'))
        print line
out.close()
print 'finished'



#
# xmldoc = minidom.parse('account_chart_skr49.xml')
# itemlist = xmldoc.getElementsByTagName('record')
# print(len(itemlist))
# for s in itemlist:
#     if s.attributes['model'].value == 'account.account.template':
#         line = ""
#         line += s.attributes['id'].value
#         line += ";"
#         #line += s.childNodes['code'].nodeValue
#         #print line
#         print s