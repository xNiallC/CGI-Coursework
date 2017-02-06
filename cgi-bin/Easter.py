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
    easterYear = easterForm.getvalue('easterYear', 'a')
    displayType = int(easterForm.getvalue('displayType'))
    easterYearFormatted = easterYear.strip()

    print("Content-Type: text/html; charset=utf-8")
    print("")
    print("<!DOCTYPE HTML>")
    print("<html>")
    print("<head>")
    print("<link href=\"https://fonts.googleapis.com/css?family=Lato:100,300,400,700,900\" rel=\"stylesheet\" />")
    print("<link rel=\"stylesheet\" type=\"text/css\" href=\"../stylesheetCGI.css\" />")
    print("<title>Finding Easter</title>")
    print("</head>")
    print("<body>")
    if easterYearFormatted.isdigit() == False:
        print("<h1>404: Easter Not Found</h1>")
        print("<br>")
        print("<img src=\"../img/easter.png\">")
        print("Invalid Input. Please try again. :-)")
        print("</body>")
        print("</html>")   
    else:
        easterYearInt = int(easterYearFormatted)
        print("<h1>You found Easter!</h1>")
        print("<br>")
        print("<img src=\"../img/easter.png\">")
        print("In the year " + str(easterYear) + ", easter will occur on:")
        print("<div class=\"easter\">")
        print("<br>")
        print(easter(easterYearInt, displayType))
        print("</div>")
        print("</body>")
        print("</html>")

if __name__ == '__main__':
    main()
