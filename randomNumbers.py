import MySQLdb
import random 
import ConfigParser

nsamples=5
bigsamples=24

config = ConfigParser.ConfigParser()

config.read(["../../bookworm.cnf"])
dbname = config.get("client","database")

con = MySQLdb.connect(read_default_file="~/.my.cnf",use_unicode='True', charset='utf8', db=dbname)

cursor = con.cursor()
cursor.execute("SELECT filename FROM catalog")

output = open("groups.tsv","w")

print "filename\trandomsetA\trandomsetB"
for line in cursor.fetchall():
    bookid = line[0]
    randomsetA = 1 + int(random.random()*nsamples)
    randomsetB = 1 + int(random.random()*bigsamples)
    print str(bookid) + "\tSample " + str(randomsetA) + "\tSample " + str(randomsetB)

