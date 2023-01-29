import pandas as pd
import json
from collections import defaultdict
import time
import dask.bag as dd


with open('canvassed_voters.json') as voters:
    mailing = json.load(voters)
voters.close()

with open('canvassed_voters.json') as voters1:
    canvassed = json.load(voters1)
voters1.close()

with open('Text&Calledvoters.json') as voters2:
    called = json.load(voters2)
voters2.close()

with open('texted.json') as voters3:
    texted = json.load(voters3)
voters3.close()
total_in_precinct = defaultdict(int)
precinct_turnout = defaultdict(int)

with open('1of3.json') as voters4:
    v_all_1 = json.load(voters4)
voters4.close()


with open('2of3.json') as voters5:
    v_all_2 = json.load(voters5)
voters5.close()

with open('3of3.json') as voters6:
    v_all_3 = json.load(voters6)
voters6.close()

# with open('canvassed_voters.json') as voters7:
#     targeted = json.load(voters7)
# voters7.close()

with open('Harris1of3.json') as voters8:
    all1 = json.load(voters8)
voters8.close()

with open('Harris2of3.json') as voters9:
    all2 = json.load(voters9)
voters9.close()
#
with open('Harris1of3.json') as voters10:
    all3 = json.load(voters10)
voters10.close()



# all_voted = dict(dict(v_all_1, **v_all_2), **v_all_3)
# all_harris = dict(dict(all1, **all2), **all3)
#
# total_in_precinct = defaultdict(int)
# precinct_turnout = defaultdict(float)
#
# counter = 0
# for voter in all_harris:
#     total_in_precinct[str(all_harris[voter]["Precinct"])] += 1
#     if voter in all_voted:
#         precinct_turnout[str(all_harris[voter]["Precinct"])] += 1
#
# precinct_num = [9, 10, 11, 44, 46, 285, 347, 379]
# time.sleep(5)
#
# matched_up = {"Precinct": [], "Percentage": []}
# for i in precinct_num:
#     matched_up["Precinct"].append(str(i))
#     # print("total:", total_in_precinct[str(i)])
#     # print("turnout", precinct_turnout[str(i)])
#     matched_up["Percentage"].append(precinct_turnout[str(i)]/total_in_precinct[str(i)])
# print(pd.DataFrame(matched_up))
# pd.DataFrame(matched_up).to_pickle('percentage.pkl')

### number of voters contacted
### numbers of voters reached

df = {"Age": [], "Sex": [], "Zip": [], "Precinct": [], "Method": [], "Reached": [], "Day": [], "Voted": []}
df1 = {"Age": [], "Sex": [], "Zip": [], "Precinct": [], "Method": [], "Reached": [], "Day": [], "Voted": []}
df2 = {"Age": [], "Sex": [], "Zip": [], "Precinct": [], "Method": [], "Reached": [], "Day": [], "Voted": []}
df3 = {"Age": [], "Sex": [], "Zip": [], "Precinct": [], "Method": [], "Reached": [], "Day": [], "Voted": []}


