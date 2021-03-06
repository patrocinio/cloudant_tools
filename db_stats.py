import requests
import json
from cloudant.client import Cloudant
from cloudant.database import CloudantDatabase

import config

def main():
    client = Cloudant(config.username, config.password, account=config.account)

    client.connect()

    dbs = client.all_dbs()

    output = []
    for db in dbs:
    	print 'Retrieving stats for {0}...'.format(db)
        db = CloudantDatabase(client, db)
        print "db: " + json.dumps(db)
        output.append(db.doc_count())

	print json.dumps(output, indent=4)
	print json.dumps(sort(output), indent=4)

    client.disconnect()

def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array



if __name__ == "__main__":
	main()
