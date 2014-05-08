import MySQLdb
import random 
import ConfigParser

config = ConfigParser.ConfigParser()

config.read(["../../bookworm.cnf"])
dbname = config.get("client","database")

con = MySQLdb.connect(read_default_file="~/.my.cnf",use_unicode='True', charset='utf8', db=dbname)

nsamples=96

cursor = con.cursor()
cursor.execute("SELECT filename FROM catalog")

output = open("groups.tsv","w")

print "filename\trandomset"
for line in cursor.fetchall():
    bookid = line[0]
    randomset = 1 + int(random.random()*nsamples)
    print str(bookid) + "\tSample " + str(randomset)

