# Current Py file Directory address
# /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/Security+_StudyApp.py
# =================
# Current txt file Directory address
# /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/SecurityPlus_StudyFile.txt
# =================

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
Definition:   The Domain Name System (DNS) is a hierarchical decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities. Most prominently, it translates more readily memorized domain names to the numerical IP addresses needed for locating and identifying computer services and devices with the underlying network protocols. By providing a worldwide, distributed directory service, the Domain Name System is an essential component of the functionality on the Internet, that has been in use since 1985.The Domain Name System delegates the responsibility of assigning domain names and mapping those names to Internet resources by designating authoritative name servers for each domain. Network administrators may delegate authority over sub-domains of their allocated name space to other name servers. This mechanism provides distributed and fault tolerant service and was designed to avoid a single large central database.The Domain Name System also specifies the technical functionality of the database service that is at its core. It defines the DNS protocol, a detailed specification of the data structures and data communication exchanges used in the DNS, as part of the Internet Protocol Suite. Historically, other directory services preceding DNS were not scalable to large or global directories as they were originally based on text files, prominently the HOSTS.TXT resolver.The Internet maintains two principal namespaces, the domain name hierarchy[1] and the Internet Protocol (IP) address spaces.[2] The Domain Name System maintains the domain name hierarchy and provides translation services between it and the address spaces. Internet name servers and a communication protocol implement the Domain Name System.[3] A DNS name server is a server that stores the DNS records for a domain; a DNS name server responds with answers to queries against its database.The most common types of records stored in the DNS database are for Start of Authority (SOA), IP addresses (A and AAAA), SMTP mail exchangers (MX), name servers (NS), pointers for reverse DNS lookups (PTR), and domain name aliases (CNAME). Although not intended to be a general purpose database, DNS can store records for other types of data for either automatic lookups, such as DNSSEC records, or for human queries such as responsible person (RP) records. As a general purpose database, the DNS has also been used in combating unsolicited email (spam) by storing a real-time blackhole list. The DNS database is traditionally stored in a structured zone file.)]
# ==================================================

