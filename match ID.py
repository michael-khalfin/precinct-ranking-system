import pandas as pd
import json

# canvassed_voters = json.loads('canvassed_voters.json')
# text_called_voters = json.loads('Text&Calledvoters.json')
# phone_banking_voters = json.loads('texted.json')

with open('voters.json') as voters:
    mailing = json.load(voters)

with open('canvassed_voters.json') as voters1:
    canvassed = json.load(voters1)

with open('Text&Calledvoters.json') as voters2:
    called = json.load(voters2)

with open('texted.json') as voters3:
    texted = json.load(voters3)

with open('1of3.json') as voters4:
    v_all_1 = json.load(voters4)

with open('2of3.json') as voters5:
    v_all_2 = json.load(voters5)

with open('3of3.json') as voters6:
    v_all_3 = json.load(voters6)

### number of voters contacted
### numbers of voters reached

df = {"Age": [], "Sex": [], "Zip": [], "Precinct": [], "Method": [], "Reached": [], "Day": [], "Voted": []}
df1 = {"Age": [], "Sex": [], "Zip": [], "Precinct": [], "Method": [], "Reached": [], "Day": [], "Voted": []}
df2 = {"Age": [], "Sex": [], "Zip": [], "Precinct": [], "Method": [], "Reached": [], "Day": [], "Voted": []}
df3 = {"Age": [], "Sex": [], "Zip": [], "Precinct": [], "Method": [], "Reached": [], "Day": [], "Voted": []}

# for voter in mailing.keys():
#     if voter in v_all_1:
#         df["Age"].append(v_all_1[voter]["Age"])
#         df["Sex"].append(v_all_1[voter]["Sex"])
#         df["Zip"].append(v_all_1[voter]["Zip"])
#         df["Precinct"].append(v_all_1[voter]["Precinct"])
#         df["Method"].append("M")
#         df["Method"].append(v_all_1[voter]["Day"])
#         v_all_1[voter]["Voted"]

for voter in mailing.keys():
    if voter in v_all_1:
        df["Age"].append(int(v_all_1[voter]["Age"]))
        df["Sex"].append(v_all_1[voter]["Sex"])
        df["Zip"].append(v_all_1[voter]["Zip"])
        df["Precinct"].append(int(v_all_1[voter]["Precinct"]))
        df["Method"].append("M")
        df["Reached"].append(True)
        df["Day"].append(None)
        df["Voted"].append(True)

    elif voter in v_all_2:
        df["Age"].append(int(v_all_2[voter]["Age"]))
        df["Sex"].append(v_all_2[voter]["Sex"])
        df["Zip"].append(v_all_2[voter]["Zip"])
        df["Precinct"].append(int(v_all_2[voter]["Precinct"]))
        df["Method"].append("M")
        df["Reached"].append(True)
        df["Day"].append(None)
        df["Voted"].append(True)

    elif voter in v_all_3:
        df["Age"].append(int(v_all_3[voter]["Age"]))
        df["Sex"].append(v_all_3[voter]["Sex"])
        df["Zip"].append(v_all_3[voter]["Zip"])
        df["Precinct"].append(int(v_all_3[voter]["Precinct"]))
        df["Method"].append("M")
        df["Reached"].append(True)
        df["Day"].append(None)
        df["Voted"].append(True)

    else:
        df["Age"].append(int(mailing[voter]["Age"]))
        df["Sex"].append(mailing[voter]["Sex"])
        df["Zip"].append(mailing[voter]["Zip"])
        df["Precinct"].append(int(mailing[voter]["Precinct"][9:]))
        df["Method"].append("M")
        df["Reached"].append(True)
        df["Day"].append(None)
        df["Voted"].append(False)

days_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for id in range(1, 13):
    days_month[id] = days_month[id - 1] + days_month[id]