# for voter in mailing.keys():
#     if voter in v_all_1:
#         df["Age"].append(int(v_all_1[voter]["Age"]))
#         df["Sex"].append(v_all_1[voter]["Sex"])
#         df["Zip"].append(v_all_1[voter]["Zip"])
#         df["Precinct"].append(int(v_all_1[voter]["Precinct"]))
#         df["Method"].append("M")
#         df["Reached"].append(True)
#         df["Day"].append(None)
#         df["Voted"].append(True)
#
#     elif voter in v_all_2:
#         df["Age"].append(int(v_all_2[voter]["Age"]))
#         df["Sex"].append(v_all_2[voter]["Sex"])
#         df["Zip"].append(v_all_2[voter]["Zip"])
#         df["Precinct"].append(int(v_all_2[voter]["Precinct"]))
#         df["Method"].append("M")
#         df["Reached"].append(True)
#         df["Day"].append(None)
#         df["Voted"].append(True)
#
#     elif voter in v_all_3:
#         df["Age"].append(int(v_all_3[voter]["Age"]))
#         df["Sex"].append(v_all_3[voter]["Sex"])
#         df["Zip"].append(v_all_3[voter]["Zip"])
#         df["Precinct"].append(int(v_all_3[voter]["Precinct"]))
#         df["Method"].append("M")
#         df["Reached"].append(True)
#         df["Day"].append(None)
#         df["Voted"].append(True)
#
#     else:
#         df["Age"].append(int(mailing[voter]["Age"]))
#         df["Sex"].append(mailing[voter]["Sex"])
#         df["Zip"].append(mailing[voter]["Zip"])
#         df["Precinct"].append(int(mailing[voter]["Precinct"][10:]))
#         df["Method"].append("M")
#         df["Reached"].append(True)
#         df["Day"].append(None)
#         df["Voted"].append(False)
#
# days_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# for id in range(1, 13):
#     days_month[id] = days_month[id - 1] + days_month[id]
#
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
#
#
# for voter in texted.keys():
#     if voter in v_all_1:
#         df3["Age"].append(int(v_all_1[voter]["Age"]))
#         df3["Sex"].append(v_all_1[voter]["Sex"])
#         df3["Zip"].append(v_all_1[voter]["Zip"])
#         df3["Precinct"].append(int(v_all_1[voter]["Precinct"]))
#         df3["Method"].append("T")
#         if texted[voter] == "incoming":
#             df3["Reached"].append(True)
#         else:
#             df3["Reached"].append(False)
#
#         s = texted[voter]['Date']
#         month = int(s[5:7])
#         day = int(s[8:10])
#         day_year = days_month[month - 1] + day
#         day_week = ((day_year - 1) % 7 + 5) % 7
#
#
#         df3["Day"].append(day_week)
#         df3["Voted"].append(True)
#
#     elif voter in v_all_2:
#         df3["Age"].append(int(v_all_2[voter]["Age"]))
#         df3["Sex"].append(v_all_2[voter]["Sex"])
#         df3["Zip"].append(v_all_2[voter]["Zip"])
#         df3["Precinct"].append(int(v_all_2[voter]["Precinct"]))
#         df3["Method"].append("T")
#         if texted[voter] == "incoming":
#             df3["Reached"].append(True)
#         else:
#             df3["Reached"].append(False)
#
#         s = texted[voter]['Date']
#         month = int(s[5:7])
#         day = int(s[8:10])
#         day_year = days_month[month - 1] + day
#         day_week = ((day_year - 1) % 7 + 5) % 7
#
#         df3["Day"].append(day_week)
#         df3["Voted"].append(True)
#
#     elif voter in v_all_3:
#         df3["Age"].append(int(v_all_3[voter]["Age"]))
#         df3["Sex"].append(v_all_3[voter]["Sex"])
#         df3["Zip"].append(v_all_3[voter]["Zip"])
#         df3["Precinct"].append(int(v_all_3[voter]["Precinct"]))
#         df3["Method"].append("T")
#         if texted[voter] == "incoming":
#             df3["Reached"].append(True)
#         else:
#             df3["Reached"].append(False)
#
#         s = texted[voter]['Date']
#         month = int(s[5:7])
#         day = int(s[8:10])
#         day_year = days_month[month - 1] + day
#         day_week = ((day_year - 1) % 7 + 5) % 7
#
#         df3["Day"].append(day_week)
#         df3["Voted"].append(True)
#
#     else:
#         df3["Age"].append(None)
#         df3["Sex"].append(None)
#         df3["Zip"].append(None)
#         df3["Precinct"].append(None)
#         df3["Method"].append("T")
#         if texted[voter] == "incoming":
#             df3["Reached"].append(True)
#         else:
#             df3["Reached"].append(False)
#
#         s = texted[voter]['Date']
#         month = int(s[5:7])
#         day = int(s[8:10])
#         day_year = days_month[month - 1] + day
#         day_week = ((day_year - 1) % 7 + 5) % 7
#
#         df3["Day"].append(day_week)
#         df3["Voted"].append(False)
#
#
# mail = pd.DataFrame(df)
# walk = pd.DataFrame(df1)
# call = pd.DataFrame(df2)
# text = pd.DataFrame(df3)
#
# pd.DataFrame(df).to_pickle('mail.pkl')
# pd.DataFrame(df1).to_pickle('walk.pkl')
# pd.DataFrame(df2).to_pickle('call.pkl')
# pd.DataFrame(df3).to_pickle('text.pkl')


precinct_num = [9, 10, 11, 44, 46, 285, 347, 379]

