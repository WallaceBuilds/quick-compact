# QuickCompact 0.9.1 Linux-Friendly
# September 13, 2018
# Managed by WallaceBuilds
# Please refer to the README for general information.

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
        start = time.process_time()
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
            imageNames.insert(i,"e93z18k31203106129ps85z549w6477ra")
        self.imageNames = imageNames
        end = time.process_time()
        speed = end - start
        print("\nTotal Size =", self.totalSize,"B")
        print(speed*1000, "milliseconds")
        self.throughput = self.totalSize/speed
        print("Estimated Throughput:",self.throughput/1000000,"MB/s")
        
        self.start_time()
    
    def start_time(self):
        self.start = time.process_time()
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
        esti_print = ("Estimated to finish in %.3f" %estimate + " seconds")
        myGUI.new_labela(esti_print)
        print(esti_print)
        self.compress_scale()
        
    def compress_scale(self):
        for self.x in range(len(self.imageNames)):
            root.update()
            if myGUI.runStater("pass") == False:
                current_time = (time.process_time() - self.start)
                print("[ %.3f ]"% current_time, self.imageNames[self.x],"JOB STOPPED.")
                break
            if (self.imageNames[self.x] == "e93z18k31203106129ps85z549w6477ra"):
                continue
            try:
                self.source = Image.open(self.imageNames[self.x])
                w = self.source.size[0]
                self.scaleW = int(w/self.ratio)
                h = self.source.size[1]
                self.scaleH = int(h/self.ratio)
            except:
                current_time = (time.process_time() - self.start)
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
            self.source = self.source.resize((self.scaleW,self.scaleH),Image.NORMAL)
    
        self.compress_completer()
        
    def compress_completer(self):
        try:
            currentImage = self.imageNames[self.x].replace(self.sourceDir,"")
            self.source.save(self.destDir + currentImage,optimize=self.opti,quality=self.resultQ)
            current_time = (time.process_time() - self.start)
            print("[ %.3f ]"% current_time, currentImage,"Completed")
        except:
            current_time = (time.process_time() - self.start)
            print("[ %.3f ]"% current_time, self.imageNames[self.x],"Could not compress.")
        
    def finish_time(self):
        if myGUI.runStater("pass") == False:
            myGUI.new_labela("Job stopped.")
        else:
            self.end = time.process_time() - self.start
            finish = ("Finished in %.3f" %self.end + " seconds.")
            myGUI.new_labela(finish)
            print(finish)
            