for voter in canvassed.keys():
    if voter in v_all_1:
        df1["Age"].append(int(v_all_1[voter]["Age"]))
        df1["Sex"].append(v_all_1[voter]["Sex"])
        df1["Zip"].append(v_all_1[voter]["Zip"])
        df1["Precinct"].append(int(v_all_1[voter]["Precinct"]))
        df1["Method"].append("W")
        if canvassed[voter] != "Not Home":
            df1["Reached"].append(True)
        else:
            df1["Reached"].append(False)

        s = canvassed[voter]['Date']
        month = int(s[5:7])
        day = int(s[8:10])
        day_year = days_month[month - 1] + day
        day_week = ((day_year - 1) % 7 + 5) % 7


        df1["Day"].append(day_week)
        df1["Voted"].append(True)

    elif voter in v_all_2:
        df1["Age"].append(int(v_all_2[voter]["Age"]))
        df1["Sex"].append(v_all_2[voter]["Sex"])
        df1["Zip"].append(v_all_2[voter]["Zip"])
        df1["Precinct"].append(int(v_all_2[voter]["Precinct"]))
        df1["Method"].append("W")
        if canvassed[voter] != "Not Home":
            df1["Reached"].append(True)
        else:
            df1["Reached"].append(False)

        s = canvassed[voter]['Date']
        month = int(s[5:7])
        day = int(s[8:10])
        day_year = days_month[month - 1] + day
        day_week = ((day_year - 1) % 7 + 5) % 7

        df1["Day"].append(day_week)
        df1["Voted"].append(True)

    elif voter in v_all_3:
        df1["Age"].append(int(v_all_3[voter]["Age"]))
        df1["Sex"].append(v_all_3[voter]["Sex"])
        df1["Zip"].append(v_all_3[voter]["Zip"])
        df1["Precinct"].append(int(v_all_3[voter]["Precinct"]))
        df1["Method"].append("W")
        if canvassed[voter] != "Not Home":
            df1["Reached"].append(True)
        else:
            df1["Reached"].append(False)

        s = canvassed[voter]['Date']
        month = int(s[5:7])
        day = int(s[8:10])
        day_year = days_month[month - 1] + day
        day_week = ((day_year - 1) % 7 + 5) % 7

        df1["Day"].append(day_week)
        df1["Voted"].append(True)

    else:
        df1["Age"].append(None)
        df1["Sex"].append(None)
        df1["Zip"].append(canvassed[voter]["Zip"])
        df1["Precinct"].append(None)
        df1["Method"].append("W")
        if canvassed[voter] != "Not Home":
            df1["Reached"].append(True)
        else:
            df1["Reached"].append(False)

        s = canvassed[voter]['Date']
        month = int(s[5:7])
        day = int(s[8:10])
        day_year = days_month[month - 1] + day
        day_week = ((day_year - 1) % 7 + 5) % 7

        df1["Day"].append(day_week)
        df1["Voted"].append(False)


for voter in called.keys():
    if voter in v_all_1:
        df2["Age"].append(int(v_all_1[voter]["Age"]))
        df2["Sex"].append(v_all_1[voter]["Sex"])
        df2["Zip"].append(v_all_1[voter]["Zip"])
        df2["Precinct"].append(int(v_all_1[voter]["Precinct"]))
        df2["Method"].append("C")
        if called[voter] == "Talked to Correct Person":
            df2["Reached"].append(True)
        else:
            df2["Reached"].append(False)

        s = called[voter]['Date'].split('/')
        month = int(s[0])
        day = int(s[1])
        day_year = days_month[month - 1] + day
        day_week = ((day_year - 1) % 7 + 5) % 7


        df2["Day"].append(day_week)
        df2["Voted"].append(True)

    elif voter in v_all_2:
        df2["Age"].append(int(v_all_2[voter]["Age"]))
        df2["Sex"].append(v_all_2[voter]["Sex"])
        df2["Zip"].append(v_all_2[voter]["Zip"])
        df2["Precinct"].append(int(v_all_2[voter]["Precinct"]))
        df2["Method"].append("C")
        if called[voter] == "Talked to Correct Person":
            df2["Reached"].append(True)
        else:
            df2["Reached"].append(False)

        s = called[voter]['Date'].split('/')
        month = int(s[0])
        day = int(s[1])
        day_year = days_month[month - 1] + day
        day_week = ((day_year - 1) % 7 + 5) % 7

        df2["Day"].append(day_week)
        df2["Voted"].append(True)

    elif voter in v_all_3:
        df2["Age"].append(int(v_all_3[voter]["Age"]))
        df2["Sex"].append(v_all_3[voter]["Sex"])
        df2["Zip"].append(v_all_3[voter]["Zip"])
        df2["Precinct"].append(int(v_all_3[voter]["Precinct"]))
        df2["Method"].append("C")
        if called[voter] == "Talked to Correct Person":
            df2["Reached"].append(True)
        else:
            df2["Reached"].append(False)

        s = called[voter]['Date'].split('/')
        month = int(s[0])
        day = int(s[1])
        day_year = days_month[month - 1] + day
        day_week = ((day_year - 1) % 7 + 5) % 7

        df2["Day"].append(day_week)
        df2["Voted"].append(True)

    else:
        df2["Age"].append(None)
        df2["Sex"].append(None)
        df2["Zip"].append(None)
        df2["Precinct"].append(None)
        df2["Method"].append("C")
        if called[voter] == "Talked to Correct Person":
            df2["Reached"].append(True)
        else:
            df2["Reached"].append(False)

        s = called[voter]['Date'].split('/')
        month = int(s[0])
        day = int(s[1])
        day_year = days_month[month - 1] + day
        day_week = ((day_year - 1) % 7 + 5) % 7

        df2["Day"].append(day_week)
        df2["Voted"].append(False)

