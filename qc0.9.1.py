# QuickCompact 0.9.1 (Pre-Alpha)
# September 16, 2018
# Managed by WallaceBuilds
# Please refer to the README for general information

from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk as itk
import os
import time
import imghdr

class compress:
    
    def attributes(self,quality,optimize,ratio,antialias):
        self.resultQ = quality
        self.opti = optimize
        self.ratio = ratio
        self.antialias = antialias
    
    def sorter(self,source,dest):
        # Source directory for files to be compressed
        self.sourceDir = source
        self.sourceDir += "/"
        # Destination directory for completed compressions
    
        self.destDir = dest
        self.destDir += "/"
        # declares the general list of files to be compressed
        imageNames = []
        # Scans the source directory for all files, including non-image files
        for path, subdirs, files in os.walk(self.sourceDir):
            for name in files:
                if path == self.sourceDir:
                    imageNames.append(self.sourceDir + name)
        
        self.checker(imageNames)
        
    def checker(self,imageNames):
        start = time.perf_counter()
        self.totalSize = 0
        nonImage = []
        for i in range(len(imageNames)):
            size = os.path.getsize(imageNames[i])
            ext = imghdr.what(imageNames[i])
            print(imageNames[i])
            print(ext)
            print(size,"B")
            if size < 1000 or ext == None:
                nonImage.append(i)
            else:
                self.totalSize += size
        for i in nonImage:
            imageNames.pop(i)
            imageNames.insert(i,"")
        self.imageNames = imageNames
        end = time.perf_counter()
        speed = end - start
        print("\nTotal Size =", self.totalSize,"B")
        print(speed*1000, "milliseconds")
        self.throughput = self.totalSize/speed
        print("Estimated Throughput:",self.throughput/1000000,"MB/s")
        
        self.start_time()
    
    def start_time(self):
        self.start = time.perf_counter()
        self.estimator()
        
    def estimator(self):
        estimate = 0
        if self.opti == True:
            if self.antialias == True:
                estimate = self.totalSize / (self.throughput / 600)
            else:
                estimate = self.totalSize / (self.throughput / 450)
        else:
            if self.antialias == True:
                estimate = self.totalSize / (self.throughput / 280)
            else:
                estimate = self.totalSize / (self.throughput / 220)
        estimate = estimate / (self.ratio/2.5)
        esti_print = ("Estimated to finish in %.3f" %estimate + " seconds")
        qcGUI.new_labela(esti_print)
        print(esti_print)
        self.compress_scale()
        
    def compress_scale(self):
        for self.x in range(len(self.imageNames)):
            root.update()
            if qcGUI.runStater("pass") == False:
                current_time = (time.perf_counter() - self.start)
                print("[ %.3f ]"% current_time, self.imageNames[self.x],"JOB STOPPED.")
                break
            if (self.imageNames[self.x] == ""):
                continue
            try:
                self.source = Image.open(self.imageNames[self.x])
                w = self.source.size[0]
                self.scaleW = int(w/self.ratio)
                h = self.source.size[1]
                self.scaleH = int(h/self.ratio)
            except:
                current_time = (time.perf_counter() - self.start)
                print("[ %.3f ]"% current_time, self.imageNames[self.x],"Could not compress.")
                continue
            if self.scaleW < 1 or self.scaleH < 1:
                print(str(self.x+1)+". " + self.imageNames[self.x]+": File too small. Removed from job.")  
                continue
            self.compress_main()
        
        self.finish_time()
        
    def compress_main(self):
        if self.antialias == True:
            self.source = self.source.resize((self.scaleW,self.scaleH),Image.ANTIALIAS)
        else:
            self.source = self.source.resize((self.scaleW,self.scaleH),Image.BILINEAR)
    
        self.compress_completer()
        
    def compress_completer(self):
        try:
            currentImage = self.imageNames[self.x].replace(self.sourceDir,"")
            self.source.save(self.destDir + currentImage,optimize=self.opti,quality=self.resultQ)
            current_time = (time.perf_counter() - self.start)
            print("[ %.3f ]"% current_time, currentImage,"Completed")
        except:
            current_time = (time.perf_counter() - self.start)
            print("[ %.3f ]"% current_time, self.imageNames[self.x],"Could not compress.")
        
    def finish_time(self):
        if qcGUI.runStater("pass") == False:
            qcGUI.new_labela("Job stopped.")
        else:
            self.end = time.perf_counter() - self.start
            finish = ("Finished in %.3f" %self.end + " seconds.")
            qcGUI.new_labela(finish)
            print(finish)


