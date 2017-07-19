# Current Py file Directory address
# /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/Security+_StudyApp.py
# =================
# Current txt file Directory address
# /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/SecurityPlus_StudyFile.txt
# =================
# ==================================================
# ==================================================
'''
Explanation to turn this .py file into a .exe file.

1) Download basic software:
    py2exe software --> http://www.py2exe.org/


'''
# ==================================================
# ==================================================
# ==================================================
'''
# ==================================================
We are creating an application to help study for the Security+ Exam

1) Created a standard start page with:
    a) direct button to the add info to a study file.
        Since we will be changing a file, you must click "agree" on a safety page
    b) Close the program button
    c) direct button to go to the study page

# ==================================================
2) Page to agree/disagree to alter the file that has the study info
    a) Agree = takes you to the change the file page
    b) Disagree automatically takes you back to the Start Page

# ==================================================
3) File organization. We are keeping our pages next to each other in program code.
    Methods, even if for specific pages will be together as well.
        1) Imports and globals
        2) Tkinter overall file page format
        3) Used Class objects
        4) Methods
        4) Pages

# ==================================================
4) We created a class for study objects
    When a user adds a study piece on the add page, it is added to the file line by line
    ...but when read off the file, the read method pulls it off as a class object.
        InputObject(---------------------
            Acronym:      DNS,
            Title:        Domain Name System,
            Port:         443,
            Protocol:     N/A
            TCP/UDP:      TCP
            Definition:   The internets system of converting alphabetic names into numeric IP addressses),

# ==================================================
5) We have a global list, we can call this list at any time from anywhere
        The global list is made from input class objects, currently has 6parts of user input
        We have to run the read function to update the list as a whole
        The end of the write function on the   addToStudyFilePage  appends the user input to the page on the spot

# ==================================================
6) File written per user input as:
###
Acronym:      FTP
Title:        File Transfer Protocol
Port:         21
Protocol:     N/A
TCP/UDP:      TCP
Definition:   The File Transfer Protocol (FTP) is a standard network protocol used for the transfer of computer files between a client and server on a computer network.FTP is built on a client-server model architecture and uses separate control and data connections between the client and the server.[1] FTP users may authenticate themselves with a clear-text sign-in protocol, normally in the form of a username and password, but can connect anonymously if the server is configured to allow it. For secure transmission that protects the username and password, and encrypts the content, FTP is often secured with SSL/TLS (FTPS). SSH File Transfer Protocol (SFTP) is sometimes also used instead; it is technologically different.The first FTP client applications were command-line programs developed before operating systems had graphical user interfaces, and are still shipped with most Windows, Unix, and Linux operating systems.[2][3] Many FTP clients and automation utilities have since been developed for desktops, servers, mobile devices, and hardware, and FTP has been incorporated into productivity applications, such as web page editors.

# ==================================================
7) File read from and turned into individual study objects, and each object is inserted into global list.
    This will be so that a user can get a single piece from an object and then call the remaining pieces
    User is shown:      FTP
    User can study and guess/know that that FTP stands for File Transfer Protocol
    User can click on: Show Title to check
    Program will display the title: File Transfer Protocol to confirm the user.
Global File Data =
[
InputObject(---------------------
Acronym:      FTP,
Title:        File Transfer Protocol,
Port:         21,
Protocol:     N/A,
TCP/UDP:      TCP,
Definition:   The File Transfer Protocol (FTP) is a standard network protocol used for the transfer of computer files between a client and server on a computer network.FTP is built on a client-server model architecture and uses separate control and data connections between the client and the server.[1] FTP users may authenticate themselves with a clear-text sign-in protocol, normally in the form of a username and password, but can connect anonymously if the server is configured to allow it. For secure transmission that protects the username and password, and encrypts the content, FTP is often secured with SSL/TLS (FTPS). SSH File Transfer Protocol (SFTP) is sometimes also used instead; it is technologically different.The first FTP client applications were command-line programs developed before operating systems had graphical user interfaces, and are still shipped with most Windows, Unix, and Linux operating systems.[2][3] Many FTP clients and automation utilities have since been developed for desktops, servers, mobile devices, and hardware, and FTP has been incorporated into productivity applications, such as web page editors.),
InputObject(---------------------
Acronym:      DNS,
Title:        Domain Name System,
Port:         N/A,
Protocol:     N/A,
TCP/UDP:      N/A,
Definition:   The Domain Name System (DNS) is a hierarchical decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities. ................cont.....
# ==================================================

'''
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# Imports Imports Imports Imports Imports Imports
from tkinter import *
import random # For the random number on from the study list (StudyPage)
import urllib
import json
# Terminal/CMD (we are on mac)
#   pip install pandas
#   pip install numpy
import pandas as pd
import numpy as np

# ==================================================
import tkinter as tk
from tkinter import ttk
'''
Terminal/CMD     pip install matplotlib
'''
import matplotlib
# This (below) lets us "change the back ground"
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

from matplotlib import pyplot as plt
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
style.use("ggplot")
XL_FONT  = ("Verdana", 30)  # Base font that we want to use and will call
LARGE_FONT = ("Verdana", 18)  # Base font that we want to use and will call
NORM_FONT = ("Verdana", 12)  # Base font that we want to use and will call
SMALL_FONT = ("Verdana", 10)  # Base font that we want to use and will call
# This is our global list. While the program is running this will be used with our study data
global global_fileData
global_fileData = []

global global_ChangeFilePAge_2_Position

# ==================================================
# ==================================================
# ==================================================
# This will change the size of the graph. Customize based on data and wants
# NOTE:     THIS refers to our bitcoin import graph.
# The study file does not have a graph currently.
f = Figure(figsize=(10, 6), dpi=100)  # Cut from GraphPage
a = f.add_subplot(111)  # Cut from GraphPage   # 111 means 1x1 on chart 1
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# START PRIMARY TK CLASS      PRIMARY TK CLASS        PRIMARY TK CLASS
# ==================================================
class SecurityPlus(tk.Tk):
    # Current Py file Directory
    # /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/Security+_StudyApp.py
    # =================
    # Current txt file Directory
    # /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/SecurityPlus_StudyFile.txt
    # =================
    '''
    Note: This is our primary page container format/configuration page for all pages.
        Set geometry, title, image(not working though)

        We have a menu that is not being used at the momemnt.

        We have a popup message coming from the menu selection, just for show at the moment.


     __init__ implies that this will be run automatically if the class is called.
         other def methods will not run automatically.
            args = arguments = open ended, you can pass whatever you want through
            kwargs = key-word arguments, basically dictionaries.
     '''
    def __init__(self, *args, **kwargs):
        # Now initialize tkinter also.
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.title(self, "NCT's Security+ Study App")
        tk.Tk.geometry(self, "800x1000")
        # Can't get the icon to show, now just a png icon
        # Resized to 12/16 pixels
        tk.Tk.iconbitmap(self, "icon.png")

        # =================
        container = ttk.Frame(self)
        # Making a quick window, use pack, for more detailed, use grid
        # side= What side do you want this on.
        # fill= Fill the entire space
        # expand= If there is any more white space in the window. Use it.
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Menubar block created in file 9
        # Create an overall menubar, and assign to this tkinter
        menuBar1 = tk.Menu(container)
        # Adding a tearoff divider into the menu that drops down
        fileMenu1 = tk.Menu(menuBar1, tearoff=0)
        # Now actually place a literal piece on the menubar
        menuBar1.add_cascade(label="File", menu=fileMenu1)
        # Create a subpiece under the File Tab
        # Currently Save Settings pulls up a popup
        # PopUp relies on method above, but doesn't do anything at the moment
        fileMenu1.add_command(label="Save Settings",
                              command=lambda: popupmsg("Msg sent from class SecurityPlus"))
        # Create a separator under the File Tab
        fileMenu1.add_separator()
        # Create a 2nd subpiece under the File Tab
        fileMenu1.add_command(label="Study Page", command=lambda: self.show_frame(StudyPage))
        fileMenu1.add_command(label="AddToFile Page", command=lambda: self.show_frame(AddToFilePage))
        fileMenu1.add_command(label="ChangeFile Page", command=lambda: self.show_frame(ChangeFilePAge))
        fileMenu1.add_command(label="KeyLogger Page", command=lambda: self.show_frame(KeyLoggerPage))
        fileMenu1.add_command(label="Exit", command=quit)
        # ==================================================
        # ==================================================
        # ==================================================
        # We are adding a new choice, and then 4 subchoices to the menubar options
        # Create the main new choice, will be on the main menu bar
        # Label the new menubar choice, "Exchange", and set its command to the new method.
        exchangeChoice1 = tk.Menu(menuBar1, tearoff=1)
        menuBar1.add_cascade(label="Exchange", menu=addToStudyResovoir)
        # ==================================================
        # ==================================================
        # -----Start Sub Choices-------------
        # These are tied to the global changeExchange method that we are creating up top.
        # We have our plot since File 8 tied to a U.S. bitcoin trader.
        # Eventually these 4 sub-choices will produce plots tied to foreign bitcoin traders.
        # We are sending two parts to the method, one is a label
        #       and the other is used by the program which can only use lowercase.
        exchangeChoice1.add_command(label="BTC-e",
                                    command=lambda: addToStudyResovoir("BTC-e", "btce"))

        exchangeChoice1.add_command(label="Bitfinex",
                                    command=lambda: addToStudyResovoir("Bitfinex", "bitfinex"))

        exchangeChoice1.add_command(label="Bitstamp",
                                    command=lambda: addToStudyResovoir("Bitstamp", "bitstamp"))

        exchangeChoice1.add_command(label="Huobi",
                                    command=lambda: addToStudyResovoir("Huobi", "huobi"))
        # -----End Sub Choices-------------
        # ==================================================
        tk.Tk.config(self, menu=menuBar1)
        # ----------------------------------------------------
        # ==================================================
        # Specify a dictionary here
        self.frames = {}
        # We will have numerous windows, and either click/button will bring another.
        # One application with numerous windows.
        # ==================================================
        # ==================================================
        # ==================================================
        # ===================FOR PAGE LOOP===============================
        # For loop that ranges in our page limits
        # Make sure to add any new page to our tuple for loop
        for F in (StartPage,
                  ConfirmAddPage,
                  AddToFilePage,
                  ChangeFilePAge,
                  KeyLoggerPage,
                  StudyPage):
            # Use F so that we can progress through our pages.
            frame = F(container, self)
            self.frames[F] = frame
            # grid is more specific compared to pack.
            # sticky is using North/South/East/West -->
            #    will stretch to the size of the window.
            #       if you just use ew then it will stretch all to the sides.
            frame.grid(row=0, column=0, sticky="nsew")
        # ==================================================
        # ==================================================
        self.show_frame(StartPage)
    # ==================================================
    # ==================================================
    # Set function to show a frame for a specific page.
    def show_frame(self, controller1):
        # self.frames is looking at the frame dictionary that we created above.
        #       Controller is which frame we want to access
        frame = self.frames[controller1]
        # Then we will run a library function on the frame.
        frame.tkraise()
