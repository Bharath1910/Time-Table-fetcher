import sys
from prettytable import PrettyTable,from_csv
import datetime

now = datetime.datetime.today() #time right now

#TimeTable
Monday = ["Monday","English","Chemistry","Maths"]
Tuesday = ["Tuesday","Physics","CS","English"]
Wednesday = ["Wednesday","CS","Chemistry","Maths"]
Thursday = ["Thursday","Physics","CS","English"]
Friday = ["Friday","CS","Chemistry","Maths"]
Saturday = ["Saturday","Physics","English","CS"]

days = [
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday
        ]

#help Table 
Help = ["--help","Brings up this table"]
All = ["-all","Prints out the whole TimeTable"]
Today = ["-today","Prints out today's TimeTable"]
Next = ["-next","Prints out the next period of the today's TimeTable"]

commands = [
            Help,
            All,
            Today,
            Next
            ]

Total_time_table = PrettyTable()
Help_Table = PrettyTable()


Total_time_table.field_names = ["Day","1 (8:45 - 9:45)","2 (10:15 - 11:15)","3 (11:45 - 12:45)"]
Total_time_table.add_rows(days)

Help_Table.field_names = ["Command","Usage"]
Help_Table.add_rows(commands) 

Todays_time_table = Total_time_table.get_string(start=now.weekday())
Minute_Hour = now.hour,now.minute



if sys.argv[1] == "--help":
    print(Help_Table)

elif sys.argv[1] == "-today":
    if now.weekday() == 6:
        print("I appriciate your anticipation, but today is sunday.")
    
    else:
        print(Todays_time_table)

elif sys.argv[1] == "-all":
    print(Total_time_table)

elif sys.argv[1] == "-next":
    if Minute_Hour[0] <= 8 and Minute_Hour[1] <= 45:
        print(Todays_time_table(fields="1 (8:45 - 9:45)"))
    
    elif (Minute_Hour[0] > 8 and Minute_Hour[1] > 45) and (Minute_Hour[0] < 10 and Minute_Hour[1] < 15):
        print(Todays_time_table(fields="2 (10:15 - 11:15)"))
    
    elif (Minute_Hour[0] < 10 and Minute_Hour[1] > 15) and (Minute_Hour[0] < 11 and Minute_Hour[1] < 45):
        print(Todays_time_table(fields="3 (11:45 - 12:45)"))
    
    else:
        print("I appriciate your anticipation, but there is no class here after.")

elif sys.argv == None:
    print("Uh,oh.. I think you are in the wrong place, --help for more")

else:
    print("Uh,oh.. I think you are in the wrong place, --help for more")
