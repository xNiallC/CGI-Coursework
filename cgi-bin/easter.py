#!/usr/bin/python
import cgi, cgitb
import calendar

def easter(y, displayType):
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32

    if (4 <= p <= 20) or (24 <= p <= 30):
        daySuffix = "th"
    elif (p % 10) == 1:
        daySuffix = "st"
    elif (p % 10) == 2:
        daySuffix = "nd"
    else:
        daySuffix = "rd"

    if displayType == 1:
        return(str(p) + "/" + str(n) + "/" + str(y))

    if displayType == 2:
        return(str(p) + daySuffix + " of " + str(calendar.month_name[n]) + " " + str(y))

    if displayType == 3:
        return(str(p) + "/" + str(n) + "/" + str(y) + " | " + str(p) + daySuffix + " of " + str(calendar.month_name[n]) + " " + str(y))

def main():
    easterForm = cgi.FieldStorage()
    easterYear = int(easterForm.getvalue('easterYear'))
    displayType = int(easterForm.getvalue('displayType'))
    
    print("Content-Type: text/html; charset=utf-8")
    print("")
    print("<!DOCTYPE HTML>")
    print("<html>")
    print("<head><title>Finding Easter</title></head>")
    print("<body>")
    print(easter(easterYear, displayType))
    print("</body>")
    print("</html>")

if __name__ == '__main__':
    main()
