# Current Py file Directory address
# /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/Security+_StudyApp.py
# =================
# Current txt file Directory address
# /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/SecurityPlus_StudyFile.txt
# =================
# Current photo folder Directory address
# /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/_Photos/
# =================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# Imports Imports Imports Imports Imports Imports
# Program made with python 3.5.2
#       Pycharm Community Edition
# Runs with idle:
#       Run Module

from tkinter import *
import random # For the random number on from the study list (StudyPage)
import urllib
import json
# Terminal/CMD (we are on mac)
#   pip3 install pandas
#   pip3 install numpy
# Need for the graph if we use it
#import pandas as pd
#import numpy as np

# ==================================================
import tkinter as tk
from tkinter import ttk
'''
Terminal/CMD     pip3 install matplotlib
'''
import matplotlib
# This (below) lets us "change the back ground"
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
#---------
# Using PIL for the pop up window on the StudyPage
from PIL import Image, ImageTk
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
# Set photo directory address in StudyPage, so the PhotoPage knows what to open
# We set it to a stock photo initially, so the PhotoPage can open up front.
global globalPhoto_Directory
globalPhoto_Directory = "/Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/_Photos/"
# Called and set from SearchPage/SearchMethod
# In Method, User sets what postion they want to display in study page.
global global_SearchReturnPosition
global_SearchReturnPosition = 0
# Input from SearchPage. What the user wants to search for.
global global_UserSearchString
global_UserSearchString = ""
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
        tk.Tk.geometry(self, "1200x1000")
        # Can't get the icon to show, now just a png icon
        # Resized to 12/16 pixels
        tk.Tk.iconbitmap(self, "icon.png")
        # =================
        # =================
        # =================
        # =================
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
                              command=lambda: addPhoto_popupmsg("part1", "part2"))
        # addPhoto_popupmsg("Msg sent from class SecurityPlus"))
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
                  StudyPage,
                  SearchPage):
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
# ==================================================
# ==================================================
def areYouSure_popupmsg(position, title):
    # Method is called from the ChangePage if the user tries to delete an object.
    # Create popup window, and set it's geometry
    popup = tk.Tk()
    popup.geometry("1000x500")
    # -------------------------
    # -------------------------
    # variable set with incoming parameter title
    title = title[17:]
    confirm_this = title

    # -------------------------
    label1 = ttk.Label(popup, text="Are you sure you want to delete: " + confirm_this, font=LARGE_FONT)
    label1.pack(pady=(0,20))

    # -------------------------
    # yes button calls delete object global method
    def yes_ButtonMethod():
        deleteObject(position)
        popup.destroy()

    # ----------
    yes_Button = ttk.Button(popup, text="Yes", command=lambda: yes_ButtonMethod())
    yes_Button.pack()

    # ------------------------
    noButton = ttk.Button(popup, text="No", command=popup.destroy)
    noButton.pack()
# ==================================================
# ==================================================
# ==================================================
# ==================================================
def addPhoto_popupmsg(msg, title):
    # Create popup window, and set it's geometry
    # To get the popup window:
    # Add a new file. Will auto ask for user's photo after they click to write file.
    # This takes the title of the object the user just created and names that to the photo as a png.
    popup = tk.Tk()
    popup.geometry("1000x1000")
    # -------------------------
    # -------------------------
    label2 = ttk.Label(popup, text="Drag the photo into this current folder - "
                                   "\n\tPress OK when the photo is in this folder.", font=LARGE_FONT)
    # -------------------------
    ok_Button = ttk.Button(popup, text="OK", command=lambda: okButtonMethod())
    # -------------------------
    label3 = ttk.Label(popup, text="Enter the final name of the photo you just dragged? "
                                   "\n\nExample:"
                                   "\n/Users/Tracksta6/Dropbox/photoName123.png"
                                   "\nFinal name to enter:"
                                   "\n\nphotoName123.png", font=LARGE_FONT)
    # -------------------------
    photoName_Entry = ttk.Entry(popup)
    # -------------------------
    # --- Display Save button
    # We just showed the button, now the user can click it
    saveButton = ttk.Button(popup, text="Save", command=lambda: saveButtonMethod())
    # -------------------------

    def yesButtonMethod():
        # Yes = user has a photo to enter.
        yesButton.destroy()
        noButton.destroy()
        label2.pack(side="top", fill="x", pady=10, padx=(20, 0))
        ok_Button.pack()

    def okButtonMethod():
        # OK = user has dragged photo into the stated photo folder
        label2.destroy()
        ok_Button.destroy()
        label3.pack(side="top", fill="x", pady=10, padx=(20, 0))
        # ----------------
        # Show the Value in the entry box in red
        photoName_Entry.configure(foreground="red")
        photoName_Entry.pack(side="top", fill="x", pady=10, padx=(20, 0))
        saveButton.pack(side="top", fill="x", pady=10, padx=(20, 0))
        # ----------------

    def saveButtonMethod():
        # User entered the photo name...ex. photo123.png
        # Opens the current photo as is, and saves again as it relates to the object.
        global globalPhoto_Directory
        image1 = Image.open(globalPhoto_Directory + photoName_Entry.get())
        image1.save(globalPhoto_Directory + title + ".png")
        popup.destroy()


    # Set the popup window title
    popup.wm_title("Do you have a photo to save with this?")
    # Set a label in the popup window
    label1 = ttk.Label(popup, text=msg + "\n" + title, font=XL_FONT)
    label1.pack(side="top", fill="x", pady=10, padx=(20,0))

    # Set a button in the popup window with a command to destroy popup window
    yesButton = ttk.Button(popup, text="Yes", command=lambda: yesButtonMethod())
    yesButton.pack()
    noButton = ttk.Button(popup, text="No", command=popup.destroy)
    noButton.pack()
    #popup.mainloop()
# ==================================================
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

    #dataList1 = [line.rstrip('\n') for line in open('SecurityPlus_StudyFile.txt')]
    dataList1 = [line.rstrip('\n') for line in open("/Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/SecurityPlus_StudyFile.txt")]
    # =======================
    print("\nThat was the datalist as a variable, now the for loop: ")
    # Simple print out from the file.
    for x in dataList1: pass
        #print(x)
        #if x == "###":
        #    print("----------------")
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
        # y=0 is always the first acronym
        if y == 0:
            print("we are at zero")
            acronym = dataList1[y]
            title = dataList1[y + 1]
            port = dataList1[y + 2]
            protocol = dataList1[y + 3]
            tcp_udp = dataList1[y + 4]
            definition = dataList1[y + 5]
            # Remember the very first object does not start with ###
            # We may have lists on the definition, need to account for more than 6 lines
            XII = 6
            if y != (len(dataList1)-7) and dataList1[y+XII] != "###":
                while dataList1[y+XII] != "###":
                    if dataList1[y+XII] == "\n":
                        XII += 1
                    else:
                        definition += "\n" + dataList1[y+XII]
                        XII += 1

            studyObject = inputObject(acronym, title, port, protocol, tcp_udp, definition)
            global_fileData.append(studyObject)

        # after y=0 if line == ###  then we know the next 6 lines will be our attributes
        if dataList1[y] == "###":
            acronym = dataList1[y+1]
            title = dataList1[y+2]
            port = dataList1[y+3]
            protocol = dataList1[y+4]
            tcp_udp = dataList1[y+5]
            definition = dataList1[y+6]
            # We may have lists on the definition, need to account for more than 6 lines
            XII = 7
            if y != (len(dataList1)-7) and dataList1[y+XII] != "###":
                while dataList1[y+XII] != "###":
                    if dataList1[y+XII] == "\n":
                        XII += 1
                    else:
                        definition += "\n" + dataList1[y+XII]
                        XII += 1

            # Create an object and add it to the txt file.
            studyObject = inputObject(acronym, title, port, protocol, tcp_udp, definition)
            global_fileData.append(studyObject)
