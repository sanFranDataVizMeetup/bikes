A series of python scripts to complete and append context data to existing bike crash data.

# How it works

Run the python script processData.py with the bike data JSON file as a parameter:

```
python processData.py sanfrancisco_crashes.json
```

# Modules

- addDay, add the day of the week (Monday-Sunday) and the type of day (Weekend or workday)
Fields added:
weekday: integer, 0 (Monday) to 6 (Sunday)
weekdayname: string
weekdaytype: integer, 0 (Workday) or 1 (Weekend day)
weekdaytypename: string, "Workday" or "Weekend day"