class qcGUI:
    def __init__(self, master):
        self.master = master
        master.title("QuickCompact 0.9.1 (Pre-Alpha)")
        master.geometry("800x420")
        self.master.iconbitmap('@QuickCompactBox.xbm')
        root.resizable(0,0)
        # Warning Label
        self.label0 = Label(master, text="",font="Sans 12")
        self.label0.place(x=200, y=220)
        # Source Directory label, text field, and browse button
        self.label1 = Label(master, text="Source Directory",font="Sans 12")
        self.label1.place(x=0,y=15)
        self.textbox1 = StringVar()
        self.textbox1 = Entry(master, font = "Sans 12", width=60)
        self.textbox1.place(x=200,y=15)
        self.browse_button1 = Button(text="...", command=self.browse1)
        self.browse_button1.place(x=765,y=12)
        # Destination Directory label, text field, and browse button
        self.label2 = Label(master, text="Destination Directory",font="Sans 12")
        self.label2.place(x=0,y=60)
        self.textbox2 = StringVar()
        self.textbox2 = Entry(master, font="Sans 12", width=60)
        self.textbox2.place(x=200,y=60)
        self.browse_button2 = Button(text="...", command=self.browse2)
        self.browse_button2.place(x=765,y=57)
        # JPG Quality label, label bindings, and slider
        self.label3 = Label(master, text="JPG Quality (1-100)",font="Sans 12")
        self.label3.place(x=0,y=120)
        self.label3.bind("<Enter>", self.l3enter)
        self.label3.bind("<Leave>", self.leave)
        self.slidera = Scale(master, from_=1, to=100, orient=HORIZONTAL,font="Sans 12")
        self.slidera.set(100)
        self.slidera.place(x=200,y=105)
        # Optimize boolean, checkbutton, checkbutton bindings
        self.opti = False
        self.opti_button = Checkbutton(master, text="Optimize",font="Sans 12",command=self.opti_switch)
        self.opti_button.place(x=650,y=120)
        self.opti_button.bind("<Enter>", self.opti_enter)
        self.opti_button.bind("<Leave>", self.leave)
        # Compress ratio label, label bindings, and slider
        self.label7 = Label(master, text="Resize Factor",font="Sans 12")
        self.label7.place(x=0, y=165)
        self.label7.bind("<Enter>", self.l7enter)
        self.label7.bind("<Leave>", self.leave)
        self.sliderb = Scale(master, from_=16, to=1, orient=HORIZONTAL,font="Sans 12")
        self.sliderb.set(4)
        self.sliderb.place(x=200,y=150)
        
        self.aa = False
        self.aa_button = Checkbutton(master, text="Antialias",font="Sans 12",command=self.aa_switch)
        self.aa_button.place(x=650,y=165)
        self.aa_button.bind("<Enter>", self.aa_enter)
        self.aa_button.bind("<Leave>", self.leave)
        # Compress button, activates initialize method
        self.compress_button = Button(master, text="Compress", font="Sans 12",command=self.initialize)
        self.compress_button.place(x=25,y=220)
        # Cancel button, activates end method
        self.cancel_button = Button(master, text="Cancel", font="Sans 12", command=self.enda)
        self.cancel_button.place(x=690,y=220)
        # QuickCompact logo image
        image1 = PhotoImage(file = 'QuickCompactlogo.gif')
        self.label4 = Label(image = image1)
        self.label4.image = image1
        self.label4.place(x=193,y=265)
        # defines the compression method's current state
        self.runState =  False
        
    def opti_switch(self):
        if self.opti == True:
            self.opti = False
        else:
            self.opti = True
    
    def aa_switch(self):
        if self.aa == True:
            self.aa = False
        else:
            self.aa = True
            
    def l3enter(self, enter):
        self.new_labelb("The lower the number, the smaller the JPG file size. Sacrifices image quality.")
    
    def opti_enter(self, enter):
        self.new_labelb("Performs an extra pass to determine if any more space can be saved.")
        
    def aa_enter(self, enter):
        self.new_labelb("Provides a less pixelated image. Recommended for images with text.")
    
    def l7enter(self, enter):
        self.new_labelb("Configures how many times smaller each image will be upon compression.")
        
    def leave(self, leave):
        self.new_labelb("")
        
    def browse1(self):
        directory_name = filedialog.askdirectory()
        print(directory_name)
        if directory_name != "":
            self.textbox1.delete(0,END)
        self.textbox1.insert(0,directory_name)
    
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
        print(self.runState)
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
            
    def endb(self):
        self.master2.destroy()
    
    def new_labela(self, data):
        try:
            if self.label5 != "":
                self.label5.destroy()
            self.label5 = Label(text = data,font="Sans 12")
            self.label5.place(x=0,y=360)
        except:
            self.label5 = Label(text = data,font="Sans 12")
            self.label5.place(x=0,y=360)
        
    def new_labelb(self, data):
        try:
            if self.label6 != "":
                self.label6.destroy()
            self.label6 = Label(text = data,font="Sans 12")
            self.label6.place(x=0,y=390)
        except:
            self.label6 = Label(text = data,font="Sans 12")
            self.label6.place(x=0,y=390)
    
    def confirmation(self):
        self.master2 = Tk()
        self.master2.title("Confirmation")
        self.master2.geometry("280x140")
        self.master2.resizable(0,0)
        
        self.master2.iconbitmap('@QuickCompactBox.xbm')
        
        self.runStater(True)
        if self.source == self.dest:
            self.warning = Label(self.master2, text = "Original images will be overwritten.", font = "Sans 12")
            self.warning.place(x=5,y=5)
        self.label8 = Label(self.master2, text = "Are you sure?", font = "Sans 12")
        self.label8.place(x=75,y=50)
        
        self.yes = Button(self.master2, text = "Confirm", font = "Sans 12", command=self.confirm)
        self.yes.place(x=15,y=95)
        
        self.no = Button(self.master2, text = "Cancel", font = "Sans 12", command=self.endb)
        self.no.place(x=180,y=95)
        
    def confirm(self):
        self.master2.destroy()
        try:
            if self.label0 != "":
                self.label0.destroy()
                root.update()
        finally:
            c = compress()
            c.attributes(self.quality,self.opti,self.ratio,self.aa)
            c.sorter(self.source,self.dest)
    
root = Tk()
myGUI = qcGUI(root)
root.mainloop()
