'''
The MIT License (MIT)

Copyright (c) 2016 Swornim Shrestha

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''
import requests #importing the library
import time

AdminList = open("admin.dat","r")

def Credit():
    print("Admin Login Finder From Swornim Shrestha")
    print("For any queries feel free to mail me at srestaswrnm@gmail.com\n\n\n\n\n")
    print("##########################")
    print("#       Created By       #")
    print("#     Swornim Shrestha   #")
    print("#    2016 July 1 Friday  #")
    print("#  srestaswrnm@gmail.com #")
    print("#                        #")
    print("##########################\n\n\n\n\n")

def addSlash(url):
    return url+"/"

def FindLogin():
    Admin = ""
    LoginFile = open("admin.dat","r")
    url = input("Enter the url >>")

    if(url.endswith("/") != True):
        url2 = addSlash(url)
    else:
        url2 = url

    if(url2.startswith('http://') != True or url2.startswith("https://") != True):
        url3 = "http://" + url2
    else:
        url3 = url2
    print(url3)
    print("Directories and links found having possiblities to be a admin logins are :\n")

    while(True):
        adminLink = LoginFile.readline()
        if not adminLink:
            break
        urlAdmin = url3 + adminLink
        print(urlAdmin)
        urlStatus = requests.get(urlAdmin).status_code
        print(urlStatus)
        if(urlStatus == 200):
            Admin =urlAdmin
            print(Admin)
            time.sleep(1)
Credit()
FindLogin()