# ==================================================
# ==================================================
# ==================================================
# ==================================================
def appendToTxtFile(acronym, title, port, protocol, TCP_UDP, definition): #animate function with  'i' for interval
    '''
    This method appends to  our text file
    This is called on the   AddToFilePage
        Called for user to add a full object to the file.
    '''
    #writeData1 = open("SecurityPlus_StudyFile.txt", "a")
    writeData1 = open("/Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/SecurityPlus_StudyFile.txt", "a")

    # Print's are just for programmer show
    print("acronym    = " + acronym)
    print("title      = " + title)
    print("port       = " + port)
    print("protocol   = " + protocol)
    print("TCP_UDP    = " + TCP_UDP)
    print("definition = " + definition)

    # If the user does not input anything, we will write N/A
    if acronym == "":
        acronym = "-"
    # Remove /n from a single string. Keep as one piece. Only need for Definition, but be safe
    acronym = acronym.replace("\n", "")
    # -------------------
    if title == "":
        title = "-"
    # Remove /n from a single string. Keep as one piece. Only need for Definition, but be safe
    title = title.replace("\n", "")
    # -------------------
    if port == "":
        port = "-"
    # Remove /n from a single string. Keep as one piece. Only need for Definition, but be safe
    port = port.replace("\n", "")
    # -------------------
    if protocol == "":
        protocol = "-"
    # Remove /n from a single string. Keep as one piece. Only need for Definition, but be safe
    protocol = protocol.replace("\n", "")
    # -------------------
    if TCP_UDP == "":
        TCP_UDP = "-"
    # Remove /n from a single string. Keep as one piece. Only need for Definition, but be safe
    TCP_UDP = TCP_UDP.replace("\n", "")
    # -------------------
    if definition == "":
        definition = "-"
    # Double stars are turned into a new line
    #       Account for spaces
    # ----------------------------
    # The    **   helped get a new line when we were using the Definition Entry box.
    #       We switched to Definition Textbox and dont need this now.... Safe-Keeping
    '''
    definition = definition.replace(" ** ", "\n---")
    definition = definition.replace("** ", "\n---")
    definition = definition.replace(" **", "\n---")
    definition = definition.replace("**", "\n---")
    '''

    # Append the user input to the file as expected
    writeData1.write("Acronym:     " + acronym + '\n')
    writeData1.write("Title:           " + title + '\n')
    writeData1.write("Port:           " + port + "\n")
    writeData1.write("Protocol:      " + protocol + "\n")
    writeData1.write("TCP/UDP:     " + TCP_UDP + "\n")
    writeData1.write("Definition:           " + definition + '\n')
    writeData1.write('###\n')
    writeData1.close()


    studyObject2 = inputObject(acronym, title, port, protocol, TCP_UDP, definition)
    # Will call the global file later, but we have to run the read file to get it up to date
    global_fileData.append(studyObject2)
# ==================================================
# ==================================================
# ==================================================
# ==================================================
def changeTxtFile():
    '''
    # We have to re-write the file even for a one attribute change
#    Read in the file and place in list
#       Change a spot in that list.
#           Write list to file spot-->line

    Simple method to print the global-list to the file.
        This is called from the changeFilePage
        This rewrites the full file each time.
            Full rewrite is not efficient, but helps to remain consistant on a small scale like this.

    '''
    #writeData1 = open("SecurityPlus_StudyFile.txt", "w")
    writeData1 = open("/Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/SecurityPlus_StudyFile.txt", "w")
    for x in global_fileData:
        # Double stars are turned into a new line
        #       Account for spaces
        # ----------------------------
        # The    **   helped get a new line when we were using the Definition Entry box.
        #       We switched to Definition Textbox and dont need this now.... Safe-Keeping
        '''
        x.definition = x.definition.replace(" ** ", "\n---")
        x.definition = x.definition.replace("** ", "\n---")
        x.definition = x.definition.replace(" **", "\n---")
        x.definition = x.definition.replace("**", "\n---")
        '''
        # Append the user input to the file as expected
        writeData1.write(x.acronym + '\n')
        writeData1.write(x.title + '\n')
        writeData1.write(x.port + "\n")
        writeData1.write(x.protocol + "\n")
        writeData1.write(x.tcp_udp + "\n")
        writeData1.write(x.definition + '\n')
        writeData1.write('###\n')

    writeData1.close()
# ==================================================
# ==================================================
# ==================================================
# ==================================================
def deleteObject(deletePosition):
    '''
    Call this method.
        Send a int with the method call.
        That int will be the position that wants to be deleted.
    '''
    #readTxtFile()
    # Next 2 lines for programmer view
    print("\nSent Postition = " + str(deletePosition))
    print(global_fileData[deletePosition].__repr__())

    # After the delete spot, fill the others in
    # Delete the final spot since that was moved down 1
    #       Otherwise we will have a copy of the last one
    for n in range(deletePosition, len(global_fileData)):
        if n == len(global_fileData)-1:
            print("\n===================")
            print("\n111 -- " + str(global_fileData))
            del global_fileData[n]
            print("\n222 -- " + str(global_fileData))

            break
        # Start at delete position. Move subsequent posititon in
        global_fileData[n] = global_fileData[n+1]
    # Just deleted from list. Now write list to file.
    changeTxtFile()
# ==================================================
# ==================================================
# ==================================================
# ==================================================
def set_Global_PhotoDirectory(position, title):
    # Method called from the    pictureButton. User clicks to see related photo
    # Need an internal method that calls this
    # The primary directory for all photos. We need to add the actually photo name on the end.
    initial_Directory = "/Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/_Photos/"
    # Sending title parameter.
    # Must condense:    Title:           Firewalls
    #            To:    Firewalls
    title = title[17:]

    # PLANNING: when importing photo, set the title as the photo title as well.
    # Object title = Unified Thread Management
    # Photo will be save as:    example.......users/folder/Unified Threat Management.png
    # Note: The photo directory will have a   .png   so we need to include it.
    #       There are other photo types. Be careful when calling photo
    final_directory = initial_Directory + str(title) + ".png"
    # Example of a photo.
    #final_directory = "/Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/tallPhoto.png"

    # can probably just use "final_directory" since we are on the same page.
    image1 = Image.open(final_directory)
    # Current Examples:
    # image1 = Image.open("/Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/photo1.png")
    # image1 = Image.open("/Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/Party.jpg")

    # This is to resize the photo to keep within the current page.
    newWidth = image1.width
    newHeight = image1.height
    if image1.width > 1100:
        widthDifference = image1.width - 1100
        widthRatio = widthDifference / image1.width
        convertRatio = 1 - widthRatio
        newWidth = int(image1.width * convertRatio)
        newHeight = int(image1.height * convertRatio)

    # Note we need to play with size and match it to the page better probably 700 for height
    elif image1.height > 700:
        heightDifference = image1.height - 700
        heightRatio = heightDifference / image1.height
        convertRatio = 1 - heightRatio
        newWidth = int(image1.width * convertRatio)
        newHeight = int(image1.height * convertRatio)

    resized = image1.resize((newWidth, newHeight), Image.ANTIALIAS)
    # This method, imported photo, and resized to match the page.
    # Now send that back to the StudyPage
    return resized
