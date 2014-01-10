# import triple into neo4j from csv file downloaded from dbpedia
import csv
from py2neo import neo4j, node, rel, cypher
# your database service
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

# csv file
ifile = open("College.csv","rb")
reader = csv.reader(ifile)
graph_db.clear()

reader = list(reader)
relations = reader[0]
# row 2 is full uri of row 1. row 2 = namespace + row 1
properties = reader[2]

rownum = 5
for row in reader[4:]:
    subject, = graph_db.create(
        {properties[1]:row[1]}
    )
    # first one is subject
    objects = row[1:]
    colnum = 2
    for col in objects:
        if col != "NULL":
            object, rel = graph_db.create(
                {properties[colnum-1]:col},(subject, relations[colnum-1],0)
            )
        colnum = colnum + 1
    rownum = rownum + 1
ifile.close()
