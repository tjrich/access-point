from tkinter import *
import os

########################################
#           TIMOTHY RICH               #
#       timothy.rich25@gmail.com       #
#           +27745243897               #
########################################

# *** THIS ONLY WORKS FOR WINDOWS 7 AND HIGHER ***

# This program allows you to create a hosted network,
# as well as to start and stop it.
# The 'Network Sharing' button only opens the 'Network Connections' window,
# but internet connection sharing must be done manually.


# functions

# creates new hosted network network
def createNetwork(ssid, password):
    command = "netsh wlan set hostednetwork ssid=" + str(ssid) + " key=" + str(password) + " mode=allow"
    os.system(command)

# start hosted network
def startNetwork():
    os.system("netsh wlan start hostednetwork")

# stop hosted network
def stopNetwork():
    os.system("netsh wlan stop hostednetwork")

# opens 'Network Connections' window
def netShare():
    os.system("ncpa.cpl")

# font config
labelfont = ("Impact",10)
buttonfont = ("Impact",7)

# main window
main_win = Tk()
main_win.title("Access Point")
main_win.geometry("370x270")
main_win.configure(background="black")
#
# SSID entry field
Label(main_win, text="SSID:",fg="white",bg="black",font=labelfont).grid(row=0,column=1, sticky=W,padx=10,pady=10)
ssidVar = StringVar()
ssid = Entry(main_win, textvariable=ssidVar)
ssid.grid(row=0,column=2, sticky=W,padx=10,pady=10)
#
# Password entry field
Label(main_win, text="PASSWORD:",fg="white",bg="black",font=labelfont).grid(row=1,column=1, sticky=W,padx=10,pady=10)
passVar = StringVar()
password = Entry(main_win, textvariable=passVar, show="*")
password.grid(row=1,column=2, sticky=W,padx=10,pady=10)
#
# clear fields function
def clear():
    ssid.delete(0,"end")
    password.delete(0,"end")

# define buttons
#
# clear fields button
clear_fields = Button(main_win, text="Clear Fields",command=lambda: clear())
clear_fields.grid(row=0,column=3,sticky=NSEW,padx=10,pady=10)
# create a new network
create_button = Button(main_win, text="Create Network", command=lambda: createNetwork(ssid.get(), password.get()))
create_button.grid(row=1,column=3, sticky=NSEW,padx=10,pady=10)
# start access point
start_button = Button(main_win, text="Start Network", command=startNetwork)
start_button.grid(row=2,column=1, sticky=NSEW,padx=10,pady=10)
# stop access point
stop_button = Button(main_win, text="Stop Network", command=stopNetwork)
stop_button.grid(row=3,column=1, sticky=NSEW,padx=10,pady=10)
# network sharing
netshare_button = Button(main_win, text="Network Sharing", command=netShare)
netshare_button.grid(row=4,column=1, sticky=NSEW,padx=10,pady=10)
# exit
exit_button = Button(main_win, text="Exit", command=main_win.destroy)
exit_button.grid(row=5,column=1, sticky=NSEW,padx=10,pady=10)

main_win.mainloop()