# ==================================================
# ==================================================
# ==================================================
# ==================================================
def searchFor(StudyPage_UserSearchFor):
    # NOTE: This works for the most part. Not using it, turned Search into a page
    # Create popup window, and set it's geometry
    # To get the popup window:
    # Add a new file. Will auto ask for user's photo after they click to write file.
    # This takes the title of the object the user just created and names that to the photo as a png.
    popup = tk.Tk()
    popup.geometry("1000x1000")
    # Set the popup window title
    popup.wm_title("Search For: ")
    # Set a label in the popup window

    # -------------------------
    # -------------------------
    # ----
    # Top example label
    label1 = ttk.Label(popup, text="What do you want to search for?"
                                   "\nExamples:"
                                   "\n\t1) IDS"
                                   "\n\t2) Intrusion Detection System", font=LARGE_FONT)
    label1.pack(side="top", fill="x", pady=10, padx=(20,0))

    # -------------------------
    # ----
    # 2nd label, grabs user search input from the StudyPage
    label2 = ttk.Label(popup, text="\tSearching For: " + StudyPage_UserSearchFor, font=LARGE_FONT)
    label2.pack(side="top", fill="x", pady=10, padx=(20,0))

    # -------------------------
    # This for loop auto runs upon popup window opening.
    # Loop currently finds everything that exactly matches search parameter. Capitalization applies
    # Loop pushes everything in global list that matches from both acronym and title.
    popup.searchList = []
    for n in range(0, len(global_fileData)):
        if StudyPage_UserSearchFor == global_fileData[n].__str__("acronym")[13:]:
            popup.searchList.append(n)
            popup.searchList.append(global_fileData[n].__str__("acronym"))
        if StudyPage_UserSearchFor == global_fileData[n].__str__("title")[17:]:
            popup.searchList.append(n)
            popup.searchList.append(global_fileData[n].__str__("title"))
    print("searchList outside of for = :", popup.searchList)
    # -------------------------
    # -------------------------
    # Label that will be appended to and printed on screen with formated search results.
    popup.labelSearch = ""
    for n in range(0, len(popup.searchList)):
        # Even numbers will always be the position number. Odd numbers will be: ex. Acronym    DNS
        # We want to display the list position + 1 so user can relate easily.
        if n %2 ==0:
            popup.labelSearch += "Position: " + str(popup.searchList[n] + 1)
        else:
            popup.labelSearch += "\t" + str(popup.searchList[n])
        # Formatting, drop a line for the popup window print job.
        popup.labelSearch += "\n"

    # Formatted the String label from the search data. Now assign to a label.
    label3Live = ttk.Label(popup, text=popup.labelSearch, font=NORM_FONT)
    label3Live.pack(side="top", fill="x", pady=10, padx=(20,0))

    # -------------------------
    # Label to ask user what position they want to return to Study page with
    enterPositionLabel = ttk.Label(popup, text="Enter Wanted Position: ")
    enterPositionLabel.pack(side="top", fill="x", pady=10, padx=(20,0))

    # -------------------------
    # Entry box for user to enter which position that they want to go back with
    returnPosition = ttk.Entry(popup, width=15)
    returnPosition.pack(side="top", fill="x", pady=10, padx=(20,0))

    # Value and sub function to bring back
    def backWithPosition_ButtonMethod():
        global global_SearchReturnPosition

        print("search method - global_SearchReturnPosition = " + str(global_SearchReturnPosition))

        global_SearchReturnPosition = int(returnPosition.get())
        print("search method - global_SearchReturnPosition = " + str(global_SearchReturnPosition))

    setPositionButton = ttk.Button(popup, text="Set Your Wanted Postition", command=lambda: backWithPosition_ButtonMethod)
    setPositionButton.pack(side="top", fill="x", pady=10, padx=(20,0))
    # -------------------------
    cancelButton = ttk.Button(popup, text="Return to StudyPage", command=lambda: popup.destroy())
    cancelButton.pack(side="top", fill="x", pady=10, padx=(20,0))
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
                    Note: Down and right arrow are used in StudyPage
                    They seem to be permanently tied. Can't be used here?
            5) Quit Program


    '''
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font=XL_FONT)
        label.pack(padx=10, pady=10)

        # ----------------------------
        # ttk will give us a good looking button
        def studyPage_Command():
            # To call a readFile before you go anytime.
            readTxtFile()
            controller.show_frame(StudyPage)
        startPage_GOToStudyPageButton = ttk.Button(self, text="Study Page",
                                                   command=lambda: studyPage_Command(), width=15)
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

        label = ttk.Label(self, text="-------------------- Add to Study File ------------------------------",
                          font=XL_FONT)
        # 1st row, 2nd column, pushto right 40%
        label.grid(row=0, column=1, padx=10)
        # ------------------------
        warninglabel = ttk.Label(self,
                                 text="Some characters may not be accepted. "
                                "EX. Microsoft Word will AutoFill dashes, arrows, etc. They are not accepted here."
                                "\nSome quotation marks can be copied and pasted that don't work"
                                "\nThe definition can be long, but keep it simple. "
                                    "User input will remain unless you click Write to Txt File, or exit the entire program.", font=NORM_FONT)
        warninglabel.grid(row=1, column=1, pady=(0,10))
        # ------------------------
        # ------------------------
        # ------------------------
        # --------------------------------------------------------------
        acro_Label = ttk.Label(self, text="Add Acronym: ", font=LARGE_FONT)
        acro_Label.grid(row=4, column=0, sticky="W", padx=20)
        # -----
        acro_input = ttk.Entry(self)
        acro_input.grid(row=4, column=1, sticky="WE")
        # -----
        acro_Example = ttk.Label(self, text="Ex: DNS ", font=NORM_FONT)
        acro_Example.grid(row=5, column=1, sticky="WE", padx=20, pady=(0,5))
        # --------------------------------------------------------------
        title_Label = ttk.Label(self, text="Add Title: ", font=LARGE_FONT)
        title_Label.grid(row=6, column=0, sticky="W", padx=20)
        # -----
        title_input = ttk.Entry(self)
        title_input.grid(row=6, column=1, sticky="WE")
        # -----
        title_Example = ttk.Label(self, text="Ex: Domain Name System ", font=NORM_FONT)
        title_Example.grid(row=7, column=1, sticky="WE", padx=20, pady=(0,5))
        # --------------------------------------------------------------
        port_Label = ttk.Label(self, text="Related Port#: ", font=LARGE_FONT)
        port_Label.grid(row=8, column=0, sticky="W", padx=20)
        # -----
        port_input = ttk.Entry(self)
        port_input.grid(row=8, column=1, sticky="WE")
        # -----
        port_Example = ttk.Label(self, text="Ex: 443 ", font=NORM_FONT)
        port_Example.grid(row=9, column=1, sticky="WE", padx=20, pady=(0,5))
        # --------------------------------------------------------------
        protocol_Label = ttk.Label(self, text="Add Protocol: ", font=LARGE_FONT)
        protocol_Label.grid(row=10, column=0, sticky="W", padx=20)
        # -----
        protocol_input = ttk.Entry(self)
        protocol_input.grid(row=10, column=1, sticky="WE")
        # -----
        protocol_Example = ttk.Label(self, text="Ex: Secure Shell (SSH) (RFC 4250-4256) ", font=NORM_FONT)
        protocol_Example.grid(row=11, column=1, sticky="WE", padx=20, pady=(0,5))
        # --------------------------------------------------------------
        tcp_udp_Label = ttk.Label(self, text="TCP and/or UDP", font=LARGE_FONT)
        tcp_udp_Label.grid(row=12, column=0, sticky="W", padx=20)
        # -----
        tcp_udp_input = ttk.Entry(self)
        tcp_udp_input.grid(row=12, column=1, sticky="WE")
        # -----
        tcp_udp_Example = ttk.Label(self, text="Ex: TCP ", font=NORM_FONT)
        tcp_udp_Example.grid(row=13, column=1, sticky="WE", padx=20, pady=(0,5))
        # --------------------------------------------------------------
        def_Label = ttk.Label(self, text="Add Definition: ", font=LARGE_FONT)
        def_Label.grid(row=14, column=0, sticky="NW", padx=20)
        # -----
        # We changed from an Entrybox to a TextBox
        #def_input = ttk.Entry(self )
        #def_input.grid(row=14, column=1, sticky="WE")
        def_textBox = tk.Text(self, height=5, width=100)
        def_textBox.grid(row=14, column=1, sticky="WE")
        # -----
        # --------------------------------------------------------------
        # --------------------------------------------------------------
        # Label that updates with user input and button click
        self.defLiveLabel_textVar = StringVar()
        self.defLiveSampleLabel = "Example: " \
                                  "\n1) The Internet's system for converting alphabetic names into numeric IP addresses. " \
                                  "For example, when a Web address (URL) is typed into a browser, DNS servers return the " \
                                  "IP address of the Web server associated with that name." \
                                  "\n2) This is line 2" \
                                  "\n\n3) This is line number 3, with an extra blank line." \
                                  "\n\nPress 'View Current Definition' to see your definiton so far."
        self.defLiveLabel_textVar.set(self.defLiveSampleLabel)

        # Update the display label based on user input and button push
        def textUpdate():
            self.defLiveLabel_textVar.set(def_textBox.get("1.0", END))

        defLiveLabel = ttk.Label(self, textvariable=self.defLiveLabel_textVar, font=NORM_FONT, wraplength=950)
        defLiveLabel.grid(row=15, column=1, padx=(20,0), pady=(0,10), sticky="W")

        # --------------------------------------------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # --------------------------------------------------------------
        def writeFileButton_command():
            # For file we want to strip the end new lines from the text box.
            #       and add 1 new line to the beginning.
            textbox =  str(def_textBox.get("1.0", END))
            textbox = textbox.strip("\n")
            textbox = "\n" + textbox

            # -----------
            # Ignore unknown/unusable characters
            # This does ignore unusable copy and paste characters but, also ignores \n when a user wants a new line
            # in the definition. I am not sure how to remove unusables, but keep unicode needs.
            defUnicode_Ascii = textbox.encode("ascii", "ignore")
            print("defUniceode_Ascii = ", str(defUnicode_Ascii))
            convert = str(defUnicode_Ascii)
            # -----------

            appendToTxtFile(acro_input.get(), title_input.get(), port_input.get(), protocol_input.get(),
                            tcp_udp_input.get(), def_textBox.get("1.0", END)) #convert)

            # Data was just saved as an object. Ask user to save a photo
            # Popup with yes/no buttons. Yes lets user put in a photo directory
            addPhoto_popupmsg("Do you have a photo for: ", title_input.get())

            # Method to write input to file. Then clears the labels, for another possible input.
            acro_input.delete(0, END)
            title_input.delete(0, END)
            port_input.delete(0, END)
            protocol_input.delete(0, END)
            tcp_udp_input.delete(0, END)
            def_textBox.delete("1.0", END)
            self.defLiveLabel_textVar.set(self.defLiveSampleLabel)
        # ------------------------
        # ------------------------
        # Takes your inputs and it writes as a new object to the file.
        writeFileButton = ttk.Button(self, text="Write to Txt File", command=lambda: writeFileButton_command(),
                                     width=15)
        writeFileButton.grid(row=19, column=0, padx=(20,0), pady=(0,0), sticky="W")

        # ------------------------
        # Click the button and it will display your current definition text.
        setLabelButton = ttk.Button(self, text="View Current Definition", command=lambda: textUpdate())
        setLabelButton.grid(row=19, column=1, sticky="WE")
        # ----------------------------
        # ----------------------------
        # Next 3 lines. Return Adda 2 starts to input text. Converted into new line.
        # This worked with the Definition Entry, but we do not need this with a Textbox
        def add_2Stars_to_DefInput():
            # 2Stars in text is auto converted to a new line.
            # 2Stars are distinguishable and easy to insert
            # We have also directly tied ** to the return key.
            tempDef = def_textBox.get("1.0", END)
            tempDef = tempDef + "**"
            # ----------------------------
            # Can't change anything other than foreground....internet has not been helpful
            def_textBox.configure(foreground="red")
            def_textBox.delete("1.0", END)
            def_textBox.insert(END, tempDef)
        # ----------------------------
        # This ** from the return key worked with the Definition Entry, but we do not need this with a Textbox
        '''
        def return_Key(event):
            if len(event.char) == 1:
                # charcters like []/.,><#$ also Return and ctrl/key
                print('Punctuation666 Key %r (%r)' % (event.keysym, event.char))
                add_2Stars_to_DefInput()
        setLabelButton.bind_all('<Return>', return_Key)
        '''
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ttk will give us a good looking button
        def returnHome():
            readTxtFile()
            controller.show_frame(StartPage)
        returHomeButton = ttk.Button(self, text=" Return Home ",
                             command=lambda: returnHome(), width=15)
        returHomeButton.grid(row=0, column=0, padx=(20,0), sticky="W")
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
        mainlabel = ttk.Label(self, text="------------------------- Change File Page ----------------------------", font=XL_FONT)
        mainlabel.grid(row=0, column=2, padx=(0,0), pady=5, sticky="WE")
        # ----------------------------
        asklabel = ttk.Label(self, text="Option 1) Press 'Next' to see the next study object."
                                        "\nOption 2) Enter Position # and click 'Go To Position' to be specific."
                                        " 0 and 1 will both start from the beginning."
                                        "\nPress the 'Edit' buttons to change the current study attribute."
                                        "\nDefinitions may seem to be missing lines after you click 'edit'."
                                        " Just scroll through the red box, and the new lines will appear.",
                                        font=NORM_FONT)
                                        # Instruction when we used  **  in EntryBox. But we switched to TextBox
                                        #"\nIf you want a new line in a definition, add:     **     anywhere. ",
        # font=NORM_FONT)
        asklabel.grid(row=1, column=2, padx=(0,0), pady=5, sticky="WE")

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
            # Don't keep reading if we have already, only on -1
            deletePosition.grid(row=8, column=1, sticky="WE", padx=(20, 10), pady=(5, 5))

            if self.position ==-1:
                readTxtFile()
            # Can't go past the list lengths
            if self.position < len(global_fileData)-1:
                self.position += 1
                goto_input.delete(0, END)
                goto_input.insert(END, self.position+1)
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
            deletePosition.grid(row=8, column=1, sticky="WE", padx=(20, 10), pady=(5, 5))
            # We only have to read the file once for sure, at -1
            if self.position == -1:
                readTxtFile()

            # Called if the goto button is pressed
            if wanted_position == 0:
                wanted_position = wanted_position
            else: # User wants spot 2 but the list reads as spot 1  0-->1-->2
                wanted_position = wanted_position-1

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
                self.newInput = "Acronym:     " + new_inputBox.get("1.0", END)
                acronymLabel_textVar.set(self.newInput)
                global_fileData[self.position].acronym = self.newInput
                changeTxtFile()

            elif self.attribute == "Tit":
                self.newInput = "Title:           " + new_inputBox.get("1.0", END)
                titleLabel_textVar.set(self.newInput)
                global_fileData[self.position].title = self.newInput
                changeTxtFile()

            elif self.attribute == "Por":
                self.newInput = "Port:           " + new_inputBox.get("1.0", END)
                portLabel_textVar.set(self.newInput)
                global_fileData[self.position].port = self.newInput
                changeTxtFile()

            elif self.attribute == "Pro":
                self.newInput = "Protocol:      " + new_inputBox.get("1.0", END)
                protocolLabel_textVar.set(self.newInput)
                global_fileData[self.position].protocol = self.newInput
                changeTxtFile()

            elif self.attribute == "TCP":
                self.newInput = "TCP_UDP:     " + new_inputBox.get("1.0", END)
                tcp_udp_Label_textVar.set(self.newInput)
                global_fileData[self.position].tcp_udp = self.newInput
                changeTxtFile()

            elif self.attribute == "Def":
                self.newInput = "Definition:           " + new_inputBox.get("1.0", END)
                definitionLabel_textVar.set(self.newInput)
                global_fileData[self.position].definition = self.newInput
                changeTxtFile()
            callBack_buttons()

        # =================
        # --- Edit Acronym button method
        saveButton = ttk.Button(self, text="Save", command=saveNewInput, width=15)
        new_inputBox = tk.Text(self, height=5, width=90)

        def edit_Acronym():
            # self.position   holds the position we want to change
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Grab the first 3 chars from the line. Use to tell saveNewInput --> Will get 'Acr'
            self.attribute = global_fileData[self.position].__str__("acronym")[0:3]
            clear_Labels()
            # Get rid of the top parts
            pushAway_Buttons()

            # ----------------
            # Create Entry box for the attribute that was selected
            #new_inputBox = ttk.Entry(self, width=70)
            new_inputBox.configure(foreground="red")
            # ----- attribute includes word 'Acronymm' plus 5 spaces. Remove those
            acronym = global_fileData[self.position].__str__("acronym")
            acronym = acronym[13:]
            # Show the Value in the entry box in red
            new_inputBox.delete("1.0", END)
            new_inputBox.insert(END, acronym)
            new_inputBox.grid(row=3, column=2, padx=(5, 0), sticky="WE")
            # Set the acronym label with the original so user can see what it was
            acronymLabel_textVar.set(global_fileData[self.position].__str__("acronym"))
            # =================
            # --- Display Save button
            # We just showed the button, now the user can click it
            #saveButton = ttk.Button(self, text="Save", command=saveNewInput, width=15)
            saveButton.grid(row=3, column=1, padx=(20, 0), sticky="NW")
        # =================
        def edit_Title():
            # self.position   holds the position we want to change
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Grab the first 3 chars from the line. Use to tell saveNewInput --> Will get 'Tit'
            self.attribute = global_fileData[self.position].__str__("title")[0:3]
            clear_Labels()
            # Get rid of the top parts
            pushAway_Buttons()

            # ----------------
            # Create Entry box for the attribute that was selected
            new_inputBox.configure(foreground="red")
            # ----- attribute includes word 'Acronymm' plus 5 spaces. Remove those
            title = global_fileData[self.position].__str__("title")
            title = title[17:]
            # Show the Value in the entry box in red
            new_inputBox.delete("1.0", END)
            new_inputBox.insert(END, title)
            new_inputBox.grid(row=3, column=2, padx=(5, 0), sticky="WE")
            # Set the acronym label with the original so user can see what it was
            titleLabel_textVar.set(global_fileData[self.position].__str__("title"))
            # =================
            # --- Display Save button
            # We just showed the button, now the user can click it
            saveButton.grid(row=3, column=1, padx=(20, 0), sticky="NW")
        # =================
        def edit_Port():
            # self.position   holds the position we want to change
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Grab the first 3 chars from the line. Use to tell saveNewInput --> Will get 'Por'
            self.attribute = global_fileData[self.position].__str__("port")[0:3]
            clear_Labels()
            # Get rid of the top parts
            pushAway_Buttons()

            # ----------------
            # Create Entry box for the attribute that was selected
            new_inputBox.configure(foreground="red")
            # ----- attribute includes word 'Acronymm' plus 5 spaces. Remove those
            port = global_fileData[self.position].__str__("port")
            port = port[16:]
            # Show the Value in the entry box in red
            new_inputBox.delete("1.0", END)
            new_inputBox.insert(END, port)
            new_inputBox.grid(row=3, column=2, padx=(5, 0), sticky="WE")
            # Set the acronym label with original
            portLabel_textVar.set(global_fileData[self.position].__str__("port"))
            # =================
            # --- Display Save button
            # We just showed the button, now the user can click it
            saveButton.grid(row=3, column=1, padx=(20, 0), sticky="NW")
        # =================
        def edit_Protocol():
            # self.position   holds the position we want to change
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Grab the first 3 chars from the line. Use to tell saveNewInput --> Will get 'Pro'
            self.attribute = global_fileData[self.position].__str__("protocol")[0:3]
            clear_Labels()
            # Get rid of the top parts
            pushAway_Buttons()

            # ----------------
            # Create Entry box for the attribute that was selected
            new_inputBox.configure(foreground="red")
            # ----- attribute includes word 'Acronymm' plus 5 spaces. Remove those
            protocol = global_fileData[self.position].__str__("protocol")
            protocol = protocol[15:]
            # Show the Value in the entry box in red
            new_inputBox.delete("1.0", END)
            new_inputBox.insert(END, protocol)
            new_inputBox.grid(row=3, column=2, padx=(5, 0), sticky="WE")
            # Set the acronym label with original
            protocolLabel_textVar.set(global_fileData[self.position].__str__("protocol"))
            # =================
            # --- Display Save button
            # We just showed the button, now the user can click it
            saveButton.grid(row=3, column=1, padx=(20, 0), sticky="NW")
        # =================
        def edit_TCP_UDP():
            # self.position   holds the position we want to change
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Grab the first 3 chars from the line. Use to tell saveNewInput --> Will get 'TCP'
            self.attribute = global_fileData[self.position].__str__("tcp_udp")[0:3]
            clear_Labels()
            # Get rid of the top parts
            pushAway_Buttons()

            # ----------------
            # Create Entry box for the attribute that was selected
            new_inputBox.configure(foreground="red")
            # ----- attribute includes word 'Acronymm' plus 5 spaces. Remove those
            tcp_udp = global_fileData[self.position].__str__("tcp_udp")
            tcp_udp = tcp_udp[13:]
            # Show the Value in the entry box in red
            new_inputBox.delete("1.0", END)
            new_inputBox.insert(END, tcp_udp)
            new_inputBox.grid(row=3, column=2, padx=(5, 0), sticky="NW")
            # Set the acronym label with original
            tcp_udp_Label_textVar.set(global_fileData[self.position].__str__("tcp_udp"))
            # =================
            # --- Display Save button
            # We just showed the button, now the user can click it
            saveButton.grid(row=3, column=1, padx=(20, 0), sticky="WE")
        # =================
        def edit_Definition():
            # self.position   holds the position we want to change
            # If user starts on this page we need to auto read in the file.
            readTxtFile()
            # Grab the first 3 chars from the line. Use to tell saveNewInput --> Will get 'Def'
            self.attribute = global_fileData[self.position].__str__("definition")[0:3]
            clear_Labels()
            # Get rid of the top parts
            pushAway_Buttons()
            # ----------------
            # Create Entry box for the attribute that was selected
            new_inputBox.configure(foreground="red")
            # ----- attribute includes word 'Acronymm' plus 5 spaces. Remove those
            definition = global_fileData[self.position].__str__("definition")
            definition = definition[22:]
            # Show the Value in the entry box in red
            new_inputBox.delete("1.0", END)
            new_inputBox.insert(END, definition)
            new_inputBox.grid(row=3, column=2, padx=(5, 0), sticky="WE")
            # Set the acronym label with original
            definitionLabel_textVar.set(global_fileData[self.position].__str__("definition"))
            # =================
            # --- Display Save button
            # We just showed the button, now the user can click it
            saveButton.grid(row=3, column=1, padx=(20, 0), sticky="NW")

            # =================
        # =================
        def pushAway_Buttons():
            # This is to hide the goto button, goto Entry and next button
            # Also is to display the save button and new input box.
            new_inputBox.grid(row=3, column=2, padx=(20, 0), sticky="W")
            saveButton.grid(row=6, column=1, padx=(20, 0), sticky="W")
            deletePosition.grid(row=8, column=1, sticky="WE", padx=(20, 10), pady=(0, 0))

            gotoButton.grid(row=23, column=20, padx=(20, 0), sticky="E")
            goto_input.grid(row=24, column=20, padx=(20, 0), sticky="E")
            nextButton.grid(row=25, column=20, padx=(20, 0), pady=(0, 0), sticky="E")
        # =================
        def callBack_buttons():
            # This is to hide the save button and input box
            # Also to bring back the goto button, next button, inputbox, display labels
            # Hidden Save Position
            saveButton.grid(row=26, column=20, padx=(20, 0), sticky="E")
            new_inputBox.grid(row=23, column=20, padx=(20, 0), sticky="E")
            deletePosition.grid(row=28, column=21, sticky="WE", padx=(20, 10), pady=(0, 0))

            # =================
            # Original position
            gotoButton.grid(row=3, column=1, padx=(20, 0), sticky="W")
            goto_input.grid(row=4, column=1, padx=(50, 0), sticky="W")
            nextButton.grid(row=4, column=2, padx=(5, 0), pady=(0, 0), sticky="W")

            #
            acronymLabel_textVar.set(global_fileData[self.position].__str__("acronym"))
            titleLabel_textVar.set(global_fileData[self.position].__str__("title"))
            portLabel_textVar.set(global_fileData[self.position].__str__("port"))
            protocolLabel_textVar.set(global_fileData[self.position].__str__("protocol"))
            tcp_udp_Label_textVar.set(global_fileData[self.position].__str__("tcp_udp"))
            definitionLabel_textVar.set(global_fileData[self.position].__str__("definition"))
        # ================




        # --- Goto button
        # User can enter an int to view a specifc position
        gotoButton = ttk.Button(self, text="Go To Position:",
                                command=lambda: goTo(int(goto_input.get())))
        gotoButton.grid(row=3, column=1, padx=(20,0), sticky="W")

        # ----------------------------
        # Can't change anything other than foreground....internet has not been helpful
        goto_input = ttk.Entry(self, width=10)
        goto_input.configure(foreground="red")
        goto_input.insert(END, '0')
        goto_input.grid(row=4, column=1, padx=(50,0), sticky="W")

        # =================
        # =================
        # =================
        # --- Next button
        nextButton = ttk.Button(self, text="Next", command=lambda: state_FullFile(self.position))
        nextButton.grid(row=4, column=2, padx=(5,0), pady=(0,0), sticky="W")
        # ----------------------------
        # =================
        # --- Position label
        viewFileLabel_textVar = StringVar()
        viewFileLabel_textVar.set('Position: 0')
        # Note: wraplegth keeps the definition in the current window frame.
        # I don't know if we need this on the other 5 yet
        viewFileLabel = ttk.Label(self, textvariable=viewFileLabel_textVar,
                                    font=LARGE_FONT, wraplength=1000)
        viewFileLabel.grid(row=8, column=2, sticky="W", padx=(5,0), pady=(0,0))
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
                                    font=NORM_FONT, wraplength=1000)
        definitionLabel.grid(row=14, column=2, sticky="W",  padx=(5, 0), pady=(5,0))
        # ===================================================
        # ===================================================
        # =================
        # ----------------------------
        # Button to go back home
        returHomeButtonf = ttk.Button(self, text=" Return Home",
                             command=lambda: controller.show_frame(StartPage), width=15)
        returHomeButtonf.grid(row=0, column=1, sticky="W", padx=(20,0))
        # ----------------------------
        # Button to go delete this current spot
        # Popup window with question and yes/no buttons. Dont let user delete unless confirmed.
        deletePosition = ttk.Button(self, text="Delete This Position",
                             command=lambda: areYouSure_popupmsg(self.position, global_fileData[
                                 self.position].__str__("title")))
        deletePosition.grid(row=28, column=1, sticky="WE", padx=(20,10), pady=(50,0))
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
        mainlabel = ttk.Label(self, text="StudyPage: Use Page Buttons & Keyboard Shortcuts", font=XL_FONT)
        mainlabel.grid(row=0, column=2, padx=(10,0), pady=10, sticky="W")
        # -----
        #-----------------
        #Key bind Labels
        keybind_label1B = ttk.Label(self, text="Keyboard: Right Arrow --> Move to Next Position", font=NORM_FONT)
        keybind_label1B.grid(row=1, column=2, padx=10, sticky="W")
        # -----
        # ---
        keybind_label2B = ttk.Label(self, text="Keyboard: Down Arrow -> Show All Traits", font=NORM_FONT)
        keybind_label2B.grid(row=2, column=2, padx=10, sticky="W")
        # -----
        # ---
        keybind_label3B = ttk.Label(self, text="Keyboard: Up Arrow ----> Acronym > Title > Port > Protocol > TCP/UDP > Definition > Clear All",
                                    font=NORM_FONT)
        keybind_label3B.grid(row=3, column=2, padx=10, pady=(0,0), sticky="W")
        # -----
        # ---
        keybind_label4B = ttk.Label(self, text="Keyboard: Left Arrow ---> Move to Previous Position",
                                    font=NORM_FONT)
        keybind_label4B.grid(row=4, column=2, padx=10, pady=(0,20), sticky="W")
        # ---
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
            self.attribute_count = 1
        # ---
        # ==================================================
        self.studyNumber = 0
        # Remember, we are displaying the values +1 to the user of how python reads the list
        # In the list the first spot is 0, but users like 1 better
        def state_currentPosition():
            print(global_SearchReturnPosition)
            return ("Position:" + str(global_SearchReturnPosition + 1))
        # ---

        # =============
        # Change the value for the user in seeking in the StudyObject list
        # This is for the single increment for the next object
        # Can't be more than the len - 1
        global global_SearchReturnPosition
        def next_StudyObject():
            # called a readTxtFile from the start page. Shouldnt need to anymore on this page.
            # Commented out for now. Should delete if not needed

            # We need to clear the current labels
            clear_Labels()
            global global_SearchReturnPosition
            if global_SearchReturnPosition < len(global_fileData)-1:
                global_SearchReturnPosition += 1
                check_IfPhotoExists()
                listPositionLabel_textVar.set(state_currentPosition())

            else:
                print("\n There are no more objects")
                global_SearchReturnPosition = 0
                listPositionLabel_textVar.set(state_currentPosition())
        # ---
        # =============
        # ==================================================
        # Change the value for the user in seeking in the previous object in the StudyObject list
        # This is for the single decrement for the next object
        # Zero will recycle to len - 1
        def prev_StudyObject():
            # called a readTxtFile from the start page. Shouldnt need to anymore on this page.
            global global_SearchReturnPosition

            # We need to clear the current labels
            clear_Labels()
            if global_SearchReturnPosition> 0:
                global_SearchReturnPosition -= 1
                check_IfPhotoExists()
                listPositionLabel_textVar.set(state_currentPosition())

            else:
                global_SearchReturnPosition = len(global_fileData)-1
                check_IfPhotoExists()
                listPositionLabel_textVar.set(state_currentPosition())
        # ---
        # =============
        # ==================================================
        # Allow the user to get a random study object from the list.
        def random_StudyObject():
            # called a readTxtFile from the start page. Shouldnt need to anymore on this page.
            global global_SearchReturnPosition
            # We need to clear the current labels
            clear_Labels()
            # Don't go past the last one.
            global_SearchReturnPosition = random.randint(0, len(global_fileData)-1)
            check_IfPhotoExists()
            listPositionLabel_textVar.set(state_currentPosition())
        # ---
        # =============
        # ==================================================
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # User clicks a button with what they want from of the 6 object values
        # The button calls this method while sending the stated value that they want.
        # readTxtFile(): Make sure that the global_list is refreshed when the 6 buttons are clicked
        def state_Acronym():
            # Make sure we have imported a list on the first round.
            # called a readTxtFile from the start page. Shouldnt need to anymore on this page.
            # Commented out for now. Should delete if not needed
            update_label()
            acronymLabel_textVar.set(global_fileData[global_SearchReturnPosition].__str__("acronym"))
            self.attribute_count = 2
            # ---
        # ----------------------------
        def state_Title():
            # Make sure we have imported a list on the first round.
            # called a readTxtFile from the start page. Shouldnt need to anymore on this page.
            # Commented out for now. Should delete if not needed
            update_label()
            titleLabel_textVar.set(global_fileData[global_SearchReturnPosition].__str__("title"))
            self.attribute_count = 3
            # ---
        # ----------------------------
        def state_Port():
            # Make sure we have imported a list on the first round.
            # called a readTxtFile from the start page. Shouldnt need to anymore on this page.
            # Commented out for now. Should delete if not needed
            update_label()
            portLabel_textVar.set(global_fileData[global_SearchReturnPosition].__str__("port"))
            self.attribute_count = 4
            # ---
        # ----------------------------
        def state_Protocol():
            # Make sure we have imported a list on the first round.
            # called a readTxtFile from the start page. Shouldnt need to anymore on this page.
            # Commented out for now. Should delete if not needed
            update_label()
            protocolLabel_textVar.set(global_fileData[global_SearchReturnPosition].__str__("protocol"))
            self.attribute_count = 5
            # ---
        # ----------------------------
        def state_Tcp_Udp():
            # Make sure we have imported a list on the first round.
            # called a readTxtFile from the start page. Shouldnt need to anymore on this page.
            # Commented out for now. Should delete if not needed
            update_label()
            tcp_udp_Label_textVar.set(global_fileData[global_SearchReturnPosition].__str__("tcp_udp"))
            self.attribute_count = 6
            # ---
        # ----------------------------
        def state_Definition():
            # Make sure we have imported a list on the first round.
            # called a readTxtFile from the start page. Shouldnt need to anymore on this page.
            # Commented out for now. Should delete if not needed
            update_label()
            definitionLabel_textVar.set(global_fileData[global_SearchReturnPosition].__str__("definition"))
            self.attribute_count = 7
            # ---
        # ----------------------------
        # ---
        def state_All6():
            state_Acronym()
            state_Title()
            state_Port()
            state_Protocol()
            state_Tcp_Udp()
            state_Definition()
        # ==================================================
        def update_label():

            listPositionLabel_textVar.set(state_currentPosition())
        # ----------------------------
        # The methods(above), 6 study page methods
        #       and the labels (below) for the 6 labels on StudyPage
        #       and the 6 buttons
        # ----------------------------
        # ----------------------------
        # --- Acronym button
        stateAcronymButton = ttk.Button(self, text="Acronym", command=state_Acronym, width=10)
        stateAcronymButton.grid(row=5, column=1, sticky="W", padx=(20,0), pady=(0,10))
        # ---
        # --- Acronym label
        acronymLabel_textVar = StringVar()
        acronymLabel_textVar.set(':')
        acronymLabel = ttk.Label(self, textvariable=acronymLabel_textVar, font=LARGE_FONT)
        acronymLabel.grid(row=5, column=2, sticky="W", pady=(0,10))
        # ----------------------------
        # ----------------------------
        # --- Title button
        stateTitleButton = ttk.Button(self, text="Title", command=state_Title, width=10)
        stateTitleButton.grid(row=6, column=1, sticky="W", padx=(20,0), pady=(0,10))
        # ---
        # --- Title label
        titleLabel_textVar = StringVar()
        titleLabel_textVar.set(':')
        titleLabel = ttk.Label(self, textvariable=titleLabel_textVar, font=LARGE_FONT)
        titleLabel.grid(row=6, column=2, sticky="W", pady=(0,10))
        # ----------------------------
        # ----------------------------
        # --- Port button
        statePortButton = ttk.Button(self, text="Port", command=state_Port, width=10)
        statePortButton.grid(row=7, column=1, sticky="W", padx=(20,0), pady=(0,10))
        # ---
        # --- Port label
        portLabel_textVar = StringVar()
        portLabel_textVar.set(':')
        portLabel = ttk.Label(self, textvariable=portLabel_textVar, font=LARGE_FONT)
        portLabel.grid(row=7, column=2, sticky="W", pady=(0,10))
        # ----------------------------
        # ----------------------------
        # --- Protocol button
        stateProtocolButton = ttk.Button(self, text="Protocol", command=state_Protocol, width=10)
        stateProtocolButton.grid(row=8, column=1, sticky="W", padx=(20,0), pady=(0,10))
        # ---
        # --- Protocol label
        protocolLabel_textVar = StringVar()
        protocolLabel_textVar.set(':')
        protocolLabel = ttk.Label(self, textvariable=protocolLabel_textVar, font=LARGE_FONT)
        protocolLabel.grid(row=8, column=2, sticky="W", pady=(0,10))
        # ----------------------------
        # ----------------------------
        # --- TCP_UDP button
        state_tcp_udp_Button = ttk.Button(self, text="TCP/UDP", command=state_Tcp_Udp, width=10)
        state_tcp_udp_Button.grid(row=9, column=1, sticky="W", padx=(20,0), pady=(0,10))
        # ---
        # --- TCP_UDP label
        tcp_udp_Label_textVar = StringVar()
        tcp_udp_Label_textVar.set(':')
        tcp_udp_Label = ttk.Label(self, textvariable=tcp_udp_Label_textVar, font=LARGE_FONT)
        tcp_udp_Label.grid(row=9, column=2, sticky="W", pady=(0,10))
        # ----------------------------
        # ----------------------------
        # --- Definition button
        stateDefinitionButton = ttk.Button(self, text="Definition", command=state_Definition, width=10)
        stateDefinitionButton.grid(row=10, column=1, sticky="WN", padx=(20,0), pady=(0,10))
        # ---
        # --- Definition label
        definitionLabel_textVar = StringVar()
        definitionLabel_textVar.set(':')
        # Note: wraplegth keeps the definition in the current window frame.
        # I don't know if we need this on the other 5 yet
        definitionLabel = ttk.Label(self, textvariable=definitionLabel_textVar,
                                    font=NORM_FONT, wraplength=1000)
        definitionLabel.grid(row=10, column=2, sticky="W", pady=(0,10))
        # ---
        # ---
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # We are calling these 3 in the set_Global_PhotoDirectoy method.
        #       Must create them out here first.
        self.returnButton = ttk.Button(self, text="Go Back", command=lambda: destroyPic_Label_Button())
        self.label1 = ttk.Label(self)
        self.label2 = ttk.Label(self,
                                text="-----------------------------------------------------------------------------"
                                     "-----------------------------------------------------------------------------"
                                     "-----------------------------------------------------------------------------------")
        # We are settring these 3 to view a related photo. Need to remove when user wants to see StudyPage again
        #       Called in set_Global_PhotoDirectory.
        def destroyPic_Label_Button():
            self.returnButton.destroy()
            self.label1.destroy()
            self.label2.destroy()
        # ----------------------------
        # This method, calls a global method that returns a resized photo
        # When the resized photo returns it is set as a label
        def place_thePicture():
            resized = set_Global_PhotoDirectory(global_SearchReturnPosition, global_fileData[global_SearchReturnPosition].__str__(
                "title"))
            self.photo1 = ImageTk.PhotoImage(resized)
            self.label1 = ttk.Label(self, image=self.photo1)
            self.label1.resized = self.photo1
            self.label1.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="WE")
            # -----------
            # Label is to push every thing else off the screen without destroying it.
            self.label2 = ttk.Label(self,
                                    text="-----------------------------------------------------------------------------"
                                         "-----------------------------------------------------------------------------"
                                         "-----------------------------------------------------------------------------------")
            self.label2.grid(row=1, column=0, padx=(20, 0), pady=10, sticky="WE")
            # -----------
            self.returnButton = ttk.Button(self, text="Go Back", command=lambda: destroyPic_Label_Button(), width=30)
            self.returnButton.grid(row=2, column=0, sticky="W", padx=(20,0))
        # ----------------------------
        # ----------------------------
        # ----------------------------
        def check_IfPhotoExists():
            # If director address for photo exists, button will change to "View Photo"
            # photo address ends with the current object title, so we can check specifically
            from pathlib import Path
            title = global_fileData[global_SearchReturnPosition].__str__("title")
            # Cut down from:    Title:      Secure Shell    to just     Secure Shell
            title = title[17:] + ".png"
            my_Photo = Path(globalPhoto_Directory + title)
            if my_Photo.is_file():
                # Page sub-methods to change the text on the photo button.
                yes_Picture()
            else:
                no_Picture()

        # ----------------------------
        # Show a related picture button
        # We have the base format here, then will call yes/no functions when a new object is changed.
        # If the photo address is True call the yes method  or else  call the no method.
        # We are using the tk format instead of ttk format. Auto provides a subtle border
        pictureButton = tk.Button(self, text="No Picture Available", command=lambda: place_thePicture())
        pictureButton.configure(font=('Sans', '20', 'bold'), background='blue', foreground='#eeeeff')
        pictureButton.grid(row=16, column=2, sticky="WE", padx=(20,0))
        def no_Picture():
            pictureButton = tk.Button(self, text="No Picture Available", command=lambda: place_thePicture())
            pictureButton.configure(font=('Sans', '16', 'bold'), background='blue', foreground='#eeeeff')
            pictureButton.grid(row=16, column=2, sticky="WE", padx=(20, 0))
        def yes_Picture():
            pictureButton = tk.Button(self, text="View Picture", command=lambda: place_thePicture())
            pictureButton.configure(font=('Sans', '20', 'bold'), background='blue', foreground='#eeeeff')
            pictureButton.grid(row=16, column=2, sticky="WE", padx=(20, 0))
        # ----------------------------
        # ----------------------------
        # --- StateAll button
        stateAllButton = ttk.Button(self, text="All Traits", command=state_All6, width=10)
        stateAllButton.grid(row=15, column=1, sticky="W", padx=(20,0))
        # ---
        # ----------------------------
        # --- Clear All / Redo button
        clearAllredoButton = ttk.Button(self, text="Clear/Redo", command=clear_Labels)
        clearAllredoButton.grid(row=15, column=2, sticky="WE", padx=(20,0))
        # --- Position label
        listPositionLabel_textVar = StringVar()
        listPositionLabel_textVar.set(str(state_currentPosition()))
        listPositionLabel = ttk.Label(self, textvariable=listPositionLabel_textVar, font=LARGE_FONT)
        listPositionLabel.grid(row=16, column=1, sticky="E", padx=(20,20), pady=(5,5))

        # ----------------------------
        # Button to increase the studyNumber + 1 to call for the next object
        increaseByOneButton = ttk.Button(self, text="Next", command=next_StudyObject, width=10)
        increaseByOneButton.grid(row=17, column=1, sticky="W", padx=(20,0), pady=(0,5))
        # ----------------------------
        # Button to get a random studyNumber for the next object
        randomNumberButton = ttk.Button(self, text="Random", command=random_StudyObject)
        randomNumberButton.grid(row=17, column=2, sticky="WE", padx=(20,0), pady=(0,5))
        # ----------------------------
        # ---
        # ---
        # User wants to search. Will take you to the search page.
        searchButton = ttk.Button(self, text="Search For: ", command=lambda: controller.show_frame(SearchPage), width=10)
        searchButton.grid(row=18, column=1, sticky="W", padx=(20,0), pady=(0,5))

        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # Keyboard binds
        # Details are in the pseudo-keylogger page for the programmer
        # Remember we have to bind this to a created StudyPage button
        # ------------------
        # ----------------------------
        # Move to the next object
        def right_Key(event):
            # If we are on this StudyPage, the right keyboard button will move to the next object
            if len(event.char) == 1:
            # charcters like []/.,><#$ also Return and ctrl/key
                print('Punctuation666 Key %r (%r)' % (event.keysym, event.char))
                next_StudyObject()
        increaseByOneButton.bind_all('<Right>', right_Key)
        # ---
        # ----------------------------
        # States all the attributes at once
        def down_Key(event):
            if len(event.char) == 1:
            # charcters like []/.,><#$ also Return and ctrl/key
                print('Punctuation666 Key %r (%r)' % (event.keysym, event.char))
                state_All6()
        stateAllButton.bind_all('<Down>', down_Key)
        # ---
        # ----------------------------
        # self.attribute and method allow for up key to state attributes.
        self.attribute_count=1
        def ac_ti_po_pr_tc_de():
            if self.attribute_count == 1:
                state_Acronym()
            elif self.attribute_count == 2:
                state_Title()
            elif self.attribute_count == 3:
                state_Port()
            elif self.attribute_count == 4:
                state_Protocol()
            elif self.attribute_count == 5:
                state_Tcp_Udp()
            elif self.attribute_count == 6:
                state_Definition()
            elif self.attribute_count == 7:
                clear_Labels()
        # ---
        # Up key an object's displays attributes step x step. Call method right above.
        def up_Key(event):
            if len(event.char) == 1:
            # charcters like []/.,><#$ also Return and ctrl/key
                print('Punctuation666 Key %r (%r)' % (event.keysym, event.char))
                ac_ti_po_pr_tc_de()
        # Must bind to an existing button, even if not the same task.
        stateAllButton.bind_all('<Up>', up_Key)
        # ---
        # ----------------------------
        # Left moves to the previous list object
        def left_Key(event):
            if len(event.char) == 1:
            # charcters like []/.,><#$ also Return and ctrl/key
                print('Punctuation666 Key %r (%r)' % (event.keysym, event.char))
                prev_StudyObject()
        # Must bind to an existing button, even if not the same task.
        stateAllButton.bind_all('<Left>', left_Key)
        # ----------------------------
        # ---

        def mouse_Move(event):
            if len(event.char) == 1:
            # charcters like []/.,><#$ also Return and ctrl/key
                print('Punctuation666 Key %r (%r)' % (event.keysym, event.char))
                update_label()
        # Must bind to an existing button, even if not the same task.
        stateAllButton.bind_all('<Key-q>', mouse_Move)
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # Button to go back home
        returHomeButtonf = ttk.Button(self, text="Return Home",
                             command=lambda: controller.show_frame(StartPage), width=10)
        returHomeButtonf.grid(row=0, column=1, sticky="W", padx=(20,0))
# ==================================================
# ==================================================
# ==================================================
# ==================================================
class SearchPage(ttk.Frame):
    # -----
        # -------------------------
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        mainlabel = ttk.Label(self, text="SearchPage", font=XL_FONT)
        mainlabel.grid(row=0, column=2, padx=(10,0), pady=10, sticky="W")
        # -------------------------
        # ----
        # Top example label
        label1 = ttk.Label(self, text="What do you want to search for?"
                                       "\nExamples:"
                                       "\n\tIDS"
                                       "\n\tIntrusion Detection System", font=LARGE_FONT)
        label1.grid(row=1, column=2, padx=(10,0), pady=10, sticky="W")
        # -------------------------
        # ----
        # 2nd label, grabs user search input from the StudyPage
        # This can be set using the method  updateSearchLabel  but it needs to be clicked.
        #label2 = ttk.Label(self, text="\tSearching For: " + str(global_UserSearchString.get()), font=LARGE_FONT)
        label2 = ttk.Label(self, text="\tSearching For: " + global_UserSearchString, font=LARGE_FONT)

        label2.grid(row=2, column=2, padx=(10,0), pady=10, sticky="W")
        # -------------------------
        # ----
        def searchButtonMethod():
            # Set the global search string, and call the search page
            # Clear the labelSearch, so we dont double print searches.
            self.labelSearch0_24 = ""
            self.labelSearch25_49 = ""
            global global_UserSearchString
            global_UserSearchString = str(search_input.get())
            updateSearchLabel()
        # -------------------------
        # ----
        # Will grab user search input box and take to popup window method
        searchButton = ttk.Button(self, text="Search For: ", command=lambda: searchButtonMethod(), width=10)
        searchButton.grid(row=3, column=1, sticky="W", padx=(20,0), pady=(0,5))
        # -------------------------
        # ----
        # Input box for user to input search string
        search_input = ttk.Entry(self, width=10)
        search_input.configure(foreground="red")
        search_input.insert(END, '0')
        search_input.grid(row=3, column=2, sticky="WE", padx=(20,0), pady=(0,5))
        # -------------------------
        # ----
        # If global search variable matches, then the object's number and attribute are placed in the list.
        self.searchList = []
        def createSearchList():
            global global_UserSearchString
            if len(self.searchList) == 112:
                self.searchList = []

            for n in range(0, len(global_fileData)):

                if global_UserSearchString == global_fileData[n].__str__("acronym")[13:]:
                    self.searchList.append(n)
                    self.searchList.append(global_fileData[n].__str__("acronym"))
                if global_UserSearchString == global_fileData[n].__str__("title")[17:]:
                    self.searchList.append(n)
                    self.searchList.append(global_fileData[n].__str__("title"))
                if global_UserSearchString == global_fileData[n].__str__("port")[16:]:
                    self.searchList.append(n)
                    self.searchList.append(global_fileData[n].__str__("port"))
                if global_UserSearchString == global_fileData[n].__str__("protocol")[15:]:
                    self.searchList.append(n)
                    self.searchList.append(global_fileData[n].__str__("protocol"))
                if global_UserSearchString == global_fileData[n].__str__("tcp_udp")[13:]:
                    self.searchList.append(n)
                    self.searchList.append(global_fileData[n].__str__("tcp_udp"))
                if global_UserSearchString == global_fileData[n].__str__("definition")[22:]:
                    self.searchList.append(n)
                    self.searchList.append(global_fileData[n].__str__("definition"))
        # -------------------------
        # ----
        # Label that will be appended to and printed on screen with formatted search results.
        self.labelSearch0_24 = ""
        self.labelSearch25_49 = ""
        def setSearchReturn_Label():
            for n in range(0, len(self.searchList)):
                # Even numbers will always be the position number. Odd numbers will be: ex. Acronym    DNS
                # We want to display the list position + 1 so user can relate easily.
                # Our tkinter screen only handles 56 lines, 28 on each label
                #       That translates to 112 on the list
                if n == 112:
                    break

                if n % 2 == 0 and n < 56:
                    # -------------------------
                    self.labelSearch0_24 += "Position: " + str(self.searchList[n] + 1)
                if n % 2 == 0 and n >= 56:
                    self.labelSearch25_49 += "Position: " + str(self.searchList[n] + 1)
                    # -------------------------
                if n % 2 != 0 and n < 56:
                    self.labelSearch0_24 += "\t" + str(self.searchList[n])
                    # Formatting, drop a line for the popup window print job.
                    self.labelSearch0_24 += "\n"
                    # -------------------------
                if n % 2 != 0 and n >= 56:
                    self.labelSearch25_49 += "\t" + str(self.searchList[n])
                    # Formatting, drop a line for the popup window print job.
                    self.labelSearch25_49 += "\n"
                    # -------------------------
            # Formatted the String label from the search data. Now assign to a label.
            # Search page an only hold 25 print lines, if List[0 "string"] > 50
            #       We have to print 0-24 label3Live, and 25-49 on label4Live
            label3Live = ttk.Label(self, text=self.labelSearch0_24, font=NORM_FONT)
            label3Live.grid(row=4, column=2, padx=(10, 0), pady=10, sticky="NW")
            # -------------------------
            # ----
            label4Live = ttk.Label(self, text=self.labelSearch25_49, font=NORM_FONT)
            label4Live.grid(row=4, column=3, padx=(10, 0), pady=10, sticky="NE")
        # -------------------------
        # ----
        def updateSearchLabel():
            # This sets the label using the global search var.
            # The label is not set completely. It sets itself before a user enters the search.
            # This Function is called from the Set Your Wanted Position Button but that is inefficient.
            global global_UserSearchString
            label2 = ttk.Label(self, text="\tSearching For: " + global_UserSearchString, font=LARGE_FONT)
            label2.grid(row=2, column=2, padx=(10, 0), pady=10, sticky="W")

            createSearchList()
            setSearchReturn_Label()

            # -------------------------
            # -------------------------
        # -------------------------
        # ----
        # This for loop auto runs upon popup window opening.
        # Loop currently finds everything that exactly matches search parameter. Capitalization applies
        # Loop pushes everything in global list that matches from both acronym and title.
        # -------------------------
        # ----
        # Label to ask user what position they want to return to Study page with
        enterPositionLabel = ttk.Label(self, text="Enter Wanted Position: ")
        enterPositionLabel.grid(row=5, column=2, padx=(10,0), pady=(10,0), sticky="W")

        # -------------------------
        # ----
        # Entry box for user to enter which position that they want to go back with
        returnPosition = ttk.Entry(self, width=15)
        returnPosition.grid(row=6, column=2, padx=(10,0), pady=(0,0), sticky="W")
        # -------------------------
        # ----
        # Value and sub function to bring back
        def position_ButtonMethod():
            global global_SearchReturnPosition
            print("search method - global_SearchReturnPosition = " + str(global_SearchReturnPosition))
            global_SearchReturnPosition = (int(returnPosition.get()) - 1)
            print("search method - global_SearchReturnPosition = " + str(global_SearchReturnPosition))

        # -------------------------
        # ----
        setPositionButton = ttk.Button(self, text="Set Your Wanted Postition",
                                       command=lambda: position_ButtonMethod())
        setPositionButton.grid(row=7, column=2, padx=(10,0), pady=(0,10), sticky="W")
        # -------------------------
        # ----
        def returnHomeButton_Method():
            position_ButtonMethod()
            controller.show_frame(StudyPage)
            # -------------------------
            # ----
        cancelButton = ttk.Button(self, text="Return to StudyPage", command=lambda: returnHomeButton_Method())
        cancelButton.grid(row=8, column=2, padx=(10,0), pady=10, sticky="W")
# ==================================================
# ==================================================
# ==================================================
# ==================================================
class KeyLoggerPage(ttk.Frame):
    # This is just for show.
    # If you go to this page it simply prints your keys that you press.
    # This does nothing, but I want to use it on the other pages
    #       and am just testing it out.
    # The right arrow and down arrow are permanently tied to the Study Page bind functions,
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

        currentErrorlabel = ttk.Label(self, text="The Right Arrow and Down Arrow, seem to be "
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
def update_StudyPage(app):
    #StudyPage.studyNumber = global_SearchReturnPosition
    #StudyPage.listPositionLabel_textVar.set(("Position:" + str(StudyPage.studyNumber + 1)))
    #print("xxx " + str(StudyPage.studyNumber))
    '''
    This works, it runs every second and repeats this method.
    I can access the global position, which is changed after a SearchPage search
        and this picks that up.

    The point is to change the position label on the StudyPage
        I search on the search page, and set a return position.
        That return position works, if I hit all traits the correct spot pops up
            but without doing anything, the position label still says the last position that was viewed.

    Create a global StringVar()
    Create a global method
    '''
    global global_SearchReturnPosition
    #global_SearchReturnPosition += 5
    print("global_SearchReturnPosition = " + str(global_SearchReturnPosition))
    print("Every 1 Seconds")
    app.after(1000, lambda: update_StudyPage(app))
update_StudyPage(app)


app.mainloop()
# ==================================================
#   MAIN    MAIN    MAIN    MAIN    MAIN    MAIN
# ==================================================
