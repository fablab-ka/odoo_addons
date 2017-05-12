from xml.etree import ElementTree as ET
#from xml.dom import minidom




int = open('Kontenplan_V5.csv', 'r')
out = open('account_chart_EXPORT.xml', 'w+')


out.write('''<?xml version="1.0" encoding="utf-8"?>
<openerp>
    <data noupdate="1">
    <!-- account templates -->\n''')
int.readline()#skip the first line
line = str(int.readline())
#line[0] Category
#line[1] Code
#line[2] Name
#line[3] Type

while line:
    print line
    line = line.replace('\n', '').split(';')
    if len(line) != 4:
        print line
        exit()
    print line
    type = ""
    user_type = ""
    if line[3] == "view":
        line = str(int.readline())
        continue #ignore view entries
        type = "view"
        user_type = "account.account_type_view"
    elif line[3] == "asset":
        type = "other"
        user_type = "account.data_account_type_current_assets"
    elif line[3] == "liability":
        type = "other"
        user_type = "account.data_account_type_current_liabilities"
    elif line[3] == "income":
        type = "other"
        user_type = "account.data_account_type_revenue"
    elif line[3] == "expense":
        type = "other"
        user_type = "account.data_account_type_expenses"
    elif line[3] == "other":
        type = "other"
        user_type = "l10n_de.account_type_other"
    else:
        print("TYPE ERROR")
        exit()

    out.write('        <record id="chart_skr49_' + line[1] + '" model="account.account.template">\n')
    out.write('            <field name="code">' + line[1] + '</field>\n')
    out.write('            <field name="name">' + line[2] + '</field>\n')
    out.write('            <field name="user_type_id" ref="' + user_type + '"/>\n')
    out.write('            <field name="chart_template_id" ref="l10n_chart_de_skr49"/>\n')
    out.write('        </record>\n')
    out.write('\n')
    line = str(int.readline())

out.write('    </data>\n')
out.write('</openerp>')


int.close()
out.close()
print 'finished'