# for voter in canvassed.keys():
#     if voter in v_all_1:
#         df1["Age"].append(int(v_all_1[voter]["Age"]))
#         df1["Sex"].append(v_all_1[voter]["Sex"])
#         df1["Zip"].append(v_all_1[voter]["Zip"])
#         df1["Precinct"].append(int(v_all_1[voter]["Precinct"]))
#         df1["Method"].append("W")
#         if canvassed[voter] != "Not Home":
#             df1["Reached"].append(True)
#         else:
#             df1["Reached"].append(False)
#
#         s = canvassed[voter]['Date']
#         month = int(s[5:7])
#         day = int(s[8:10])
#         day_year = days_month[month - 1] + day
#         day_week = ((day_year - 1) % 7 + 5) % 7
#
#
#         df1["Day"].append(day_week)
#         df1["Voted"].append(True)
#
#     elif voter in v_all_2:
#         df1["Age"].append(int(v_all_2[voter]["Age"]))
#         df1["Sex"].append(v_all_2[voter]["Sex"])
#         df1["Zip"].append(v_all_2[voter]["Zip"])
#         df1["Precinct"].append(int(v_all_2[voter]["Precinct"]))
#         df1["Method"].append("W")
#         if canvassed[voter] != "Not Home":
#             df1["Reached"].append(True)
#         else:
#             df1["Reached"].append(False)
#
#         s = canvassed[voter]['Date']
#         month = int(s[5:7])
#         day = int(s[8:10])
#         day_year = days_month[month - 1] + day
#         day_week = ((day_year - 1) % 7 + 5) % 7
#
#         df1["Day"].append(day_week)
#         df1["Voted"].append(True)
#
#     elif voter in v_all_3:
#         df1["Age"].append(int(v_all_3[voter]["Age"]))
#         df1["Sex"].append(v_all_3[voter]["Sex"])
#         df1["Zip"].append(v_all_3[voter]["Zip"])
#         df1["Precinct"].append(int(v_all_3[voter]["Precinct"]))
#         df1["Method"].append("W")
#         if canvassed[voter] != "Not Home":
#             df1["Reached"].append(True)
#         else:
#             df1["Reached"].append(False)
#
#         s = canvassed[voter]['Date']
#         month = int(s[5:7])
#         day = int(s[8:10])
#         day_year = days_month[month - 1] + day
#         day_week = ((day_year - 1) % 7 + 5) % 7
#
#         df1["Day"].append(day_week)
#         df1["Voted"].append(True)
#
#     else:
#         df1["Age"].append(None)
#         df1["Sex"].append(None)
#         df1["Zip"].append(canvassed[voter]["Zip"])
#         df1["Precinct"].append(None)
#         df1["Method"].append("W")
#         if canvassed[voter] != "Not Home":
#             df1["Reached"].append(True)
#         else:
#             df1["Reached"].append(False)
#
#         s = canvassed[voter]['Date']
#         month = int(s[5:7])
#         day = int(s[8:10])
#         day_year = days_month[month - 1] + day
#         day_week = ((day_year - 1) % 7 + 5) % 7
#
#         df1["Day"].append(day_week)
#         df1["Voted"].append(False)
#
# for voter in called.keys():
#     if voter in v_all_1:
#         df2["Age"].append(int(v_all_1[voter]["Age"]))
#         df2["Sex"].append(v_all_1[voter]["Sex"])
#         df2["Zip"].append(v_all_1[voter]["Zip"])
#         df2["Precinct"].append(int(v_all_1[voter]["Precinct"]))
#         df2["Method"].append("C")
#         if called[voter] == "Talked to Correct Person":
#             df2["Reached"].append(True)
#         else:
#             df2["Reached"].append(False)
#
#         s = called[voter]['Date'].split('/')
#         month = int(s[0])
#         day = int(s[1])
#         day_year = days_month[month - 1] + day
#         day_week = ((day_year - 1) % 7 + 5) % 7
#
#
#         df2["Day"].append(day_week)
#         df2["Voted"].append(True)
#
#     elif voter in v_all_2:
#         df2["Age"].append(int(v_all_2[voter]["Age"]))
#         df2["Sex"].append(v_all_2[voter]["Sex"])
#         df2["Zip"].append(v_all_2[voter]["Zip"])
#         df2["Precinct"].append(int(v_all_2[voter]["Precinct"]))
#         df2["Method"].append("C")
#         if called[voter] == "Talked to Correct Person":
#             df2["Reached"].append(True)
#         else:
#             df2["Reached"].append(False)
#
#         s = called[voter]['Date'].split('/')
#         month = int(s[0])
#         day = int(s[1])
#         day_year = days_month[month - 1] + day
#         day_week = ((day_year - 1) % 7 + 5) % 7
#
#         df2["Day"].append(day_week)
#         df2["Voted"].append(True)
#
#     elif voter in v_all_3:
#         df2["Age"].append(int(v_all_3[voter]["Age"]))
#         df2["Sex"].append(v_all_3[voter]["Sex"])
#         df2["Zip"].append(v_all_3[voter]["Zip"])
#         df2["Precinct"].append(int(v_all_3[voter]["Precinct"]))
#         df2["Method"].append("C")
#         if called[voter] == "Talked to Correct Person":
#             df2["Reached"].append(True)
#         else:
#             df2["Reached"].append(False)
#
#         s = called[voter]['Date'].split('/')
#         month = int(s[0])
#         day = int(s[1])
#         day_year = days_month[month - 1] + day
#         day_week = ((day_year - 1) % 7 + 5) % 7
#
#         df2["Day"].append(day_week)
#         df2["Voted"].append(True)
#
#     else:
#         df2["Age"].append(None)
#         df2["Sex"].append(None)
#         df2["Zip"].append(None)
#         df2["Precinct"].append(None)
#         df2["Method"].append("C")
#         if called[voter] == "Talked to Correct Person":
#             df2["Reached"].append(True)
#         else:
#             df2["Reached"].append(False)
#
#         s = called[voter]['Date'].split('/')
#         month = int(s[0])
#         day = int(s[1])
#         day_year = days_month[month - 1] + day
#         day_week = ((day_year - 1) % 7 + 5) % 7
#
#         df2["Day"].append(day_week)
#         df2["Voted"].append(False)