# ==================================================
# END PRIMARY TK CLASS      PRIMARY TK CLASS        PRIMARY TK CLASS
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# START OBJECT CLASS OBJECT CLASS OBJECT CLASS
# START OBJECT CLASS OBJECT CLASS OBJECT CLASS
# START OBJECT CLASS OBJECT CLASS OBJECT CLASS
class inputObject:
    # We should store a user input as a class object with parts
    # We initially use this in the readTxtFile() method
    # We insert into the txt file, just line by line of user input
    # We read out the file and once we hit a   '###'   we know that the next 6 lines are object attributes.
    #    Take those 6 lines adn insert into an object of this class to match the input format.
    # Then take that object and insert into the global list.

    # This is built into class objects so we can easily keep track of how many we have every time we add 1
    numberOFStudyObjects = 0

    def __init__(self, acronym, title, port, protocol, tcp_udp, definition):
        # Now initialize tkinter also.
        self.acronym = str(acronym)
        self.title = str(title)
        self.port = str(port)
        self.protocol = str(protocol)
        self.tcp_udp = str(tcp_udp)
        self.definition = str(definition)


        # Just created an study object, increase the count
        self.numberOFStudyObjects += 1

    # -----------------------------------------------------------------
    #  Special Methods: NOTE Dunder = double + under
    '''Both repr and str are basically displays. repr is more techincal and for the programmer
        while str is more for a user. '''
    def __repr__(self):
        return "\nInputObject(---------------------\n{}, \n{}, \n{}, \n{}, \n{}, \n{})".format(
            self.acronym, self.title, self.port, self.protocol, self.tcp_udp, self.definition)
    # =======================
    def __str__(self, whichOne):
        if whichOne == "acronym":
            return '{}'.format(self.acronym)
            # Prints out:       Acronym:      FTP
        elif whichOne == "title":
            return '{}'.format(self.title)
        elif whichOne == "port":
            return '{}'.format(self.port)
        elif whichOne == "protocol":
            return '{}'.format(self.protocol)
        elif whichOne == "tcp_udp":
            return '{}'.format(self.tcp_udp)
        elif whichOne == "definition":
            return '{}'.format(self.definition)

        # ======================
    def __len__(self):
        return self.numberOFStudyObjects
        # =======================
        # =======================
        # =======================
# ==================================================
# ==================================================
# END OBJECT CLASS OBJECT CLASS OBJECT CLASS
# END OBJECT CLASS OBJECT CLASS OBJECT CLASS
# END OBJECT CLASS OBJECT CLASS OBJECT CLASS
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# START METHODS METHODS METHODS METHODS METHODS METHODS
# START METHODS METHODS METHODS METHODS METHODS METHODS
# START METHODS METHODS METHODS METHODS METHODS METHODS
# ==================================================
# ==================================================
# This section including addToStudyResovoir method is part of the menu in the BTC-e page.
exchange = "BTC-e"
datCounter = 9000
programName = "btce"

def addToStudyResovoir(toWhat, pn):
    global exchange
    global datCounter
    global programName

    exchange = toWhat
    programName = pn
    datCounter = 9000
# ==================================================
# ==================================================
# To get the popup window:
#       Run program: StartPage:  TradingPage:   Agree:  File:  Save Settings
def popupmsg(msg):
    # Create popup window, and set it's geometry
    '''
    Not used at the moment.
    '''
    popup = tk.Tk()
    popup.geometry("400x100")

    # Set the popup window title
    popup.wm_title("Title on top of File: Save Settings: popup")
    # Set a label in the popup window
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    # Set a button in the popup window with a command to destroy popup window
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()
# ==================================================
# ==================================================
# ==================================================
def readTxtFile(): #animate function with  'i' for interval
    '''
    The primary use is to open the file and pull objects from the file, into the global_list.
        There are several print options in here, that are used just for programmer show

    This is designed to read line by line since we remain consistent in our file writing,
        once we read in   '###'   we know that the next 6 lines are object attributes.
        Those 6 lines are read in, inserted into an object, then the object is inserted into the global list.

    We are working with the same global list, and the same file. This method is called numerous times to make
        sure that user has the most updated list on all pages.
    '''
    dataList1 = [line.rstrip('\n') for line in open('SecurityPlus_StudyFile.txt')]

    # =======================
    print("\nThat was the datalist as a variable, now the for loop: ")
    # Simple print out from the file.
    for x in dataList1:
        print(x)
        if x == "###":
            print("----------------")
        # =======================
        '''
            ###
            ----------------
            Acronym:     NCT
            Title:           Nate
            Port:           Charles
            Protocol:      Terry
            TCP/UDP:     UDP
            Definition:           I am a cyber security guy
            ###
        '''
    # =======================
    print("\n Check the y range (readTxtFile)")
    # Clear the global list, as we will be adding the entire txt file including the new piece.
    global_fileData[:] = []
    for y in range(0, len(dataList1)-1):
        # if line == ###  then we know the next 6 lines will be our attributes
        if dataList1[y] == "###":
            # Create an object and add it to the txt file.
            studyObject = inputObject(dataList1[y+1], dataList1[y+2], dataList1[y+3], dataList1[y+4], dataList1[y+5], dataList1[y+6])

            global_fileData.append(studyObject)