df = {"9" : {"ID": [], "Method" : [], "Age": [], "Sex": [], "Voted": []},
      "10" : {"ID": [], "Method" : [],"Age": [], "Sex": [], "Voted": []},
      "11" : {"ID": [], "Method" : [],"Age": [], "Sex": [], "Voted": []},
      "44" : {"ID": [], "Method" : [],"Age": [], "Sex": [], "Voted": []},
      "46" : {"ID": [], "Method" : [],"Age": [], "Sex": [], "Voted": []},
      "285" : {"ID": [], "Method" : [],"Age": [], "Sex": [], "Voted": []},
      "347" : {"ID": [], "Method" : [],"Age": [], "Sex": [], "Voted": []},
      "379" : {"ID": [], "Method" : [],"Age": [], "Sex": [], "Voted": []},
      }
#
# combined = dict(mailing, **targeted)
# print(combined)
#

for voter in mailing.keys():
    if voter in v_all_1:
        if int(v_all_1[voter]["Precinct"]) in precinct_num:
            df[v_all_1[voter]["Precinct"]]["Voted"].append(True)
            df[v_all_1[voter]["Precinct"]]["ID"].append(voter)
            df[v_all_1[voter]["Precinct"]]["Method"].append("M")
            df[v_all_1[voter]["Precinct"]]["Age"].append(None)
            df[v_all_1[voter]["Precinct"]]["Sex"].append(None)

    elif voter in v_all_2:
        if int(v_all_2[voter]["Precinct"]) in precinct_num:
            df[v_all_2[voter]["Precinct"]]["Voted"].append(True)
            df[v_all_2[voter]["Precinct"]]["ID"].append(voter)
            df[v_all_2[voter]["Precinct"]]["Method"].append("M")
            df[v_all_2[voter]["Precinct"]]["Age"].append(None)
            df[v_all_2[voter]["Precinct"]]["Sex"].append(None)

    elif voter in v_all_3:
        if int(v_all_3[voter]["Precinct"]) in precinct_num:
            df[v_all_3[voter]["Precinct"]]["Voted"].append(True)
            df[v_all_3[voter]["Precinct"]]["ID"].append(voter)
            df[v_all_3[voter]["Precinct"]]["Method"].append("M")
            df[v_all_3[voter]["Precinct"]]["Age"].append(None)
            df[v_all_3[voter]["Precinct"]]["Sex"].append(None)

    else:
        try:
            try:
                if int(all2[voter]["Precinct"]) in precinct_num:
                    df[all2[voter]["Precinct"]]["Voted"].append(False)
                    df[all2[voter]["Precinct"]]["ID"].append(voter)
                    df[all2[voter]["Precinct"]]["Method"].append("M")
                    df[all2[voter]["Precinct"]]["Age"].append(None)
                    df[all2[voter]["Precinct"]]["Sex"].append(None)
            except:
                pass
            try:
                if int(all1[voter]["Precinct"]) in precinct_num:
                    df[all1[voter]["Precinct"]]["Voted"].append(False)
                    df[all1[voter]["Precinct"]]["ID"].append(voter)
                    df[all1[voter]["Precinct"]]["Method"].append("M")
                    df[all1[voter]["Precinct"]]["Age"].append(None)
                    df[all1[voter]["Precinct"]]["Sex"].append(None)
            except:
                pass
            try:
                if int(all3[voter]["Precinct"]) in precinct_num:
                    df[all3[voter]["Precinct"]]["Voted"].append(False)
                    df[all3[voter]["Precinct"]]["ID"].append(voter)
                    df[all3[voter]["Precinct"]]["Method"].append("M")
                    df[all3[voter]["Precinct"]]["Age"].append(None)
                    df[all3[voter]["Precinct"]]["Sex"].append(None)
            except:
                pass
        finally:
            pass

print(df)