for voter in texted.keys():
    if voter in v_all_1:
        df3["Age"].append(int(v_all_1[voter]["Age"]))
        df3["Sex"].append(v_all_1[voter]["Sex"])
        df3["Zip"].append(v_all_1[voter]["Zip"])
        df3["Precinct"].append(int(v_all_1[voter]["Precinct"]))
        df3["Method"].append("T")
        if texted[voter] == "incoming":
            df3["Reached"].append(True)
        else:
            df3["Reached"].append(False)

        s = texted[voter]['Date']
        month = int(s[5:7])
        day = int(s[8:10])
        day_year = days_month[month - 1] + day
        day_week = ((day_year - 1) % 7 + 5) % 7


        df3["Day"].append(day_week)
        df3["Voted"].append(True)

    elif voter in v_all_2:
        df3["Age"].append(int(v_all_2[voter]["Age"]))
        df3["Sex"].append(v_all_2[voter]["Sex"])
        df3["Zip"].append(v_all_2[voter]["Zip"])
        df3["Precinct"].append(int(v_all_2[voter]["Precinct"]))
        df3["Method"].append("T")
        if texted[voter] == "incoming":
            df3["Reached"].append(True)
        else:
            df3["Reached"].append(False)

        s = texted[voter]['Date']
        month = int(s[5:7])
        day = int(s[8:10])
        day_year = days_month[month - 1] + day
        day_week = ((day_year - 1) % 7 + 5) % 7

        df3["Day"].append(day_week)
        df3["Voted"].append(True)

    elif voter in v_all_3:
        df3["Age"].append(int(v_all_3[voter]["Age"]))
        df3["Sex"].append(v_all_3[voter]["Sex"])
        df3["Zip"].append(v_all_3[voter]["Zip"])
        df3["Precinct"].append(int(v_all_3[voter]["Precinct"]))
        df3["Method"].append("T")
        if texted[voter] == "incoming":
            df3["Reached"].append(True)
        else:
            df3["Reached"].append(False)

        s = texted[voter]['Date']
        month = int(s[5:7])
        day = int(s[8:10])
        day_year = days_month[month - 1] + day
        day_week = ((day_year - 1) % 7 + 5) % 7

        df3["Day"].append(day_week)
        df3["Voted"].append(True)

    else:
        df3["Age"].append(None)
        df3["Sex"].append(None)
        df3["Zip"].append(None)
        df3["Precinct"].append(None)
        df3["Method"].append("T")
        if texted[voter] == "incoming":
            df3["Reached"].append(True)
        else:
            df3["Reached"].append(False)

        s = texted[voter]['Date']
        month = int(s[5:7])
        day = int(s[8:10])
        day_year = days_month[month - 1] + day
        day_week = ((day_year - 1) % 7 + 5) % 7

        df3["Day"].append(day_week)
        df3["Voted"].append(False)


mail = pd.DataFrame(df)
walk = pd.DataFrame(df1)
call = pd.DataFrame(df2)
text = pd.DataFrame(df3)

pd.DataFrame(df).to_pickle('mail.pkl')
pd.DataFrame(df1).to_pickle('walk.pkl')
pd.DataFrame(df2).to_pickle('call.pkl')
pd.DataFrame(df3).to_pickle('text.pkl')
# elif voter in canvassed:
#
# elif voter in called:
#
# elif voter in texted:










