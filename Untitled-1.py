from os import write
import mariadb 
import csv
import re

conn = mariadb.connect(
    user="root",
        password="2173670",
        host="127.0.0.1",
        port=3306,
        database="new_database")



cursor = conn.cursor()



# result = cursor.execute(")

cursor.execute("SELECT node.nid, node.title, url_alias.alias, field_data_body.body_value FROM node \
      JOIN field_data_body ON node.nid = field_data_body.entity_id \
          LEFT JOIN url_alias ON CONCAT('node/', node.nid) = url_alias.source WHERE node.type = 'page' LIMIT 50" )
          
        # LEFT JOIN url_alias ON url_alias.alias = CONCAT(node.nid, 'node/') LIMIT 5")
result = cursor.fetchall()

for x in result:

    print(x)

new_list: list = []

for row in result:
    
    nid = row[0]
    title = row[1]
    alias = row[2]
    body_value = row[3]

    body_value = re.sub('\r\n', '', body_value)


    # pt = re.compile('\n', flags=re.VERBOSE)
    # nid = re.sub('\n',' ', nid)
    # title = re.sub('\n',' ', title)
    # alias = re.sub('\n',' ', alias)
    # body_value = re.sub('\n',' ', body_value)

    obj: list = [nid, title, alias, body_value]


    new_list.append(obj)


with open("zzz.csv", "w") as csv_file:  
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([row[0] for row in cursor.description])
    csv_writer.writerows(new_list)



conn.close()