for voter in called.keys():
    if voter in v_all_1:
        if int(v_all_1[voter]["Precinct"]) in precinct_num:
            df[v_all_1[voter]["Precinct"]]["Age"].append(int(v_all_1[voter]["Age"]))
            df[v_all_1[voter]["Precinct"]]["Sex"].append(v_all_1[voter]["Sex"])
            df[v_all_1[voter]["Precinct"]]["Voted"].append(True)
            df[v_all_1[voter]["Precinct"]]["ID"].append(voter)
            df[v_all_1[voter]["Precinct"]]["Method"].append("C")

    elif voter in v_all_2:
        if int(v_all_2[voter]["Precinct"]) in precinct_num:
            df[v_all_2[voter]["Precinct"]]["Age"].append(int(v_all_2[voter]["Age"]))
            df[v_all_2[voter]["Precinct"]]["Sex"].append(v_all_2[voter]["Sex"])
            df[v_all_2[voter]["Precinct"]]["Voted"].append(True)
            df[v_all_2[voter]["Precinct"]]["ID"].append(voter)
            df[v_all_2[voter]["Precinct"]]["Method"].append("C")

    elif voter in v_all_3:
        if int(v_all_3[voter]["Precinct"]) in precinct_num:
            df[v_all_3[voter]["Precinct"]]["Age"].append(int(v_all_3[voter]["Age"]))
            df[v_all_3[voter]["Precinct"]]["Sex"].append(v_all_3[voter]["Sex"])
            df[v_all_3[voter]["Precinct"]]["Voted"].append(True)
            df[v_all_3[voter]["Precinct"]]["ID"].append(voter)
            df[v_all_3[voter]["Precinct"]]["Method"].append("C")

    else:
        try:
            try:
                if int(all2[voter]["Precinct"]) in precinct_num:
                    df[all2[voter]["Precinct"]]["Voted"].append(False)
                    df[all2[voter]["Precinct"]]["ID"].append(voter)
                    df[all2[voter]["Precinct"]]["Method"].append("C")
                    df[all2[voter]["Precinct"]]["Age"].append(None)
                    df[all2[voter]["Precinct"]]["Sex"].append(None)
            except:
                pass
            try:
                if int(all1[voter]["Precinct"]) in precinct_num:
                    df[all1[voter]["Precinct"]]["Voted"].append(False)
                    df[all1[voter]["Precinct"]]["ID"].append(voter)
                    df[all1[voter]["Precinct"]]["Method"].append("C")
                    df[all1[voter]["Precinct"]]["Age"].append(None)
                    df[all1[voter]["Precinct"]]["Sex"].append(None)
            except:
                pass
            try:
                if int(all3[voter]["Precinct"]) in precinct_num:
                    df[all3[voter]["Precinct"]]["Voted"].append(False)
                    df[all3[voter]["Precinct"]]["ID"].append(voter)
                    df[all3[voter]["Precinct"]]["Method"].append("C")
                    df[all3[voter]["Precinct"]]["Age"].append(None)
                    df[all3[voter]["Precinct"]]["Sex"].append(None)
            except:
                pass
        finally:
            pass

for voter in texted.keys():
    if voter in v_all_1:
        if int(v_all_1[voter]["Precinct"]) in precinct_num:
            df[v_all_1[voter]["Precinct"]]["Age"].append(int(v_all_1[voter]["Age"]))
            df[v_all_1[voter]["Precinct"]]["Sex"].append(v_all_1[voter]["Sex"])
            df[v_all_1[voter]["Precinct"]]["Voted"].append(True)
            df[v_all_1[voter]["Precinct"]]["ID"].append(voter)
            df[v_all_1[voter]["Precinct"]]["Method"].append("T")

    elif voter in v_all_2:
        if int(v_all_2[voter]["Precinct"]) in precinct_num:
            df[v_all_2[voter]["Precinct"]]["Age"].append(int(v_all_2[voter]["Age"]))
            df[v_all_2[voter]["Precinct"]]["Sex"].append(v_all_2[voter]["Sex"])
            df[v_all_2[voter]["Precinct"]]["Voted"].append(True)
            df[v_all_2[voter]["Precinct"]]["ID"].append(voter)
            df[v_all_2[voter]["Precinct"]]["Method"].append("T")

    elif voter in v_all_3:
        if int(v_all_3[voter]["Precinct"]) in precinct_num:
            df[v_all_3[voter]["Precinct"]]["Age"].append(int(v_all_3[voter]["Age"]))
            df[v_all_3[voter]["Precinct"]]["Sex"].append(v_all_3[voter]["Sex"])
            df[v_all_3[voter]["Precinct"]]["Voted"].append(True)
            df[v_all_3[voter]["Precinct"]]["ID"].append(voter)
            df[v_all_3[voter]["Precinct"]]["Method"].append("T")

    else:
        try:
            try:
                if int(all2[voter]["Precinct"]) in precinct_num:
                    df[all2[voter]["Precinct"]]["Voted"].append(False)
                    df[all2[voter]["Precinct"]]["ID"].append(voter)
                    df[all2[voter]["Precinct"]]["Method"].append("T")
                    df[all2[voter]["Precinct"]]["Age"].append(None)
                    df[all2[voter]["Precinct"]]["Sex"].append(None)
            except:
                pass
            try:
                if int(all1[voter]["Precinct"]) in precinct_num:
                    df[all1[voter]["Precinct"]]["Voted"].append(False)
                    df[all1[voter]["Precinct"]]["ID"].append(voter)
                    df[all1[voter]["Precinct"]]["Method"].append("T")
                    df[all1[voter]["Precinct"]]["Age"].append(None)
                    df[all1[voter]["Precinct"]]["Sex"].append(None)
            except:
                pass
            try:
                if int(all3[voter]["Precinct"]) in precinct_num:
                    df[all3[voter]["Precinct"]]["Voted"].append(False)
                    df[all3[voter]["Precinct"]]["ID"].append(voter)
                    df[all3[voter]["Precinct"]]["Method"].append("T")
                    df[all3[voter]["Precinct"]]["Age"].append(None)
                    df[all3[voter]["Precinct"]]["Sex"].append(None)
            except:
                pass
        finally:
            pass
