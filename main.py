import csv
import urllib2


# read file local
# f = open('violations.csv')
# open file from url
f = urllib2.urlopen("http://forever.codeforamerica.org/fellowship-2015-tech-interview/Violations-2012.csv")

csvfile  = csv.DictReader(f)
catfile = dict()

#for row in csvfile:
#	print row 

def categories(csvfile):
    for row in csvfile:
        if row["violation_category"] not in catfile:
            catfile[row["violation_category"]] = set()
    	catfile[row["violation_category"]].add(row["violation_date"]) 
    return catfile


catfile = categories(csvfile)

print "There are [" , len(catfile) , "] categories of violations!"

for row in catfile:
	count = 0
	max_violation = None
	earliest_violation = None
	min_violation = None
	latest_violation = None
	
	print "Category %s  " %(row)
	for rows in catfile[row]:
		count += 1
		#print "   %s " %(rows)
		if max_violation == None or max_violation > rows:
			max_violation = rows
			earliest_violation = max_violation
		if min_violation == None or min_violation < rows:
			min_violation = rows
			latest_violation = min_violation
		
	print "Total number of violations for category  [%s ] is [%d]" %(row, count)	
	print "The latest violation is %s" %(latest_violation)
	print "The earliest violation is %s" %(earliest_violation)