# ==================================================
# ==================================================
# ==================================================
def appendToTxtFile(acronym, title, port, protocol, TCP_UDP, definition): #animate function with  'i' for interval
    '''
    This method appends to  our text file
    This is called on the   AddToFilePage
        Called for user to add a full object to the file.
    '''
    writeData1 = open("SecurityPlus_StudyFile.txt", "a")

    # Print's are just for programmer show
    print("acronym    = " + acronym)
    print("title      = " + title)
    print("port       = " + port)
    print("protocol   = " + protocol)
    print("TCP_UDP    = " + TCP_UDP)
    print("definition = " + definition)

    # If the user does not input anything, we will write N/A
    if acronym == "":
        acronym = "N/A"
    # Remove /n from a single string. Keep as one piece. Only need for Definition, but be safe
    acronym = acronym.replace("\n", "")
    # -------------------
    if title == "":
        title = "N/A"
    # Remove /n from a single string. Keep as one piece. Only need for Definition, but be safe
    title = title.replace("\n", "")
    # -------------------
    if port == "":
        port = "N/A"
    # Remove /n from a single string. Keep as one piece. Only need for Definition, but be safe
    port = port.replace("\n", "")
    # -------------------
    if protocol == "":
        protocol = "N/A"
    # Remove /n from a single string. Keep as one piece. Only need for Definition, but be safe
    protocol = protocol.replace("\n", "")
    # -------------------
    if TCP_UDP == "":
        TCP_UDP = "N/A"
    # Remove /n from a single string. Keep as one piece. Only need for Definition, but be safe
    TCP_UDP = TCP_UDP.replace("\n", "")
    # -------------------
    if definition == "":
        definition = "N/A"
    # Remove /n from a single string. Keep as one piece.
    definition = definition.replace("\n", "")


    # Append the user input to the file as expected
    writeData1.write('###\n')
    writeData1.write("Acronym:     " + acronym + '\n')
    writeData1.write("Title:           " + title + '\n')
    writeData1.write("Port:           " + port + "\n")
    writeData1.write("Protocol:      " + protocol + "\n")
    writeData1.write("TCP/UDP:     " + TCP_UDP + "\n")
    writeData1.write("Definition:           " + definition + '\n')
    writeData1.close()


    studyObject2 = inputObject(acronym, title, port, protocol, TCP_UDP, definition)
    # Will call the global file later, but we have to run the read file to get it up to date
    global_fileData.append(studyObject2)
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# We have to re-write the file even for a one attribute change
#    Read in the file and place in list
#       Change a spot in that list.
#           Write list to file spot-->line
def changeTxtFile():
    '''
    Simple method to print the global-list to the file.
        This is called from the changeFilePage
        This rewrites the full file each time.
            Full rewrite is not efficient, but helps to remain consistant on a small scale like this.

    '''
    writeData1 = open("SecurityPlus_StudyFile.txt", "w")

    for x in global_fileData:

        # Append the user input to the file as expected
        writeData1.write('###\n')
        writeData1.write(x.acronym + '\n')
        writeData1.write(x.title + '\n')
        writeData1.write(x.port + "\n")
        writeData1.write(x.protocol + "\n")
        writeData1.write(x.tcp_udp + "\n")
        writeData1.write(x.definition + '\n')
    writeData1.close()
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# END METHODS METHODS METHODS METHODS METHODS METHODS
# END METHODS METHODS METHODS METHODS METHODS METHODS
# END METHODS METHODS METHODS METHODS METHODS METHODS
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# START PAGES PAGES PAGES PAGES PAGES PAGES PAGES
# START PAGES PAGES PAGES PAGES PAGES PAGES PAGES
# START PAGES PAGES PAGES PAGES PAGES PAGES PAGES
# ==================================================
# ==================================================
class StartPage(ttk.Frame):

    '''
    START PAGE
        Note: this page is on the pack format, not the grid
        Current: 5 Buttons - take user to page, or close program
            1) Study Page
                User can cycle through list and study objects
            2) Add to File Page
                User can add to txt-file, must click accept on confirm page
            3) Change the File Page
                User can adjust a specific object's attributes
            4) Key Logger page
                Simple display of user pressing buttons and being 'recorded'
                    Note: Space and right arrow are used in StudyPage
                    They seem to be permanently tied. Can't be used here?
            5) Quit Program


    '''
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font=XL_FONT)
        label.pack(padx=10, pady=10)

        # ----------------------------
        # ttk will give us a good looking button
        startPage_GOToStudyPageButton = ttk.Button(self, text="Study Page",
                                                   command=lambda: controller.show_frame(StudyPage), width=15)
        startPage_GOToStudyPageButton.pack(pady=(0,10))

        # ----------------------------
        # ttk will give us a good looking button
        startPage_addToStudyFilePageButton = ttk.Button(self, text="Add to File",
                                                 command=lambda: controller.show_frame(ConfirmAddPage), width=15)
        startPage_addToStudyFilePageButton.pack(pady=(0,10))

        # ----------------------------
        # ttk will give us a good looking button
        startPage_ChangeFilePAgePageButton = ttk.Button(self, text="Change the File",
                                                 command=lambda: controller.show_frame(ChangeFilePAge), width=15)
        startPage_ChangeFilePAgePageButton.pack(pady=(0,10))

         # ----------------------------
        # ttk will give us a good looking button
        startPage_keyLoggerPageButton = ttk.Button(self, text="Key Logger Page",
                                                 command=lambda: controller.show_frame(KeyLoggerPage), width=15)
        startPage_keyLoggerPageButton.pack(pady=(0,10))

        # ----------------------------
        # ttk will give us a good looking button
        startPage_CloseButton = ttk.Button(self, text="Close Program",
                                           command=quit, width=15)
        startPage_CloseButton.pack(pady=(0,10))
# ==================================================
# ==================================================
# ==================================================
# ==================================================
class ConfirmAddPage(ttk.Frame):
    # Simple confirmation page
    # Lets user agree that they will be changing the file
    # If user agrees, it will take them to the change page

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="The Study File", font=XL_FONT)
        label.pack(padx=10, pady=10)

        # ----------------------------
        askButton = ttk.Label(self, text="""Do you want to add information to your txt file?
        \nChange at your own risk.""", font=NORM_FONT)
        askButton.pack(padx=10, pady=10)

        # ----------------------------
        # ttk will give us a good looking button
        returHomeButtonf = ttk.Button(self, text="Return to Home Page",
                             command=lambda: controller.show_frame(StartPage))
        returHomeButtonf.pack()

        # ----------------------------
        bcte_label = ttk.Label(self, text="Click agree and you will be directed to the file changing page.", font=NORM_FONT)
        bcte_label.pack(padx=10, pady=10)

        # ----------------------------
        # This is our only link to our add to file page
        addToStudyFilePage_agreeButton = ttk.Button(self, text="Agree",
                                             command=lambda: controller.show_frame(AddToFilePage))
        addToStudyFilePage_agreeButton.pack()

        # ----------------------------
        # This will auto-take you back to the start of the program
        addToStudyFilePage_disagreeButton = ttk.Button(self, text="DisAgree",
                                                command=lambda: controller.show_frame(StartPage))
        addToStudyFilePage_disagreeButton.pack()
        # ----------------------------
