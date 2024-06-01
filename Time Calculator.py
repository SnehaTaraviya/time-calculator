week=[
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
]

def add_time(start,duration,*args):

    [L,meridiem]=start.split(" ")
    [SH, SM] = L.split(":")
    [DH,DM]=duration.split(":")



    total_minutes=int(SM)+int(DM)
    total_hour=int(SH)+int(DH)
    days = 0
    if total_minutes >+ 60:
         total_minutes-=60
         total_hour+=1
    if total_minutes<10:
            total_minutes=f"{ total_minutes}".zfill(2)
    if total_hour>=12:
        t,r=divmod(total_hour,12)
        total_hour=r if r else total_hour
        if total_hour>12:
            total_hour=total_hour-((t-1)*12)
        if t>0:
            if meridiem == "PM":
                days=((t-1)//2)+1
            else:
                days=t//2

        if t>0 and t%2!=0:
            meridiem  = "AM" if meridiem=="PM" else "PM"

    new_time=str(total_hour) + ":"
    new_time += str(total_minutes) + f" {meridiem}"

    if args:
        day=args[0].title()
        if days>0:
            index=week.index(day)
            index+=days%7
            if index>6:
                index=index-7
            day=week[index]
        new_time+=f", {day}"

    if days==1:
        new_time+="(next day)".rjust(11)
    elif days>1:
        new_time+=f" ({days} days later)".rjust(11)

    return new_time



print(add_time("3:30 PM","3:10"))
print(add_time("11:30 AM","2:32","Monday"))
print(add_time("11:43 AM","00:20"))
print(add_time("10:10 PM","3:30"))
print(add_time("11:43 PM","24:20","tueSday"))
print(add_time("6:30 PM","205:12"))
print(add_time("5:01 AM","0:00"))
print(add_time("8:16 PM","466:02","tuesday"))