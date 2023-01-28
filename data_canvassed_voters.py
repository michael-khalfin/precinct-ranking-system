days_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for id in range(1,13):
        days_month[id] = days_month[id-1] + days_month[id]
    
    # print(days_month)
    
    # unique_days = defaultdict(int)
    
    for id in data.keys():
        s = data[id]['Date']
        print(s)
        month = int(s[5:7])
        day = int(s[8:10])
        # print(month)
        # print(day)
        day_year = days_month[month-1] + day
        # unique_days.add(day_year)
        # print(day_year)
        day_week = ((day_year - 1)%7 + 5)%7
        # unique_days[day_week] = unique_days[day_week] + 1
        # print(day_week)
        data[id]['Date'] = day_week
        print(data[id]['Date'])