# ==================================================
# ==================================================
# ==================================================
# ==================================================
class AddToFilePage(ttk.Frame):
    '''
        We are adding to the file in this way.
         ###
         Add Acronym:       DNS
         Add Title:         Domain Name System
         Related Port#:     21
         Add Protocol:      N/A
         TCP and/or UDP:    TCP
         Add Definition:    The Internet's system for converting alphabetic names into .........

     There are 6 entry boxes, all with examples, and titles for the user input.

     There are 3 buttons at the bottom of the page.
        Write Text File - as seen by the 7 lines above starting with '###' it will be written to the
                txt file based on those principles, since we have tailored this to storing and
                helping us with the security+ exam. It comes out in the file like:
                            ###
                            ----------------
                            Acronym:     NCT
                            Title:           Nate
                            Port:           Charles
                            Protocol:      Terry
                            TCP/UDP:     UDP
                            Definition:           I am a cyber security guy
                            ###
                The pound signs allow the program to visually separate along with a dash line.
                There is unique spacing between the value and the title, this just made it more
                    simple to import into the program.
        Read Text File - the method helps in many different ways throughout the program, but
                this button is just to help the programmer view what has been imported
                via the print function.
        Return to Home Page
    '''

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Add to Study File", font=XL_FONT)
        # 1st row, 2nd column, pushto right 40%
        label.grid(row=0, column=1, padx=40)
        # ------------------------
        warninglabel = ttk.Label(self, text="Note: If you leave a spot blank, we will auto-include 'N/A'",
                                 font=NORM_FONT)
        warninglabel.grid(row=1, column=1)
        # ------------------------
        warninglabel2 = ttk.Label(self, text="There are special characters that aren't accepted."
                                             "\nThe definition can be long, but keep it simple. ",
                                 font=NORM_FONT)
        warninglabel2.grid(row=2, column=1)

        # ------------------------
        spacerLabel = ttk.Label(self, text="", font=LARGE_FONT)
        # 1st row, 2nd column, pushto right 40%
        spacerLabel.grid(row=3, column=0, padx=20)
        # ------------------------
        # ------------------------
        # --------------------------------------------------------------
        acro_Label = ttk.Label(self, text="Add Acronym: ", font=LARGE_FONT)
        acro_Label.grid(row=4, column=0, sticky="W", padx=20)
        # -----
        acro_input = ttk.Entry(self, width=40)
        acro_input.grid(row=4, column=1, sticky="W")
        # -----
        acro_Example = ttk.Label(self, text="Ex: DNS ", font=NORM_FONT)
        acro_Example.grid(row=5, column=1, sticky="WE", padx=20, pady=(0,10))
        # --------------------------------------------------------------
        title_Label = ttk.Label(self, text="Add Title: ", font=LARGE_FONT)
        title_Label.grid(row=6, column=0, sticky="W", padx=20)
        # -----
        title_input = ttk.Entry(self, width=40)
        title_input.grid(row=6, column=1, sticky="W")
        # -----
        title_Example = ttk.Label(self, text="Ex: Domain Name System ", font=NORM_FONT)
        title_Example.grid(row=7, column=1, sticky="WE", padx=20, pady=(0,10))
        # --------------------------------------------------------------
        port_Label = ttk.Label(self, text="Related Port#: ", font=LARGE_FONT)
        port_Label.grid(row=8, column=0, sticky="W", padx=20)
        # -----
        port_input = ttk.Entry(self, width=40)
        port_input.grid(row=8, column=1, sticky="W")
        # -----
        port_Example = ttk.Label(self, text="Ex: 443 ", font=NORM_FONT)
        port_Example.grid(row=9, column=1, sticky="WE", padx=20, pady=(0,10))
        # --------------------------------------------------------------
        protocol_Label = ttk.Label(self, text="Add Protocol: ", font=LARGE_FONT)
        protocol_Label.grid(row=10, column=0, sticky="W", padx=20)
        # -----
        protocol_input = ttk.Entry(self, width=40)
        protocol_input.grid(row=10, column=1, sticky="W")
        # -----
        protocol_Example = ttk.Label(self, text="Ex: Secure Shell (SSH) (RFC 4250-4256) ", font=NORM_FONT)
        protocol_Example.grid(row=11, column=1, sticky="WE", padx=20, pady=(0,10))
        # --------------------------------------------------------------
        tcp_udp_Label = ttk.Label(self, text="TCP and/or UDP", font=LARGE_FONT)
        tcp_udp_Label.grid(row=12, column=0, sticky="W", padx=20)
        # -----
        tcp_udp_input = ttk.Entry(self, width=40)
        tcp_udp_input.grid(row=12, column=1, sticky="W")
        # -----
        tcp_udp_Example = ttk.Label(self, text="Ex: TCP ", font=NORM_FONT)
        tcp_udp_Example.grid(row=13, column=1, sticky="WE", padx=20, pady=(0,10))
        # --------------------------------------------------------------
        def_Label = ttk.Label(self, text="Add Definition: ", font=LARGE_FONT)
        def_Label.grid(row=14, column=0, sticky="W", padx=20)
        # -----
        def_input = ttk.Entry(self, width=40)
        def_input.grid(row=14, column=1, sticky="W")
        # -----
        acro_Example = ttk.Label(self, text="Ex: The Internet's system for converting"
                                            "\nalphabetic names into numeric IP addresses."
                                            "\nFor example, when a Web address (URL) is "
                                            "\ntyped into a browser, DNS servers return the "
                                            "\nIP address of the Web server associated with "
                                            "\nthat name. In this made-up example, the DNS "
                                            "\nconverts the URL www.company.com into the IP "
                                            "\naddress 204.0.8.51. Without DNS, you would have "
                                            "\nto type the series of four numbers and dots into "
                                            "\nyour browser to retrieve the website, which you "
                                            "\nactually can do. ", font=NORM_FONT)
        acro_Example.grid(row=15, column=1, pady=(0,10))
        # --------------------------------------------------------------



        # ------------------------
        writeFileButton = ttk.Button(self, text="Write Txt File",
                                        command=lambda: appendToTxtFile(acro_input.get(), title_input.get(),
                                                                       port_input.get(), protocol_input.get(),
                                                                       tcp_udp_input.get(), def_input.get()))
        writeFileButton.grid(row=16, column=1)

        # ------------------------
        readFileButton = ttk.Button(self, text="Read Txt File",
                                        command=readTxtFile)
        readFileButton.grid(row=17, column=1)

        # ----------------------------
        # ttk will give us a good looking button
        returHomeButton = ttk.Button(self, text="Return to Home Page",
                             command=lambda: controller.show_frame(StartPage))
        returHomeButton.grid(row=18, column=1)
