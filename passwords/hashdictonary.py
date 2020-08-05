import csv
import pprint
import hashlib


with open('dictionary.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        password = ', '.join(row)
        hash = hashlib.sha1()
        hash.update(password.encode('utf-8'))
        hash.digest()
        print(password, ' > ',hash.hexdigest())
        with open('hashedpswd.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([password, hash.hexdigest()])