'''
from tkinter import *
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



style.use("ggplot")
LARGE_FONT = ("Verdana", 18)  # Base font that we want to use and will call
NORM_FONT = ("Verdana", 12)  # Base font that we want to use and will call
SMALL_FONT = ("Verdana", 10)  # Base font that we want to use and will call
# This is our global list. While the program is running this will be used with our study data
global global_fileData
global_fileData = []

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
     __init__ implies that this will be run automatically if the class is called.
         other def methods will not run automatically.
            args = arguments = open ended, you can pass whatever you want through
            kwargs = key-word arguments, basically dictionaries.
     '''
    def __init__(self, *args, **kwargs):
        # Now initialize tkinter also.
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.title(self, "NCT's Security+ Study App")
        tk.Tk.geometry(self, "600x1000")
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

        # =================
        # =================
        # =================
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
        for F in (StartPage, ConfirmAddPage, AddToFilePage, StudyPage, BTCePage):
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
# We should store a user input as a class object with parts
class inputObject:
    # We have this in the readTxtFile() method
    # We insert into the txt file, just line by line of user input
    # We read out the file and insert into an object of this class to match the input format.

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
def animate(i):
    # ==================================================
    # This is the new animate function which pulls live trading data from btc-e.com for our plot
    # This is the direct link, but we want to add a parameter, how many trades.
    #       The site limit is 2000 for us to capture
    #       To add a parameter use:     ' ?parameterName=parameterValue '
    # datalink1 = "https://btc-e.com/api/3/trades/btc_usd"

    # animate function with  'i' for interval
    # Note: The request is giving us a pseudo error. It works, but pycharm is overreacting.

    dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
    data = urllib.request.urlopen(dataLink)
    data = data.readline().decode("utf-8")
    data = json.loads(data)

    data = data["btc_usd"]  # Refers to the whole data set read in (seen below)
    # Now use pandas to organize the 2000 rows of data we are bringing in.
    data = pd.DataFrame(data)

    # Separating our json data being pulled in (seen below).
    buys1 = data[(data["type"] == "bid")]
    # Now need to convert the unix timestamp. matplotlib does not recognize this.
    buys1["datestamp"] = np.array(buys1["timestamp"]).astype("datetime64[s]")
    buyDates1 = (buys1["datestamp"]).tolist()

    # Separating our json data being pulled in (seen below).
    sells1 = data[(data["type"] == "ask")]
    # Now need to convert the unix timestamp. matplotlib does not recognize this.
    sells1["datestamp"] = np.array(sells1["timestamp"]).astype("datetime64[s]")
    sellDates1 = (sells1["datestamp"]).tolist()

    a.clear()
    # Plot the data points, and turn them into colored-labeled lines.
    a.plot_date(buyDates1, buys1["price"], "g", label="buys")
    a.plot_date(sellDates1, sells1["price"], "#00A3E0", label="sells")
    # Legend lets us specifically place our line labels in the top left
    # Default they are put on the graph and will be covered up if the lines go over them.
    a.legend(bbox_to_anchor=(0,1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
    # Plot title with a live update of the last price from the most recent data set.
    title = "BTC-e BTCUSD Prices\nLast Price: " + str(data["price"][1999])
    a.set_title(title)
    # -------------------------------------------------------
    # ==================================================
    # ==================================================
    '''
    -------------------------------------------------------
        THESE ARE REAL DAILY BIDS 12:16PM 7/7/2017
        THIS IS THE JSON info that we will be pulling from.
        It has a unix timestamp
    -------------------------------------------------------
        {"btc_usd":[{"type":"ask","price":2474.869,"amount":0.15496925,"tid":110941553,"timestamp":1499451300},
        {"type":"ask","price":2475.259,"amount":0.09,"tid":110941552,"timestamp":1499451300},
        {"type":"ask","price":2475.261,"amount":0.00527802,"tid":110941551,"timestamp":1499451300},
        {"type":"ask","price":2475.219,"amount":0.38974944,"tid":110941540,"timestamp":1499451285},
        {"type":"bid","price":2478.55,"amount":0.01653934,"tid":110941537,"timestamp":1499451283},
    -------------------------------------------------------
    '''
# ==================================================
# ==================================================
# ==================================================
# Use the hashtag as the marker of a new input.
def readTxtFile(): #animate function with  'i' for interval
#       This is called on the   AddToFilePage

    dataList1 = [line.rstrip('\n') for line in open('SecurityPlus_StudyFile.txt')]

    # =======================
    # We have put the txt file line by line into datalist1 separated at \n
    #       but this is still all one piece.
    print("The for datalist1 in readTxtFile()")
    # Create a true list
    trueList = []
    print(dataList1)
    '''
    xxx CHANGED CHANGED CHANGED XXX
    [   '###',
        'A__DNS',
        'T__Domain Name System',
        'P__443',
        'D__The internets system for converting alphabetic names into numeric IP addressses.',
        '###',
        'A__Nate',
        'T__Charles',
        'P__31',
        'D__Terry'  ]
    '''
    # =======================
    print("\nThat was the datalist as a variable, now the for loop: ")
    for x in dataList1:
        print(x)
        if x == "###":
            print("----------------")

    # =======================
    print("\n Check the y range")
    # Clear the global list, as we will be appending to it the entire txt file.
    global_fileData[:] = []
    for y in range(0, len(dataList1)):
        print(dataList1[y])
        if dataList1[y] == "###":
            studyObject = inputObject(dataList1[y+1], dataList1[y+2], dataList1[y+3], dataList1[y+4], dataList1[y+5], dataList1[y+6])
            trueList.append(studyObject)
            # Don't need the file list
            # Will call the global file later, but we have to run the read file to get it up to date
            global_fileData.append(studyObject)
    '''
            Check the y range
        ###
        Acronym:      DNS
        Title:        Domain Name System
        Port:         443
        Definition:   The internets system of converting alphabetic names into numeric IP addressses

    '''
    # =======================
    # How we are printing the object list.
    # Object format is created and returned based on the ___repr___ format from the inputObject class.
    print("\nTrueList = ", trueList)

    '''
        TrueList =  [
        InputObject(
        Acronym:      DNS,
        Title:        Domain Name System,
        Port:         443,
        Definition:   The internets system of converting alphabetic names into numeric IP addressses)]
    '''
# ==================================================
# ==================================================
# ==================================================
# This method appends to  our text file
#       This is called on the   AddToFilePage
def writeToTxtFile(acronym, title, port, protocol, TCP_UDP, definition): #animate function with  'i' for interval
    writeData1 = open("SecurityPlus_StudyFile.txt", "a")

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
    writeData1.write("Acronym:      " + acronym + '\n')
    writeData1.write("Title:        " + title + '\n')
    writeData1.write("Port:         " + port + "\n")
    writeData1.write("Protocol:     " + protocol + "\n")
    writeData1.write("TCP/UDP:      " + TCP_UDP + "\n")
    writeData1.write("Definition:   " + definition + '\n')
    writeData1.close()


    studyObject2 = inputObject(acronym, title, port, protocol, TCP_UDP, definition)
    # Will call the global file later, but we have to run the read file to get it up to date
    global_fileData.append(studyObject2)

    '''
    # We have just written to the file, we also need to now update our global study list.
    dataList2 = [line.rstrip('\n') for line in open('SecurityPlus_StudyFile.txt')]

    # =======================
    print("\n Check the y range")
    for y in range(0, len(dataList2)):
        print(dataList2[y])
        if dataList2[y] == "###":
            studyObject = inputObject(dataList2[y + 1], dataList2[y + 2], dataList2[y + 3], dataList2[y + 4])
            # Will call the global file later, but we have to run the read file to get it up to date
            global_fileData.append(studyObject)
            '''
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
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # ----------------------------
        # ttk will give us a good looking button
        startPage_addToStudyFilePageButton = ttk.Button(self, text="Add to Study File Page",
                                                 command=lambda: controller.show_frame(ConfirmAddPage))
        startPage_addToStudyFilePageButton.pack()

        # ----------------------------
        # ttk will give us a good looking button
        startPage_GOToStudyPageButton = ttk.Button(self, text="Study Page",
                                                 command=lambda: controller.show_frame(StudyPage))
        startPage_GOToStudyPageButton.pack()

        # ----------------------------
        # ttk will give us a good looking button
        startPage_CloseButton = ttk.Button(self, text="Close Program",
                                           command=quit)
        startPage_CloseButton.pack()
# ==================================================
# ==================================================
# ==================================================
# ==================================================
class ConfirmAddPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="The Study File", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # ----------------------------
        askButton = ttk.Label(self, text="""Do you want to add study info to your txt file?
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
            #
            DNS
            Domain Name System
            The Internet's system for converting alphabetic names into numeric IP addresses.
    '''

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Add to Study File", font=LARGE_FONT)
        # 1st row, 2nd column, pushto right 40%
        label.grid(row=0, column=1, padx=40)
        # ------------------------
        warninglabel = ttk.Label(self, text="Note: If you leave a spot blank, we will auto-include 'N/A'",
                                 font=SMALL_FONT)
        # 1st row, 2nd column, pushto right 40%
        warninglabel.grid(row=1, column=1, padx=40)
        # ------------------------
        spacerLabel = ttk.Label(self, text="", font=LARGE_FONT)
        # 1st row, 2nd column, pushto right 40%
        spacerLabel.grid(row=2, column=0, padx=20)
        # ------------------------
        # ------------------------
        # --------------------------------------------------------------
        acro_Label = ttk.Label(self, text="Add Acronym: ", font=NORM_FONT)
        acro_Label.grid(row=4, column=0, sticky="W", padx=20)
        # -----
        acro_input = ttk.Entry(self, width=40)
        acro_input.grid(row=4, column=1, sticky="W")
        # -----
        acro_Example = ttk.Label(self, text="Ex: DNS ", font=NORM_FONT)
        acro_Example.grid(row=5, column=1, sticky="WE", padx=20, pady=(0,10))
        # --------------------------------------------------------------
        title_Label = ttk.Label(self, text="Add Title: ", font=NORM_FONT)
        title_Label.grid(row=6, column=0, sticky="W", padx=20)
        # -----
        title_input = ttk.Entry(self, width=40)
        title_input.grid(row=6, column=1, sticky="W")
        # -----
        title_Example = ttk.Label(self, text="Ex: Domain Name System ", font=NORM_FONT)
        title_Example.grid(row=7, column=1, sticky="WE", padx=20, pady=(0,10))
        # --------------------------------------------------------------
        port_Label = ttk.Label(self, text="Related Port#: ", font=NORM_FONT)
        port_Label.grid(row=8, column=0, sticky="W", padx=20)
        # -----
        port_input = ttk.Entry(self, width=40)
        port_input.grid(row=8, column=1, sticky="W")
        # -----
        port_Example = ttk.Label(self, text="Ex: 443 ", font=NORM_FONT)
        port_Example.grid(row=9, column=1, sticky="WE", padx=20, pady=(0,10))
        # --------------------------------------------------------------
        protocol_Label = ttk.Label(self, text="Add Protocol: ", font=NORM_FONT)
        protocol_Label.grid(row=10, column=0, sticky="W", padx=20)
        # -----
        protocol_input = ttk.Entry(self, width=40)
        protocol_input.grid(row=10, column=1, sticky="W")
        # -----
        protocol_Example = ttk.Label(self, text="Ex: Secure Shell (SSH) (RFC 4250-4256) ", font=NORM_FONT)
        protocol_Example.grid(row=11, column=1, sticky="WE", padx=20, pady=(0,10))
        # --------------------------------------------------------------
        tcp_udp_Label = ttk.Label(self, text="TCP and/or UDP", font=NORM_FONT)
        tcp_udp_Label.grid(row=12, column=0, sticky="W", padx=20)
        # -----
        tcp_udp_input = ttk.Entry(self, width=40)
        tcp_udp_input.grid(row=12, column=1, sticky="W")
        # -----
        tcp_udp_Example = ttk.Label(self, text="Ex: TCP ", font=NORM_FONT)
        tcp_udp_Example.grid(row=13, column=1, sticky="WE", padx=20, pady=(0,10))
        # --------------------------------------------------------------
        def_Label = ttk.Label(self, text="Add Definition: ", font=NORM_FONT)
        def_Label.grid(row=14, column=0, sticky="W", padx=20)
        # -----
        def_input = ttk.Entry(self, width=40)
        def_input.grid(row=14, column=1, sticky="W")
        # -----
        acro_Example = ttk.Label(self, text="    Ex: The Internet's system for converting"
                                            "\n    alphabetic names into numeric IP addresses."
                                            "\n    For example, when a Web address (URL) is "
                                            "\n    typed into a browser, DNS servers return the "
                                            "\n    IP address of the Web server associated with "
                                            "\n    that name. In this made-up example, the DNS "
                                            "\n    converts the URL www.company.com into the IP "
                                            "\n    address 204.0.8.51. Without DNS, you would have "
                                            "\n    to type the series of four numbers and dots into "
                                            "\n    your browser to retrieve the website, which you "
                                            "\n    actually can do. ", font=NORM_FONT)
        acro_Example.grid(row=15, column=1, pady=(0,10))
        # --------------------------------------------------------------



        # ------------------------
        writeFileButton = ttk.Button(self, text="Write Text Fle",
                                        command=lambda: writeToTxtFile(acro_input.get(), title_input.get(),
                                                                       port_input.get(), protocol_input.get(),
                                                                       tcp_udp_input.get(), def_input.get()))
        writeFileButton.grid(row=16, column=1)

        # ------------------------
        readFileButton = ttk.Button(self, text="Read Text Fle",
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
class StudyPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Study Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # Auto get the object list of our study txt file.
        rtnList = []
        def printrtn():
            rtnList = readTxtFile()
            print("\nGlobal File Data = ")
            print(global_fileData)
            print("\nGlobal File Data[3] =", global_fileData[3]) # works
            '''
            Prints out the 4th study object in the global list
            '''
            #print("\nrtnList from StudyPage: ", rtnList)

        # ----------------------------
        # Will print out the file to the page
        printOutFile_StudyPageButton = ttk.Button(self, text="Print File to Page",
                                                 command=lambda: controller.show_frame(ConfirmAddPage))
        printOutFile_StudyPageButton.pack()

        # ----------------------------
        # Button to go back home
        returHomeButtonf = ttk.Button(self, text="Return to Home Page",
                             command=lambda: controller.show_frame(StartPage))
        returHomeButtonf.pack()

        # ----------------------------
        fileButton = ttk.Button(self, text="Print File", command=printrtn)
        fileButton.pack(padx=10, pady=10)

        # ----------------------------
        fileLabel = ttk.Label(self, text="List below", font=SMALL_FONT)
        fileLabel.pack(padx=10, pady=10)

        # ----------------------------
        fileLabel = ttk.Label(self, text="List below", font=SMALL_FONT)
        fileLabel.pack(padx=10, pady=10)
# ==================================================
# ==================================================
# ==================================================
# ==================================================
class BTCePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        # ----------------------------
        label = ttk.Label(self, text="BitCoin Trading Page"
                                     "\nThis is on live update based on site data.", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # ----------------------------
        # ttk will give us a good looking button
        pageTwo_homeButton = ttk.Button(self, text="Back to Home",
                                        command=lambda: controller.show_frame(StartPage))
        pageTwo_homeButton.pack()

        # ----------------------------
        # ----------------------------
        # ----------------------------
        # This set is needed for our plot.
        # Place this on the page you want the user to view the live plot
        # This is what is communicating with the main object call and the animate method
        canvas1 = FigureCanvasTkAgg(f, self)
        canvas1.show()
        canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # We have a graph with the above but we want a Nav Bar
        # Navigation bar
        toolbar1 = NavigationToolbar2TkAgg(canvas1, self)
        toolbar1.update()
        canvas1._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # Note we just added the standard tool bar to the graph but I
        #   i could not see it at first. I had to increase my y-height on page

        # ----------------------------
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

# using our f-object from the top, animate-function, and 5000 milliseconds
# This means we will update our data every 5 seconds.
# This is what plotted to the graph page in file 6
ani1 = animation.FuncAnimation(f, animate, interval=5000)

app.mainloop()
# ==================================================
#   MAIN    MAIN    MAIN    MAIN    MAIN    MAIN
# ==================================================