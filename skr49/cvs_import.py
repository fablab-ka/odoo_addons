from xml.etree import ElementTree as ET
#from xml.dom import minidom




int = open('Kontenplan_V5.csv', 'r')
out = open('account_chart_skr49.xml', 'w+')


out.write('''<?xml version="1.0" encoding="utf-8"?>
<openerp>
    <data noupdate="1">
    <!-- account templates -->\n''')
int.readline()#skip the first line
line = int.readline()
#line[0] Category
#line[1] Code
#line[2] Name
#line[3] Type

while line:
    line = line.replace('\n', '').split(';')
    if len(line) != 4:
        print line
        exit()
    print line
    type = ""
    user_type = ""
    if line[3] == "view":
        type = "view"
        user_type = "account.account_type_view"
    elif line[3] == "asset":
        type = "other"
        user_type = "account_type_asset_de"
    elif line[3] == "liability":
        type = "other"
        user_type = "account_type_liability_de"
    elif line[3] == "income":
        type = "other"
        user_type = "account_type_income_de"
    elif line[3] == "expense":
        type = "other"
        user_type = "account_type_expense_de"
    elif line[3] == "other":
        type = "other"
        user_type = "account.account_type_other"
    else:
        print("TYPE ERROR")
        exit()

    out.write('        <record id="chart_skr49_' + line[1] + '" model="account.account.template">\n')
    out.write('            <field name="code">' + line[1] + '</field>\n')
    out.write('            <field name="name">' + line[2] + '</field>\n')
    if line[0]:
        out.write('            <field name="parent_id" ref="chart_skr49_' + line[0] + '"/>\n')
    out.write('            <field name="type">' + type + '</field>\n')
    out.write('            <field name="user_type" ref="' + user_type + '"/>\n')
    out.write('        </record>\n')
    out.write('\n')
    line = int.readline()

out.write('    </data>\n')
out.write('</openerp>')


int.close()
out.close()
print 'finished'