# ==================================================
# ==================================================
# ==================================================
# ==================================================
class ChangeFilePAge(ttk.Frame):
    '''
    ChangeFilePage
    We have a go_to button at the top that is tied to the entry box below.
        The entry box only accepts int's and only on the size of the object list.
        This will take you to a specific object in the list.
        Note: The displayed position is +1 in contrast to the list position.
            This is just user vs programmer notation.
    We have a Next button that just starts at the first object in the list
        Click next and it will just move 1 by 1 through the list.

    This page will have 6 buttons to edit each object attributes.
        Each edit button has a corresponding internal method.
        1) If you click an edit button, it will pull the attribute
            and put it (in red) in the entry box.
        2) If you click an edit button, it will put the original attribute
            in the corresponding label.
        3) If you click an edit button, the GoTo-button, Next-button, int_Entry dissappear

        4) If you click an edit button, a Save-button, and Entry box appear
                Entry box initially holds in original corresponding attribute
                User can change
        1) If user clicks the Save-Button, it will pull the info from the new Entry
                box, and place it in the adjusted corresponding label. This will be over
                the original posting.
        self.attribute    is an internal variable that is set from the edit button.
            This is auto set to the first 3 chars from the list attribute, so that
                the save method will be able to tell exactly where this change will
                be directed, both in the global_list and the page label.
        2) If user clicks the Save-Button, the global_list will have been adjusted.
                It will now use that list and re-write the entire text file with the
                adjustments that the user just edited. This is not efficient on a massive
                scale but for a study file, it helps to maintain necessary consistency.

    '''

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        mainlabel = ttk.Label(self, text="Change File Page", font=XL_FONT)
        mainlabel.grid(row=0, column=2, padx=(0,0), pady=10, sticky="WE")
        # ----------------------------
        asklabel = ttk.Label(self, text="Option 1) Press 'Next' to see the next study object."
                                        "\nOption 2) Enter Position # and press 'Go To Position' to be specific."
                                        "\n\t0 and 1 will start from beginning."
                                        "\nPress 'Edit' to change the current study object.", font=LARGE_FONT)
        asklabel.grid(row=1, column=2, padx=(0,0), pady=10, sticky="WE")

        # Internal position to cycle through the list
        # Start at -1 so that the first click of "Next" will still be 0
        # It starts at 0, with a blank page waiting for a Next, which will take it to 1
        self.position = -1

        # ----------------------------
        # This will accept a position_int and set the
        #       listPositionLabel_textVar2   to that object's special 6
        # Note: we changed to set individual labels not a full object

        def state_FullFile(position):
            # Will run if the user clicks the Next button
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Can't go past the list lengths
            if self.position < len(global_fileData)-1:
                self.position += 1
            else:
                self.position = 0
                #----------------
            # Line below returns full object for a single label, but we need to set each label individually
            #viewFileLabel_textVar.set("Position: " + str(self.position+1) + "\n" + global_fileData[self.position].__repr__())
            viewFileLabel_textVar.set("Position: " + str(self.position + 1))
            # Set the six labels individually
            acronymLabel_textVar.set(global_fileData[self.position].__str__("acronym"))
            titleLabel_textVar.set(global_fileData[self.position].__str__("title"))
            portLabel_textVar.set(global_fileData[self.position].__str__("port"))
            protocolLabel_textVar.set(global_fileData[self.position].__str__("protocol"))
            tcp_udp_Label_textVar.set(global_fileData[self.position].__str__("tcp_udp"))
            definitionLabel_textVar.set(global_fileData[self.position].__str__("definition"))

            # ==================================================
        # =================
        # --- Go To button method
        def goTo(wanted_position):
            # Called if the goto button is pressed
            if wanted_position == 0:
                wanted_position = wanted_position
            else:
                wanted_position = wanted_position-1
            readTxtFile()
            if wanted_position <= len(global_fileData) -1:
                self.position = wanted_position
                print("positionH")
                print("positionH = " + str(self.position))
        # Line below returns full object for a single label, but we need to set each label individually
                #viewFileLabel_textVar.set("Position: " + str(self.position+1) + "\n" + global_fileData[self.position].__repr__())
                viewFileLabel_textVar.set("Position: " + str(self.position + 1))

                acronymLabel_textVar.set(global_fileData[self.position].__str__("acronym"))
                titleLabel_textVar.set(global_fileData[self.position].__str__("title"))
                portLabel_textVar.set(global_fileData[self.position].__str__("port"))
                protocolLabel_textVar.set(global_fileData[self.position].__str__("protocol"))
                tcp_udp_Label_textVar.set(global_fileData[self.position].__str__("tcp_udp"))
                definitionLabel_textVar.set(global_fileData[self.position].__str__("definition"))

            else:
                goto_input.insert(END, ' DNE')
        # =================
        def clear_Labels():
            # We need to clear the current labels
            acronymLabel_textVar.set("")
            titleLabel_textVar.set("")
            portLabel_textVar.set("")
            protocolLabel_textVar.set("")
            tcp_udp_Label_textVar.set("")
            definitionLabel_textVar.set("")

        # =================
        self.newInput = ""   # Will hold the input to set in label
        self.attribute = ""   # Sent from edit functions so the saveNewInput method can know what to save
        def saveNewInput():
            print("attribute = " + self.attribute)
            if self.attribute == "Acr":
                self.newInput = "Acronym:     " + new_inputBox.get()
                #print("new acro = " + self.newInput)
                acronymLabel_textVar.set(self.newInput)
                #print("GLOBAL 1 = " + str(global_fileData))
                global_fileData[self.position].acronym = self.newInput
                #print("\n\nGLOBAL 2 = " + str(global_fileData))
                changeTxtFile()

            elif self.attribute == "Tit":
                self.newInput = "Title:           " + new_inputBox.get()
                #print("new title = " + newInput)
                titleLabel_textVar.set(self.newInput)
                global_fileData[self.position].title = self.newInput
                #print("\n\nGLOBAL 2 = " + str(global_fileData))
                changeTxtFile()

            elif self.attribute == "Por":
                self.newInput = "Port:           " + new_inputBox.get()
                #print("new port = " + newInput)
                portLabel_textVar.set(self.newInput)
                global_fileData[self.position].port = self.newInput
                #print("\n\nGLOBAL 2 = " + str(global_fileData))
                changeTxtFile()

            elif self.attribute == "Pro":
                self.newInput = "Protocol:      " + new_inputBox.get()
                print("new protocol = " + self.newInput)
                protocolLabel_textVar.set(self.newInput)
                global_fileData[self.position].protocol = self.newInput
                #print("\n\nGLOBAL 2 = " + str(global_fileData))
                changeTxtFile()

            elif self.attribute == "TCP":
                self.newInput = "TCP_UDP:     " + new_inputBox.get()
                print("new tcp_udp = " + self.newInput)
                tcp_udp_Label_textVar.set(self.newInput)
                global_fileData[self.position].tcp_udp = self.newInput
                print("\n\nGLOBAL 2 = " + str(global_fileData))
                changeTxtFile()

            elif self.attribute == "Def":
                self.newInput = "Definition:           " + new_inputBox.get()
                #print("new definition = " + newInput)
                definitionLabel_textVar.set(self.newInput)
                global_fileData[self.position].definition = self.newInput
                # print("\n\nGLOBAL 2 = " + str(global_fileData))
                changeTxtFile()

        # =================
        # --- Edit Acronym button method
        saveButton = ttk.Button(self, text="Save", command=saveNewInput, width=15)
        new_inputBox = ttk.Entry(self, width=70)

        def edit_Acronym():
            # self.position   holds the position we want to change
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Grab the first 3 chars from the line. Use to tell saveNewInput --> Will get 'Acr'
            self.attribute = global_fileData[self.position].__str__("acronym")[0:3]
            clear_Labels()
            # Get rid of the top parts
            gotoButton.destroy()
            goto_input.destroy()
            nextButton.destroy()
            # ----------------
            # Create Entry box for the attribute that was selected
            new_inputBox.configure(foreground="red")
            # ----- attribute includes word 'Acronymm' plus 5 spaces. Remove those
            acronym = global_fileData[self.position].__str__("acronym")
            acronym = acronym[13:]
            # Show the Value in the entry box in red
            new_inputBox.delete(0, END)
            new_inputBox.insert(END, acronym)
            new_inputBox.grid(row=7, column=2, padx=(20, 0), sticky="W")
            # Set the acronym label with the original so user can see what it was
            acronymLabel_textVar.set(global_fileData[self.position].__str__("acronym"))
            # =================
            # --- Display Save button
            # We just showed the button, now the user can click it
            saveButton.grid(row=7, column=1, padx=(20, 0), sticky="W")
        # =================
        def edit_Title():
            # self.position   holds the position we want to change
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Grab the first 3 chars from the line. Use to tell saveNewInput --> Will get 'Tit'
            self.attribute = global_fileData[self.position].__str__("title")[0:3]
            clear_Labels()
            # Get rid of the top parts
            gotoButton.destroy()
            goto_input.destroy()
            nextButton.destroy()
            # ----------------
            # Create Entry box for the attribute that was selected
            new_inputBox.configure(foreground="red")
            # ----- attribute includes word 'Acronymm' plus 5 spaces. Remove those
            title = global_fileData[self.position].__str__("title")
            title = title[17:]
            # Show the Value in the entry box in red
            new_inputBox.delete(0, END)
            new_inputBox.insert(END, title)
            new_inputBox.grid(row=7, column=2, padx=(20, 0), sticky="W")
            # Set the acronym label with the original so user can see what it was
            titleLabel_textVar.set(global_fileData[self.position].__str__("title"))
            # =================
            # --- Display Save button
            # We just showed the button, now the user can click it
            saveButton.grid(row=7, column=1, padx=(20, 0), sticky="W")
        # =================
        def edit_Port():
            # self.position   holds the position we want to change
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Grab the first 3 chars from the line. Use to tell saveNewInput --> Will get 'Por'
            self.attribute = global_fileData[self.position].__str__("port")[0:3]
            clear_Labels()
            # Get rid of the top parts
            gotoButton.destroy()
            goto_input.destroy()
            nextButton.destroy()
            # ----------------
            # Create Entry box for the attribute that was selected
            new_inputBox.configure(foreground="red")
            # ----- attribute includes word 'Acronymm' plus 5 spaces. Remove those
            port = global_fileData[self.position].__str__("port")
            port = port[16:]
            # Show the Value in the entry box in red
            new_inputBox.delete(0, END)
            new_inputBox.insert(END, port)
            new_inputBox.grid(row=7, column=2, padx=(20, 0), sticky="W")
            # Set the acronym label with original
            portLabel_textVar.set(global_fileData[self.position].__str__("port"))
            # =================
            # --- Display Save button
            # We just showed the button, now the user can click it
            saveButton.grid(row=7, column=1, padx=(20, 0), sticky="W")
        # =================
        def edit_Protocol():
            # self.position   holds the position we want to change
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Grab the first 3 chars from the line. Use to tell saveNewInput --> Will get 'Pro'
            self.attribute = global_fileData[self.position].__str__("protocol")[0:3]
            clear_Labels()
            # Get rid of the top parts
            gotoButton.destroy()
            goto_input.destroy()
            nextButton.destroy()
            # ----------------
            # Create Entry box for the attribute that was selected
            new_inputBox.configure(foreground="red")
            # ----- attribute includes word 'Acronymm' plus 5 spaces. Remove those
            protocol = global_fileData[self.position].__str__("protocol")
            protocol = protocol[15:]
            # Show the Value in the entry box in red
            new_inputBox.delete(0, END)
            new_inputBox.insert(END, protocol)
            new_inputBox.grid(row=7, column=2, padx=(20, 0), sticky="W")
            # Set the acronym label with original
            protocolLabel_textVar.set(global_fileData[self.position].__str__("protocol"))
            # =================
            # --- Display Save button
            # We just showed the button, now the user can click it
            saveButton.grid(row=7, column=1, padx=(20, 0), sticky="W")
        # =================
        def edit_TCP_UDP():
            # self.position   holds the position we want to change
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Grab the first 3 chars from the line. Use to tell saveNewInput --> Will get 'TCP'
            self.attribute = global_fileData[self.position].__str__("tcp_udp")[0:3]
            clear_Labels()
            # Get rid of the top parts
            gotoButton.destroy()
            goto_input.destroy()
            nextButton.destroy()
            # ----------------
            # Create Entry box for the attribute that was selected
            new_inputBox.configure(foreground="red")
            # ----- attribute includes word 'Acronymm' plus 5 spaces. Remove those
            tcp_udp = global_fileData[self.position].__str__("tcp_udp")
            tcp_udp = tcp_udp[13:]
            # Show the Value in the entry box in red
            new_inputBox.delete(0, END)
            new_inputBox.insert(END, tcp_udp)
            new_inputBox.grid(row=7, column=2, padx=(20, 0), sticky="W")
            # Set the acronym label with original
            tcp_udp_Label_textVar.set(global_fileData[self.position].__str__("tcp_udp"))
            # =================
            # --- Display Save button
            # We just showed the button, now the user can click it
            saveButton.grid(row=7, column=1, padx=(20, 0), sticky="W")
        # =================
        def edit_Definition():
            # self.position   holds the position we want to change
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Grab the first 3 chars from the line. Use to tell saveNewInput --> Will get 'Def'
            self.attribute = global_fileData[self.position].__str__("definition")[0:3]
            clear_Labels()
            # Get rid of the top parts
            gotoButton.destroy()
            goto_input.destroy()
            nextButton.destroy()
            # ----------------
            # Create Entry box for the attribute that was selected
            new_inputBox.configure(foreground="red")
            # ----- attribute includes word 'Acronymm' plus 5 spaces. Remove those
            definition = global_fileData[self.position].__str__("definition")
            definition = definition[22:]
            # Show the Value in the entry box in red
            new_inputBox.delete(0, END)
            new_inputBox.insert(END, definition)
            new_inputBox.grid(row=7, column=2, padx=(20, 0), sticky="W")
            # Set the acronym label with original
            definitionLabel_textVar.set(global_fileData[self.position].__str__("definition"))
            # =================
            # --- Display Save button
            # We just showed the button, now the user can click it
            saveButton.grid(row=7, column=1, padx=(20, 0), sticky="W")

                # =================
        # =================

        # =================
        # --- Goto button
        # User can enter an int to view a specifc position
        gotoButton = ttk.Button(self, text="Go To Position 1,2,3...:",
                                command=lambda: goTo(int(goto_input.get())))
        gotoButton.grid(row=3, column=2, padx=(0,0), sticky="W")
        # ----------------------------
        # Can't change anything other than foreground....internet has not been helpful
        goto_input = ttk.Entry(self, width=10)
        goto_input.configure(foreground="red")
        goto_input.insert(END, '0')
        goto_input.grid(row=4, column=2, padx=(20,0), sticky="W")
        # =================
        # =================
        # =================
        # --- Next button
        nextButton = ttk.Button(self, text="Next", command=lambda: state_FullFile(self.position))
        nextButton.grid(row=5, column=2, padx=(0,0), pady=(20,0), sticky="W")
        # ----------------------------
        # =================
        # --- Position label
        viewFileLabel_textVar = StringVar()
        viewFileLabel_textVar.set('Position: 0')
        # Note: wraplegth keeps the definition in the current window frame.
        # I don't know if we need this on the other 5 yet
        viewFileLabel = ttk.Label(self, textvariable=viewFileLabel_textVar,
                                    font=LARGE_FONT, wraplength=700)
        viewFileLabel.grid(row=8, column=2, sticky="W", padx=(0,0), pady=(0,30))
        # =================
        # ===================================================
        # ===================================================
        # ===================================================
        # ===================================================
        # ===================================================
        # 6 Edit buttons and labels
        # Edit Acronym
        editAcronymButton = ttk.Button(self, text="Edit Acronym",
                                    command=lambda: edit_Acronym(), width=15)
        editAcronymButton.grid(row=9, column=1, sticky="W", padx=(20,0), pady=(5,0))
        # --- Acronym label
        acronymLabel_textVar = StringVar()
        acronymLabel_textVar.set(':')
        acronymLabel = ttk.Label(self, textvariable=acronymLabel_textVar, font=LARGE_FONT)
        acronymLabel.grid(row=9, column=2, sticky="W", padx=(5, 0), pady=(5,0))
        # ===================================================
        # ===================================================
        # Edit Title
        editTitleButton = ttk.Button(self, text="Edit Title",
                                    command=lambda: edit_Title(), width=15)
        editTitleButton.grid(row=10, column=1, sticky="W", padx=(20,0), pady=(5,0))
        # --- Title label
        titleLabel_textVar = StringVar()
        titleLabel_textVar.set(':')
        titleLabel = ttk.Label(self, textvariable=titleLabel_textVar, font=LARGE_FONT)
        titleLabel.grid(row=10, column=2, sticky="W",  padx=(5, 0), pady=(5,0))
        # ===================================================
        # ===================================================
        # Edit Port
        editPortButton = ttk.Button(self, text="Edit Port",
                                    command=lambda: edit_Port(), width=15)
        editPortButton.grid(row=11, column=1, sticky="W", padx=(20,0), pady=(5,0))
        # --- Port label
        portLabel_textVar = StringVar()
        portLabel_textVar.set(':')
        portLabel = ttk.Label(self, textvariable=portLabel_textVar, font=LARGE_FONT)
        portLabel.grid(row=11, column=2, sticky="W",  padx=(5, 0), pady=(5,0))
        # ===================================================
        # ===================================================
        # Edit Protocol
        editProtocolButton = ttk.Button(self, text="Edit Protocol",
                                    command=lambda: edit_Protocol(), width=15)
        editProtocolButton.grid(row=12, column=1, sticky="W", padx=(20,0), pady=(5,0))
        # --- Edit Protocol label
        protocolLabel_textVar = StringVar()
        protocolLabel_textVar.set(':')
        protocolLabel = ttk.Label(self, textvariable=protocolLabel_textVar, font=LARGE_FONT)
        protocolLabel.grid(row=12, column=2, sticky="W", padx=(5, 0), pady=(5,0))
        # ===================================================
        # ===================================================
        # Edit TCP/UDP
        editTCP_UDPButton = ttk.Button(self, text="Edit TCP/UDP",
                                    command=lambda: edit_TCP_UDP(), width=15)
        editTCP_UDPButton.grid(row=13, column=1, sticky="W", padx=(20,0), pady=(5,0))

        # --- TCP_UDP label
        tcp_udp_Label_textVar = StringVar()
        tcp_udp_Label_textVar.set(':')
        tcp_udp_Label = ttk.Label(self, textvariable=tcp_udp_Label_textVar, font=LARGE_FONT)
        tcp_udp_Label.grid(row=13, column=2, sticky="W", padx=(5, 0), pady=(5,0))
        # ===================================================
        # ===================================================
        # Edit Definition
        editDefinitinoButton = ttk.Button(self, text="Edit Definition",
                                    command=lambda: edit_Definition(), width=15)
        editDefinitinoButton.grid(row=14, column=1, sticky="WN", padx=(20,0), pady=(5,0))
        # --- Definition label
        definitionLabel_textVar = StringVar()
        definitionLabel_textVar.set(':')
        # Note: wraplegth keeps the definition in the current window frame.
        # I don't know if we need this on the other 5 yet
        definitionLabel = ttk.Label(self, textvariable=definitionLabel_textVar,
                                    font=NORM_FONT, wraplength=600)
        definitionLabel.grid(row=14, column=2, sticky="W",  padx=(5, 0), pady=(5,0))
        # ===================================================
        # ===================================================
        # =================
        # =================
        # ----------------------------
        # Button to go back home
        returHomeButtonf = ttk.Button(self, text=" Return Home",
                             command=lambda: controller.show_frame(StartPage))
        returHomeButtonf.grid(row=17, column=2, sticky="WE", padx=(0,0))
