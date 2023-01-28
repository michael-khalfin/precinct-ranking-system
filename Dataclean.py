import csv
import json
import datetime
import calendar
import pandas as pd

####################
#GOTVMailers_efforts
####################
# voters = {}

# USER_ID = 0 #1st col
# ZIP_CODE = 2 #3rd col
# AGE = 3
# SEX = 4
# PRECINCT = 5
#
# with open('/Users/grego/PycharmProjects/DataThon/GOTVMailers_Efforts.csv', 'r') as GOTVMailers:
#     reader = csv.reader(GOTVMailers)
#     for row in reader:
#         voter = row[USER_ID]
#         voters[voter] = {'Zip': row[ZIP_CODE], 'Age': row[AGE], 'Sex': row[SEX], 'Precinct': row[PRECINCT]}
#
# del voters["Voter ID"]
# with open('/Users/grego/PycharmProjects/DataThon/voters.json', 'w') as f:
#     json.dump(voters, f)


####################
# Canvassed
####################
#
# canvassed_voters = {}
#
# USER_ID = 0 #1st col
# DATE = 1 #3rd col
# CITY = 2
# ZIP = 3
# RESULT = 4
#
# with open('/Users/grego/PycharmProjects/DataThon/BlockWalkingAttempts.csv', 'r') as BlockWalk:
#     reader = csv.reader(BlockWalk)
#     for row in reader:
#         voter = row[USER_ID]
#         if row[USER_ID] == "" or row[CITY] == "Dallas" or row[CITY] == "" or row[RESULT] == "":
#             pass
#         else:
#             canvassed_voters[voter] = {'Zip': row[ZIP], 'Date': row[DATE], 'Result': row[RESULT]}
#
# del canvassed_voters["VoterID"]
# with open('/Users/grego/PycharmProjects/DataThon/canvassed_voters.json', 'w') as f:
#     json.dump(canvassed_voters, f)


all_voters = {}

USER_ID = 0 #1st col
ZIP = 3
SEX = 4
BIRTH_YEAR = 6
SITE = 7
PRECINCT = 8

with open('/Users/grego/PycharmProjects/DataThon/Voters_3of3.csv', 'r') as All_Voters:
    reader = csv.reader(All_Voters)
    next(reader)
    next(reader)
    for row in reader:
        voter = row[USER_ID]
        if row[SITE] == "":
            site = "null"
        else:
            site = row[SITE]
        try:
            val = int(row[BIRTH_YEAR])
        except:
            pass

        print(type(val))
        if voter == "--":
            pass
        else:
            try:
                val = int(row[BIRTH_YEAR])
                all_voters[voter] = {'Zip': row[ZIP], 'Sex': row[SEX], 'Age': (2022 - val), 'Site': site,
                                 'Precinct': row[PRECINCT]}
            except:
                pass

with open('/Users/grego/PycharmProjects/DataThon/3of3.json', 'w') as f:
    json.dump(all_voters, f)

