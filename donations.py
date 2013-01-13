import os
#print os.getcwd()

## donations

class donation:
    'fields: email, date, amount'

def str_to_don (s):
    fields = s.split()
    D = donation()
    D.email = fields[0]
    D.date = fields[1]
    D.amount = float(fields[2])
    return D

def process_donations(filename):
    try:
        donationfile = file(filename, 'r')
    except: print "file ain't there!"
    donations = map(str_to_don, donationfile.readlines())
    donationfile.close
    donor_dict = {}
    for donation in donations:
        if donor_dict.has_key(donation.email):
            donor_dict[donation.email] + donation.amount
        else:
            donor_dict[donation.email] = donation.amount
    donor_file = file('totaldons.txt', 'w')
    for donor in donor_dict:
        donor_file.write ('%f %s\n' % (donor_dict[donor], donor))
    donor_file.close()