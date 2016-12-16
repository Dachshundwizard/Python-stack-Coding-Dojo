from datetime import datetime, time, date
# These classes are already written

# def main():
#     today = datetime.now()
#     wd = date.weekday(today)
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     print "Today is " + days[wd]

# def main():
#     today = datetime.now()
#     weekday = date.weekday(today)
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
#     print "Today's date is " + days[weekday] + ", " + today.strftime("%Y") + "."
#
# if __name__ == "__main__":
#     main();
#
# def main():
#     today = datetime.now()
#     print "Today's date is " + today.strftime("%A") + " the " + today.strftime("%d") + "th."
#     print today
#
# if __name__ == "__main__":
#     main();

def main():
    now =  datetime.now()
    print now.strftime("%c")
    print now.strftime("%x")
    print now.strftime("%X")
    print now.strftime("%I:%M:%S %p")
    print now.strftime("%H:%M")


if __name__=="__main__":
    main();