class qcGUI:
    def __init__(self, master):
        self.master = master
        master.title("QuickCompact 0.9.1 (Pre-Alpha)")
        master.geometry("480x300")
        # Places the icon at the top-left corner of the window pane
        root.iconbitmap('QuickCompactBox.ico')
        root.resizable(0,0)
        # Warning Label
        self.label0 = Label(master, text="")
        self.label0.place(x=91, y=157)
        # Source Directory label, text field, and browse button
        self.label1 = Label(master, text="Source Directory")
        self.label1.place(x=15,y=15)
        self.label1.bind("<Enter>", self.l1enter)
        self.label1.bind("<Leave>", self.leave)
        self.textbox1 = StringVar()
        self.textbox1 = Entry(master, width=50)
        self.textbox1.place(x=140,y=15)
        self.browse_button1 = Button(text="...", command=self.browse1)
        self.browse_button1.place(x=450,y=10)
        # Destination Directory label, text field, and browse button
        self.label2 = Label(master, text="Destination Directory")
        self.label2.place(x=15,y=45)
        self.label2.bind("<Enter>", self.l2enter)
        self.label2.bind("<Leave>", self.leave)
        self.textbox2 = StringVar()
        self.textbox2 = Entry(master, width=50)
        self.textbox2.place(x=140,y=45)
        self.browse_button2 = Button(text="...", command=self.browse2)
        self.browse_button2.place(x=450,y=40)
        # JPG Quality label, label bindings, slider, and default setting
        self.label3 = Label(master, text="JPG Quality (1-100)")
        self.label3.place(x=15,y=80)
        self.label3.bind("<Enter>", self.l3enter)
        self.label3.bind("<Leave>", self.leave)
        self.slidera = Scale(master, from_=1, to=100, orient=HORIZONTAL)
        self.slidera.set(100)
        self.slidera.place(x=140,y=65)
        # Optimize state, checkbutton, and bindings
        self.opti = False
        self.opti_button = Checkbutton(master, text="Optimize",command=self.opti_switch)
        self.opti_button.place(x=290,y=75)
        self.opti_button.bind("<Enter>", self.opti_enter)
        self.opti_button.bind("<Leave>", self.leave)
        # Antialias state, checkbutton, and bindings
        self.aa = False
        self.aa_button = Checkbutton(master, text="Antialias",command=self.aa_switch)
        self.aa_button.place(x=290,y=115)
        self.aa_button.bind("<Enter>", self.aa_enter)
        self.aa_button.bind("<Leave>", self.leave)
        # Resize factor label, label bindings, slider, and default setting
        self.label7 = Label(master, text="Resize Factor")
        self.label7.place(x=15, y=120)
        self.label7.bind("<Enter>", self.l7enter)
        self.label7.bind("<Leave>", self.leave)
        self.sliderb = Scale(master, from_=16, to=1, orient=HORIZONTAL)
        self.sliderb.set(4)
        self.sliderb.place(x=140,y=105)
        # Compress button
        self.compress_button = Button(master, text="Compress", command=self.initialize)
        self.compress_button.place(x=25,y=155)
        # Cancel button
        self.cancel_button = Button(master, text="Cancel", command=self.enda)
        self.cancel_button.place(x=400,y=155)
        # QuickCompact logo placement
        image1 = PhotoImage(file = 'QuickCompactlogo.gif')
        self.label4 = Label(image = image1)
        self.label4.image = image1 # yes can keep a reference - good!
        self.label4.place(x=33,y=185)
        self.runState =  False
        # Initialize labels for new_labela and new_labelb
        self.label5 = Label()
        self.label6 = Label()
        # Initialize confirmation window state
        self.confirmState = False
    # Acts as a switch for the optimize checkbutton
    def opti_switch(self):
        if self.opti == True:
            self.opti = False
        else:
            self.opti = True
    # Acts as a switch for the antialias switch button
    def aa_switch(self):
        if self.aa == True:
            self.aa = False
        else:
            self.aa = True
    # Hover text for source directory label
    def l1enter(self, enter):
        self.new_labelb("The directory from which the program retrieves image files.")
    # Hover text for destination directory label    
    def l2enter(self, enter):
        self.new_labelb("The directory to which the program saves compressed image files.")
    # Hover text for image quality label    
    def l3enter(self, enter):
        self.new_labelb("The lower the number, the smaller the JPG file size. Sacrifices image quality.")
    # Hover text for optimize label
    def opti_enter(self, enter):
        self.new_labelb("Performs an extra pass to determine if any more space can be saved.")
    # Hover text for antialias label    
    def aa_enter(self, enter):
        self.new_labelb("Provides a less pixelated image. Recommended for images with text.")
    # Hover text for resize factor label
    def l7enter(self, enter):
        self.new_labelb("Configures how many times smaller each image will be upon compression.")
    # Clears hover text    
    def leave(self, leave):
        self.new_labelb("")
    # Browse and clear/fill function for source directory textbox    
    def browse1(self):
        directory_name = filedialog.askdirectory()
        print(directory_name)
        if directory_name != "":
            self.textbox1.delete(0,END)
        self.textbox1.insert(0,directory_name)
    # Browse and clear/fill function for destination directory textbox   
    def browse2(self):
        directory_name = filedialog.askdirectory()
        print(directory_name)
        if directory_name != "":
            self.textbox2.delete(0,END)
        self.textbox2.insert(0,directory_name)
    # Determines whether the compression script can continue
    def runStater(self,instance):
        if instance == True:
            self.runState = True
        elif instance == "pass":
            return self.runState
        else:
            self.runState = False
        return self.runState
    # Gets all necessary values ready for passing to the compression script
    def initialize(self):
        self.source = self.textbox1.get()
        self.dest = self.textbox2.get()
        self.quality = self.slidera.get()
        self.ratio = self.sliderb.get()
        if self.source == "" or self.dest == "":
            print("No entry.\n")
            self.label0.configure(text = "Please select a source directory and destination directory.",fg="red")
        else:
            if self.confirmState == True:
                print("Confirm window already opened.")
            else:
                self.confirmState = True
                self.confirmation()        
    # Ends the compression script, if running
    def enda(self):
        if self.runStater("pass") == False:
            print("Job not yet started.")
            self.new_labela("No job is currently active.")
            self.new_labelb("")
        else:
            print("Stopped.")
            self.runStater(False)
            self.new_labela("Job Stopped.")
            self.new_labelb("")
    # Ends the confirmation window, flips confirmState to False        
    def endb(self):
        self.master2.destroy()
        self.confirmState = False
    # Alters text in the first info label
    def new_labela(self, data):
        self.label5.configure(text = data)
        self.label5.place(x=0,y=260)
    # Alters text in the second info label
    def new_labelb(self, data):
        self.label6.configure(text = data)
        self.label6.place(x=0,y=280)
    # Builds the confirmation window
    def confirmation(self):
        self.master2 = Tk()
        self.master2.title("Confirmation")
        self.master2.geometry("200x120")
        self.master2.resizable(0,0)
        self.master2.iconbitmap('QuickCompactBox.ico')
        # Determines whether the source and destination directories are the same, warns user
        if self.source == self.dest:
            self.warning = Label(self.master2, text = "Original images will be overwritten.")
            self.warning.place(x=5,y=5)
        self.label8 = Label(self.master2, text = "Are you sure?")
        self.label8.place(x=60,y=25)
        # Confirm button
        self.yes = Button(self.master2, text = "Confirm", command=self.confirm)
        self.yes.place(x=15,y=80)
        # Cancel button
        self.no = Button(self.master2, text = "Cancel", command=self.endb)
        self.no.place(x=130,y=80)
        # Detects if the window is closed, so that the endb function can follow through
        self.master2.protocol("WM_DELETE_WINDOW", self.endb)
    # Passes the information needed to the compress class
    def confirm(self):
        self.master2.destroy()
        self.runStater(True)
        self.confirmState = False
        try:
            if self.label0 != "":
                self.label0.destroy()
                root.update()
        finally:
            c = compress()
            c.attributes(self.quality,self.opti,self.ratio,self.aa)
            c.sorter(self.source,self.dest)
            
# Initializes the GUI as a tkinter window
root = Tk()
qcGUI = qcGUI(root)
root.mainloop()