# ==================================================
# ==================================================
# ==================================================
# ==================================================
class StudyPage(ttk.Frame):
    '''
    Study Page:
    6 attribute buttons on the top left.
        Corresponding attribute labels next to the buttons on the right.
        If you click an attribute button, the label will display the current
            object attribute. A repeat click of the same button will do nothing.
        You can click the other attribute buttons to add their corresponding labels.
        This is so that a user can study and work to memorize a specicif object and its
            attributes..
    All Traits - Button --> Lists all traits of the current object.
        This is just so that a user doesnt have to click 6 buttons
    Clear/Redo - Button --> Remains on the current list object.
        Clears the labels, so the user can redo and work on memorization.
    Next - Button --> Clears the entire label list and makes it blank.
        Next-Button is tied to its personal method.
        Also moves to the next object in the list. If the user feels good and has memorized
            object 2, they click next and can try to memorize the 3rd object in the list.
    Random - Button --> Clears the entire label list and makes it blank.
        Random-Button is tied to its personal method
        Follows the Next-Button idea, but uses a built in randum function to choose a
            a random int position within the length of the list.

    '''
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        mainlabel = ttk.Label(self, text="StudyPage", font=XL_FONT)
        mainlabel.grid(row=0, column=1, padx=(10,0), pady=10, sticky="W")
        # -----
        mainlabel2 = ttk.Label(self, text="Use the Page Buttons or Keyboard Shortcuts", font=LARGE_FONT)
        mainlabel2.grid(row=0, column=2, padx=10, pady=10, sticky="W")
        #-----------------
        #Key bind Labels
        keybind_label1A = ttk.Label(self, text="Keyboard: Right Arrow -", font=NORM_FONT)
        keybind_label1A.grid(row=1, column=1, padx=10, sticky="W")
        keybind_label1B = ttk.Label(self, text="Move to Next Position", font=NORM_FONT)
        keybind_label1B.grid(row=1, column=2, padx=10, sticky="W")
        # -----
        keybind_label2A = ttk.Label(self, text="Keyboard: Space Bar -", font=NORM_FONT)
        keybind_label2A.grid(row=2, column=1, padx=10, pady=(0,20),  sticky="W")
        keybind_label2B = ttk.Label(self, text="Show All Traits", font=NORM_FONT)
        keybind_label2B.grid(row=2, column=2, padx=10, pady=(0,20), sticky="W")
        # ==================================================
        # Built funciton to clear the labels.
        # Used in:   next_StudyObject():   &&   random_StudyObject():
        def clear_Labels():
            # We need to clear the current labels
            acronymLabel_textVar.set(":")
            titleLabel_textVar.set(":")
            portLabel_textVar.set(":")
            protocolLabel_textVar.set(":")
            tcp_udp_Label_textVar.set(":")
            definitionLabel_textVar.set(":")

        # ==================================================
        self.studyNumber = 0
        # Remember, we are displaying the values +1 to the user of how python reads the list
        # In the list the first spot is 0, but users like 1 better
        def state_currentPosition():
            print(self.studyNumber)
            return ("Position:" + str(self.studyNumber + 1))

        # =============
        # Change the value for the user in seeking in the StudyObject list
        # This is for the single increment for the next object
        # Can't be more than the len - 1
        def next_StudyObject():

            # We need to clear the current labels
            clear_Labels()
            print(self.studyNumber) # Print the current number. Just show
            if self.studyNumber < len(global_fileData)-1:
                self.studyNumber += 1
                print(self.studyNumber)
                listPositionLabel_textVar.set(state_currentPosition())

            else:
                print("\n There are no more objects")
                self.studyNumber = 0
                listPositionLabel_textVar.set(state_currentPosition())

        # ==================================================
        # Allow the user to get a random study object from the list.
        def random_StudyObject():

            # We need to clear the current labels
            clear_Labels()
            print(self.studyNumber)
            # Don't go past the last one.
            self.studyNumber = random.randint(0, len(global_fileData)-1)
            print(self.studyNumber)
            listPositionLabel_textVar.set(state_currentPosition())

        # ==================================================
        # Clear the traits, but it will stay on the current object. If the user wants to repeat
        def clear_Page():
            pass

        # ==================================================
        # Automatically get the object list of our study txt file.
        # printrtn(): method is just for programmer show, not the user.

        def printrtn(): # ==================================================
            readTxtFile()
            print("\nGlobal File Data = ")
            print(global_fileData)
            # ---------
            # Currently we are just asking to get the last on in the list.
            # The __repr__ prints the full value of the studyObject.
            # We created the __repr__ in the class inputObject
            print("\nGlobal File Data[Lastone] repr data=",
                  global_fileData[self.studyNumber].__repr__()) # works
            # ---------
            # __str__ currently prints:      Acronym:      FTP
            #   We created the __str__ in the class inputObject
            #   __str__()   depends on the sent piece: (acronym, title, port, protocol, tcp_udp, definition)
            #   We have it printing from the last one in the list currently
            print("\nGlobal File Data[Lastone] str data =",
                  global_fileData[self.studyNumber].__str__("acronym")) # works
            # ---------

        # ==================================================
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # User clicks a button with what they want from of the 6 object values
        # The button calls this method while sending the stated value that they want.
        # readTxtFile(): Make sure that the global_list is refreshed when the 6 buttons are clicked
        def state_Acronym():
            readTxtFile()
            print(global_fileData[self.studyNumber].__str__("acronym"))
            acronymLabel_textVar.set(global_fileData[self.studyNumber].__str__("acronym"))
        # ----------------------------
        def state_Title():
            readTxtFile()
            print(global_fileData[self.studyNumber].__str__("title"))
            titleLabel_textVar.set(global_fileData[self.studyNumber].__str__("title"))
        # ----------------------------
        def state_Port():
            readTxtFile()
            print(global_fileData[self.studyNumber].__str__("port"))
            portLabel_textVar.set(global_fileData[self.studyNumber].__str__("port"))
        # ----------------------------
        def state_Protocol():
            readTxtFile()
            print(global_fileData[self.studyNumber].__str__("protocol"))
            protocolLabel_textVar.set(global_fileData[self.studyNumber].__str__("protocol"))
        # ----------------------------
        def state_Tcp_Udp():
            readTxtFile()
            print(global_fileData[self.studyNumber].__str__("tcp_udp"))
            tcp_udp_Label_textVar.set(global_fileData[self.studyNumber].__str__("tcp_udp"))
        # ----------------------------
        def state_Definition():
            readTxtFile()
            print(global_fileData[self.studyNumber].__str__("definition"))
            definitionLabel_textVar.set(global_fileData[self.studyNumber].__str__("definition"))
        # ----------------------------
        def state_All6():
            state_Acronym()
            state_Title()
            state_Port()
            state_Protocol()
            state_Tcp_Udp()
            state_Definition()
            # ==================================================
        # ----------------------------
        # The methods(above), 6 study page methods
        #       and the labels (below) for the 6 labels on StudyPage
        #       and the 6 buttons
        # ----------------------------
        # ----------------------------
        # --- Acronym button
        stateAcronymButton = ttk.Button(self, text="Acronym", command=state_Acronym, width=10)
        stateAcronymButton.grid(row=3, column=1, sticky="W", padx=(20,0), pady=(0,20))
        # --- Acronym label
        acronymLabel_textVar = StringVar()
        acronymLabel_textVar.set(':')
        acronymLabel = ttk.Label(self, textvariable=acronymLabel_textVar, font=LARGE_FONT)
        acronymLabel.grid(row=3, column=2, sticky="W", pady=(0,20))
        # ----------------------------
        # ----------------------------
        # --- Title button
        stateTitleButton = ttk.Button(self, text="Title", command=state_Title, width=10)
        stateTitleButton.grid(row=4, column=1, sticky="W", padx=(20,0), pady=(0,20))
        # --- Title label
        titleLabel_textVar = StringVar()
        titleLabel_textVar.set(':')
        titleLabel = ttk.Label(self, textvariable=titleLabel_textVar, font=LARGE_FONT)
        titleLabel.grid(row=4, column=2, sticky="W", pady=(0,20))
        # ----------------------------
        # ----------------------------
        # --- Port button
        statePortButton = ttk.Button(self, text="Port", command=state_Port, width=10)
        statePortButton.grid(row=5, column=1, sticky="W", padx=(20,0), pady=(0,20))
        # --- Port label
        portLabel_textVar = StringVar()
        portLabel_textVar.set(':')
        portLabel = ttk.Label(self, textvariable=portLabel_textVar, font=LARGE_FONT)
        portLabel.grid(row=5, column=2, sticky="W", pady=(0,20))
        # ----------------------------
        # ----------------------------
        # --- Protocol button
        stateProtocolButton = ttk.Button(self, text="Protocol", command=state_Protocol, width=10)
        stateProtocolButton.grid(row=6, column=1, sticky="W", padx=(20,0), pady=(0,20))
        # --- Protocol label
        protocolLabel_textVar = StringVar()
        protocolLabel_textVar.set(':')
        protocolLabel = ttk.Label(self, textvariable=protocolLabel_textVar, font=LARGE_FONT)
        protocolLabel.grid(row=6, column=2, sticky="W", pady=(0,20))
        # ----------------------------
        # ----------------------------
        # --- TCP_UDP button
        state_tcp_udp_Button = ttk.Button(self, text="TCP/UDP", command=state_Tcp_Udp, width=10)
        state_tcp_udp_Button.grid(row=7, column=1, sticky="W", padx=(20,0), pady=(0,20))
        # --- TCP_UDP label
        tcp_udp_Label_textVar = StringVar()
        tcp_udp_Label_textVar.set(':')
        tcp_udp_Label = ttk.Label(self, textvariable=tcp_udp_Label_textVar, font=LARGE_FONT)
        tcp_udp_Label.grid(row=7, column=2, sticky="W", pady=(0,20))
        # ----------------------------
        # ----------------------------
        # --- Definition button
        stateDefinitionButton = ttk.Button(self, text="Definition", command=state_Definition, width=10)
        stateDefinitionButton.grid(row=8, column=1, sticky="WN", padx=(20,0), pady=(0,20))
        # --- Definition label
        definitionLabel_textVar = StringVar()
        definitionLabel_textVar.set(':')
        # Note: wraplegth keeps the definition in the current window frame.
        # I don't know if we need this on the other 5 yet
        definitionLabel = ttk.Label(self, textvariable=definitionLabel_textVar,
                                    font=NORM_FONT, wraplength=550)
        definitionLabel.grid(row=8, column=2, sticky="W", pady=(0,20))
        # ----------------------------
        # ----------------------------
        # --- StateAll button
        stateAllButton = ttk.Button(self, text="All Traits", command=state_All6, width=10)
        stateAllButton.grid(row=15, column=1, sticky="W", padx=(20,0))
        # ----------------------------
        # --- Clear All / Redo button
        clearAllredoButton = ttk.Button(self, text="Clear/Redo", command=clear_Labels)
        clearAllredoButton.grid(row=15, column=2, sticky="WE", padx=(0,0))
        # ----------------------------
        # ----------------------------
        # ==================================================
        # --- Position label
        listPositionLabel_textVar = StringVar()
        listPositionLabel_textVar.set(str(state_currentPosition()))
        listPositionLabel = ttk.Label(self, textvariable=listPositionLabel_textVar, font=LARGE_FONT)
        listPositionLabel.grid(row=17, column=2, sticky="W", pady=(0,10))
        # ----------------------------
        # Button to increase the studyNumber + 1 to call for the next object
        increaseByOneButton = ttk.Button(self, text="Next", command=next_StudyObject, width=10)
        increaseByOneButton.grid(row=18, column=1, sticky="W", padx=(20,0))
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # Keyboard binds
        # Details are in the pseudo-keylogger page for the programmer
        # Remember we have to bind this to a created StudyPage button
        # ------------------
        def right_Key(event):
            # If we are on this StudyPage, the right keyboard button will move to the next object
            if len(event.char) == 1:
            # charcters like []/.,><#$ also Return and ctrl/key
                readTxtFile()
                print('Punctuation666 Key %r (%r)' % (event.keysym, event.char))
                next_StudyObject()
        # -----
        increaseByOneButton.bind_all('<Right>', right_Key)
        # ----------------------------
        def space_Bar(event):
            if len(event.char) == 1:
            # charcters like []/.,><#$ also Return and ctrl/key
                readTxtFile()
                print('Punctuation666 Key %r (%r)' % (event.keysym, event.char))
                state_All6()
        stateAllButton.bind_all('<space>', space_Bar)
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------

        # Button to get a random studyNumber for the next object
        randomNumberButton = ttk.Button(self, text="Random", command=random_StudyObject)
        randomNumberButton.grid(row=18, column=2, sticky="WE", padx=(0,0))
        # ----------------------------
        # Button to go back home
        returHomeButtonf = ttk.Button(self, text="Return Home",
                             command=lambda: controller.show_frame(StartPage), width=10)
        returHomeButtonf.grid(row=20, column=1, sticky="W", padx=(20,0))