#
# print(df)


for voter in canvassed.keys():
    if voter in v_all_1:
        if int(v_all_1[voter]["Precinct"]) in precinct_num:
            df[v_all_1[voter]["Precinct"]]["Age"].append(int(v_all_1[voter]["Age"]))
            df[v_all_1[voter]["Precinct"]]["Sex"].append(v_all_1[voter]["Sex"])
            df[v_all_1[voter]["Precinct"]]["Voted"].append(True)
            df[v_all_1[voter]["Precinct"]]["ID"].append(voter)
            df[v_all_1[voter]["Precinct"]]["Method"].append("W")

    elif voter in v_all_2:
        if int(v_all_2[voter]["Precinct"]) in precinct_num:
            df[v_all_2[voter]["Precinct"]]["Age"].append(int(v_all_2[voter]["Age"]))
            df[v_all_2[voter]["Precinct"]]["Sex"].append(v_all_2[voter]["Sex"])
            df[v_all_2[voter]["Precinct"]]["Voted"].append(True)
            df[v_all_2[voter]["Precinct"]]["ID"].append(voter)
            df[v_all_2[voter]["Precinct"]]["Method"].append("W")

    elif voter in v_all_3:
        if int(v_all_3[voter]["Precinct"]) in precinct_num:
            df[v_all_3[voter]["Precinct"]]["Age"].append(int(v_all_3[voter]["Age"]))
            df[v_all_3[voter]["Precinct"]]["Sex"].append(v_all_3[voter]["Sex"])
            df[v_all_3[voter]["Precinct"]]["Voted"].append(True)
            df[v_all_3[voter]["Precinct"]]["ID"].append(voter)
            df[v_all_3[voter]["Precinct"]]["Method"].append("W")

    else:
        try:
            try:
                if int(all2[voter]["Precinct"]) in precinct_num:
                    df[all2[voter]["Precinct"]]["Voted"].append(False)
                    df[all2[voter]["Precinct"]]["ID"].append(voter)
                    df[all2[voter]["Precinct"]]["Method"].append("W")
                    df[all2[voter]["Precinct"]]["Age"].append(None)
                    df[all2[voter]["Precinct"]]["Sex"].append(None)
            except:
                pass
            try:
                if int(all1[voter]["Precinct"]) in precinct_num:
                    df[all1[voter]["Precinct"]]["Voted"].append(False)
                    df[all1[voter]["Precinct"]]["ID"].append(voter)
                    df[all1[voter]["Precinct"]]["Method"].append("C")
                    df[all1[voter]["Precinct"]]["Age"].append(None)
                    df[all1[voter]["Precinct"]]["Sex"].append(None)
            except:
                pass
            try:
                if int(all3[voter]["Precinct"]) in precinct_num:
                    df[all3[voter]["Precinct"]]["Voted"].append(False)
                    df[all3[voter]["Precinct"]]["ID"].append(voter)
                    df[all3[voter]["Precinct"]]["Method"].append("C")
                    df[all3[voter]["Precinct"]]["Age"].append(None)
                    df[all3[voter]["Precinct"]]["Sex"].append(None)
            except:
                pass
        finally:
            pass
#

with open('/Users/grego/PycharmProjects/DataThon/matched_up.json', 'w') as f:
     json.dump(df, f)







