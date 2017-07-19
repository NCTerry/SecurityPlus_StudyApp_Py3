NCTerry Security Plus Study App

# Current Py file Directory address
# /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/Security+_StudyApp.py
# =================
# Current txt file Directory address
# /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/SecurityPlus_StudyFile.txt
# =================

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

Example of File :
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


    Note: This is our primary page container format/configuration page for all pages.
        Set geometry, title, image(not working though)

        We have a menu that is not being used at the momemnt.

        We have a popup message coming from the menu selection, just for show at the moment.

# ==================================================
class inputObject:
    # We should store a user input as a class object with parts
    # We initially use this in the readTxtFile() method
    # We insert into the txt file, just line by line of user input
    # We read out the file and once we hit a   '###'   we know that the next 6 lines are object attributes.
    #    Take those 6 lines and insert into an object of this class to match the input format.
    # Then take that object and insert into the global list.

    # This is built into class objects so we can easily keep track of how many we have every time we add 1

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
# ==================================================
def appendToTxtFile(acronym, title, port, protocol, TCP_UDP, definition): #animate function with  'i' for interval
    '''
    This method appends to  our text file
    This is called on the   AddToFilePage
        Called for user to add a full object to the file.
    '''

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
            Full rewrite is not efficient, but helps to remain consistent on a small scale like this.

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

# ==================================================
class ConfirmAddPage(ttk.Frame):
    # Simple confirmation page
    # Lets user agree that they will be changing the file
    # If user agrees, it will take them to the change page

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