# ==================================================
# ==================================================
# ==================================================
# ==================================================
class KeyLoggerPage(ttk.Frame):
    # This is just for show.
    # If you go to this page it simply prints your keys that you press.
    # This does nothing, but I want to use it on the other pages
    #       and am just testing it out.
    # The right arrow and space bar are permanently tied to the Study Page bind functions,
    #       not sure why at the momemnt.
    '''
        If I press the Right arrow it will print:
            Punctuation Key 'Right' ('\uf703')
    '''

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        mainlabel = ttk.Label(self, text="Key Logger Page", font=XL_FONT)
        mainlabel.grid(row=0, column=2, padx=(50,0), pady=10, sticky="WE")

        mainlabel2 = ttk.Label(self, text="Press ESC to Return Home", font=LARGE_FONT)
        mainlabel2.grid(row=1, column=2, padx=(50,0), pady=10, sticky="WE")

        currentErrorlabel = ttk.Label(self, text="The Right Arrow and Space bar, seem to be "
                                                 "\n permanently tied to the Study Page Functions."
                                                 "\n Not sure why.", font=NORM_FONT)
        currentErrorlabel.grid(row=2, column=2, padx=(50,0), pady=10, sticky="WE")
        # ----------------------------


        # --- Key log adjustable label
        keyLogLabel_textVar = StringVar()
        keyLogLabel_textVar.set(':')
        keyLogLabel = ttk.Label(self, textvariable=keyLogLabel_textVar, font=LARGE_FONT)
        keyLogLabel.grid(row=6, column=2, sticky="W", pady=(40,20), padx=(50,0))


        def key(event):
            """shows key or tk code for the key"""
            if event.keysym == 'Escape':
                controller.show_frame(StartPage)
                print("Made it to escape")

            if event.char == event.keysym:
                # normal number and letter characters
                print('Normal Key %r' % event.char)
                keyLogLabel_textVar.set('Normal Key %r' % event.char)

            elif len(event.char) == 1:
                # charcters like []/.,><#$ also Return and ctrl/key
                print('Punctuation Key %r (%r)' % (event.keysym, event.char))
                keyLogLabel_textVar.set('Punctuation Key %r (%r)' % (event.keysym, event.char))
            else:
                # f1 to f12, shift keys, caps lock, Home, End, Delete ...
                print('Special Key %r' % event.keysym)
                keyLogLabel_textVar.set('Special Key %r' % event.keysym)

        keyLogLabel.bind_all('<Key>', key)
        # ----------------------------

        # ttk will give us a good looking button
        returHomeButtonf = ttk.Button(self, text="Return to Home Page",
                             command=lambda: controller.show_frame(StartPage))
        returHomeButtonf.grid(row=10, column=2, sticky="W", pady=(40,20), padx=(50,0))
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# END PAGES PAGES PAGES PAGES PAGES PAGES PAGES
# END PAGES PAGES PAGES PAGES PAGES PAGES PAGES
# END PAGES PAGES PAGES PAGES PAGES PAGES PAGES
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
#   MAIN    MAIN    MAIN    MAIN    MAIN    MAIN
# ==================================================
app = SecurityPlus()

app.mainloop()
# ==================================================
#   MAIN    MAIN    MAIN    MAIN    MAIN    MAIN
# ==================================================