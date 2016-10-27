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
    passwordFile = open("admin.dat","r") # Opening Password File.
    print("[*] Opening Password List File\n")
    url = input("[+] Enter the url >>")

    if(url.endswith("/") != True):
        url2 = addSlash(url)
    else:
        url2 = url

    if(url2.startswith('http://') != True or url2.startswith("https://") != True):
        url3 = "http://" + url2
    else:
        url3 = url2

    print(url3)
    print("[*] Checking administrative login page:\n")

    while(True):
        adminLink = passwordFile.readline().rstrip()

        if not adminLink:
            break
        urlAdmin = url3 + adminLink

        urlStatus = requests.get(urlAdmin).status_code
        print("[!] The admin login page is not at %s" %urlAdmin)
        print(urlStatus)
        if(urlStatus == requests.codes.ok): # Checking Status Code if it is 200
            print("[+] Found admin page at %s" %urlAdmin)
            time.sleep(1)
            break;
Credit()
FindLogin()
