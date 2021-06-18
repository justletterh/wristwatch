from os import get_terminal_size as get_size
from datetime import datetime as dt, timezone as timez, timedelta as td
from num2words import num2words as n2w
from math import trunc
from roman import toRoman as roman
from json import dumps as jd

months=[i.capitalize() for i in ".january.febuary.march.april.may.june.july.august.september.october.november.december".split(".")]
weekdays=[i.capitalize() for i in "monday.tuesday.wednesday.thursday.friday.saturday.sunday".split(".")]

p=lambda s:print("\n"+s+"\n")
j=lambda x:jd(x,indent=4)
div=lambda: print("-"*get_size().columns)
now=lambda tz=None:dt.now(tz)
n2o=lambda n:cap(n2w(n,to="ordinal"))

def cap(s,*,num=None):
    ss=""
    s=s.split(" ")
    for i in s:
        if i.lower() != "and":
            if not "-" in i:
                ss+=i.capitalize()
            else:
                ss+="-".join([x.capitalize() for x in i.split("-")])
        else:
            ss+=i
        ss+=" "
    while ss[-1].isspace():
        ss=ss[:-1]
    if type(num)==int:
        if num<=9:
            ss="Oh "+ss
    return ss

def main():
    w=lambda x:cap(n2w(x))
    n=now(timez(-td(hours=5)))
    d={}
    d["int_iso_weekday"]=n.isoweekday()
    d["int_weekday"]=n.weekday()
    d["word_weekday"]=weekdays[n.weekday()]
    d["int_day"]=n.day
    d["cardinal_day"]=w(n.day)
    d["ordinal_day"]=n2o(n.day)
    d["half_ordinal_day"]=cap(n2w(n.day,to="ordinal_num"))
    d["int_month"]=n.month
    d["word_month"]=months[n.month]
    d["int_year"]=n.year
    d["word_year"]=w(n.year)
    d["roman_year"]=roman(n.year)
    d["int_hour"]=n.hour
    d["word_hour"]=w(n.hour)
    d["int_minute"]=n.minute
    d["word_minute"]=cap(n2w(n.minute),num=n.minute)
    d["int_second"]=n.second
    d["word_second"]=w(n.second)
    us=n.microsecond
    d["int_millisecond"]=trunc(us/1000)
    d["word_millisecond"]=w(trunc(us/1000))
    d["int_microsecond"]=us-(trunc(us/1000)*1000)
    d["word_microsecond"]=w(us-(trunc(us/1000)*1000))
    print(j(d))

def init():
    div()
    p("Starting...")
    div()
    print()
    main()
    print()
    div()
    p("Done!!!")
    div()

if __name__ == "__main__":
    init()