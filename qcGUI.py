# QuickCompact 0.9.0
# September 13, 2018
# Managed by WallaceBuilds
# Please refer to the README for general information.

from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk as itk
import os
import time

def compressor():
    # Source directory for files to be compressed
    sourceDir = input1
    print(input1)
    sourceDir += "/"
    # Destination directory for completed compressions
    print(input2)
    destDir = input2
    destDir += "/"
    # declares the general list of files to be compressed
    imageNames = []
    # Scans the source directory for all files, including non-image files
    for path, subdirs, files in os.walk(sourceDir):
        for name in files:
            if path == sourceDir:
                imageNames.append(name)
    ##### imageNames = next(os.walk(sourceDir))[2]
    if(len(imageNames) < 1):
        print("Source directory contains no files or does not exist. Job ended.")
        myGUI.new_labelb("Source directory contains no files or does not exist. Job ended.")
        myGUI.runStater(False)
    else:
         # Compression rate, default at 4
        compress = input4 # Warn user if set below rate of 1 (Time to finish will be severely increased)
         # Allows user to de-optimize if desired
        opti = optimize
         # Allows user to make all images the same size
        match = False # Warn that aspect ratio will be lost
         # User input W
        userW = 1000
         # User input H
        userH = 1000
         # Quality value, default at 80
        resultQ = input3
         # keeps quality equal to or less than 100
        if resultQ > 100:
            resultQ = 100
         # The list that tracks calculation times of individual compressions
        rates = []
         # Holds the ratio of size to speed
        ratio = []
         # time start
        start = 0
         # time end
        end = 0
         # holds failed compression count
        fail = 0
         # contains keywords for verifying the filetype
        verifier = [".jpg", "-large", "-LARGE", ".JPG",".png",".PNG",".gif",".GIF",".tiff",".TIFF",".BMP",".bmp"]
         # variable used for storing the average of previous times
        avg = 0.000
        discrep = 0.000000
         # counts the number of entries in the txt file
        cnt = 0
         # open the txt file
        file = open("speed_data.txt", "r")
         # iterate based on the number of lines
        for line in file:
             #try to convert to float
             try:
                 avg += float(line)
                 # otherwise don't enter the data
             except:
                 continue
             #count successful try
             cnt += 1
        
        # divide total by number of successful to get average
        try:
            avg = avg / cnt
        except:
            avg = avg
        # close the file
        file.close()
        #set up totalSize to hold size of images being processed
        totalSize = 0
        for i in range(len(imageNames)):
            #locate the file size
            size = os.path.getsize(sourceDir + imageNames[i])
            #add to totalSize
            totalSize += size
            # Now get the discrepancies in previous estimations
        cnt = 0
        file = open("discrepancies.txt", "r")
        # iterate based on the number of lines
        for line in file:
            #try to convert to float
            try:
                discrep += float(line)
            # otherwise don't enter the data
            except:
                continue
            #count successful try
            cnt += 1
        # divide total by number of successful to get average
        try:
            discrep = discrep / cnt
        except:
            discrep = discrep
        # close the file
        file.close()
        #This gives an estimated time to spend on this process based on the previous times.
        estimate_secs = (totalSize / (avg * 1000))
        
        if estimate_secs > 59:
            estimate_mins = int(estimate_secs/60)
            estimate_secs = estimate_secs%60
            if estimate_mins > 59:
                estimate_hrs = int(estimate_mins/60)
                estimate_mins = int(estimate_mins%60)
                estimate = "Time estimated to completion: " + "%d hour(s)," % estimate_hrs + "%d minute(s)," % estimate_mins + "%.3f seconds." % estimate_secs
            else:
                estimate ="Time estimated to completion: " + "%d minute(s)," % estimate_mins + "%.3f seconds." % estimate_secs
        else:
            estimate = "Time estimated to completion: " + " %.3f seconds." % estimate_secs
            
        line = (estimate)
        print(line)
        myGUI.new_labela(line)
        root.update()
        
    while (myGUI.runStater("pass") == True):    
        for i in range(len(imageNames)):
            if myGUI.runStater("pass") == False:
                break
            root.update()
            # Keeps the maximum number of pixels high so that it doesn't throw a DOS error.
            Image.MAX_IMAGE_PIXELS = 1000000000000
        
            start = time.clock()
            chk = 0
            # checking with verifier list
            for j in range(len(verifier)):
                if verifier[j] not in imageNames[i]:
                    continue
                else:
                    chk += 1
            # removing unwanted filetypes
            if chk == 0 or chk > 1:
                fail += 1
                print(str(i+1)+". "+imageNames[i]+": File not recognized. Removed from job.")
                end = time.clock()
                rates.append(end - start)
                print("Time used:", rates[i],  "seconds \n")
                continue
            # makes a copy of the original file
            size = os.path.getsize(sourceDir + imageNames[i])
            source = Image.open(sourceDir + imageNames[i])
        
            if match == True:
                scaleW = userW
                scaleH = userH
            else:
                # determines size of original file and calculates size of result
                w = source.size[0]
                scaleW = int(w/compress)
                h = source.size[1]
                scaleH = int(h/compress)
            
            if (time.clock() - start) > 3:
                print("This process is taking longer than usual.")
        
            print(str(i+1)+". "+imageNames[i]+": Size configured.")
            # Checking the size of the final compression, scrap if less than 1x1
            if scaleW < 1 or scaleH < 1:
                fail += 1
                print(str(i+1)+". "+imageNames[i]+": File too small. Removed from job.")
                end = time.clock()
                rates.append(end - start)
                print("Time used:", rates[i],  "seconds \n")
                continue
        
        # Compressing the file          
            source = source.resize((scaleW,scaleH),Image.ANTIALIAS)
        
            if (time.clock() - start) > 5:
                print("This process is taking longer than usual.")
                
            
            print(str(i+1)+". "+imageNames[i]+": Image resized.")
        
            # Optimization and quality settings
            source.save(destDir + imageNames[i] ,optimize=opti,quality=resultQ)
            print(str(i+1)+". "+imageNames[i]+": Copy saved.")
            end = time.clock()
            rates.append(end - start)
            print("Time used:", rates[i], "seconds")
            ratio.append(size / rates[i] / 1000)
            print("KB/s:", rates[i], "\n")
        
        if myGUI.runStater("pass") == False:
            break
        
        print("Job completed.")
        myGUI.new_labela("Job completed!")
        
        print(len(imageNames)-fail, "images successfully resized.")
        print(fail, "files removed from job.")
        # used for summation of calculation times
        secs = 0
        mins = 0
        hrs = 0
        for i in range(len(rates)):
            secs += rates[i]
        
        time_spent = ""
        if secs > 59:
            mins = int(secs/60)
            secs = secs%60
            if mins > 59:
                hrs = int(mins/60)
                mins = int(mins%60)
                time_spent = "Total time spent:", hrs, "hours,", mins, "minutes,", "%.3f seconds." % secs
            else:
                time_spent ="Total time spent:", mins, "minutes,", "%.3f seconds." % secs
        else:
            time_spent = "Total time spent:"+" %.3f seconds." % secs
            
        myGUI.new_labelb(time_spent)
    
        value = 0
        for i in range(len(ratio)):
            value += ratio[i]
        value = value / (len(ratio))
        #Write the new average of times into the txt file
        file = open("speed_data.txt", "a")
        file.write(str("%.3f") % value + "\n")
        file.close()
        discrep = (totalSize / avg) - value 
        file = open("discrepancies.txt", "a")
        file.write(str("%.6f") % discrep + "\n")
        # Output average KB/s
        print("Average KB/s:", value)
        myGUI.runStater(False)
    
class qcGUI:
    def __init__(self, master):
        self.master = master
        master.title("QuickCompact")
        master.geometry("480x300")
        
        root.iconbitmap('QuickCompactBox.ico')
        root.resizable(0,0)
        
        self.label0 = Label(master, text="")
        self.label0.place(x=91, y=157)
        
        self.label1 = Label(master, text="Source Directory")
        self.label1.place(x=25,y=15)
        
        self.textbox1 = StringVar()
        self.textbox1 = Entry(master, width=50)
        self.textbox1.place(x=140,y=15)
        self.browse_button1 = Button(text="...", command=self.browse1)
        self.browse_button1.place(x=450,y=10)
        
        self.label2 = Label(master, text="Destination Directory")
        self.label2.place(x=15,y=45)
        
        self.textbox2 = StringVar()
        self.textbox2 = Entry(master, width=50)
        self.textbox2.place(x=140,y=45)
        self.browse_button2 = Button(text="...", command=self.browse2)
        self.browse_button2.place(x=450,y=40)
        
        self.label3 = Label(master, text="JPG Quality (1-100)")
        self.label3.place(x=20,y=75)
        self.label3.bind("<Enter>", self.l3enter)
        self.label3.bind("<Leave>", self.leave)
        
        self.slidera = Scale(master, from_=1, to=100, orient=HORIZONTAL)
        self.slidera.set(100)
        self.slidera.place(x=140,y=65)
        
        self.opti = False
        self.opti_button = Checkbutton(master, text="Optimize",command=self.opti_switch)
        self.opti_button.place(x=290,y=75)
        self.opti_button.bind("<Enter>", self.opti_enter)
        self.opti_button.bind("<Leave>", self.leave)
        
        self.label7 = Label(master, text="Compress Ratio")
        self.label7.place(x=28, y=115)
        self.label7.bind("<Enter>", self.l7enter)
        self.label7.bind("<Leave>", self.leave)
        
        self.sliderb = Scale(master, from_=16, to=2, orient=HORIZONTAL)
        self.sliderb.place(x=140,y=105)
        
        self.compress_button = Button(master, text="Compress", command=self.compress)
        self.compress_button.place(x=25,y=155)

        self.cancel_button = Button(master, text="Cancel", command=self.end)
        self.cancel_button.place(x=400,y=155)
        
        image1 = PhotoImage(file = 'QuickCompactlogo.gif')
        self.label4 = Label(image = image1)
        self.label4.image = image1 # yes can keep a reference - good!
        self.label4.place(x=33,y=185)
        self.runState =  False
        
    def opti_switch(self):
        if self.opti == True:
            self.opti = False
        else:
            self.opti = True
            
    def l3enter(self, enter):
        self.new_labelb("The lower the number, the smaller the JPG file size. Sacrifices image quality.")
    
    def opti_enter(self, enter):
        self.new_labelb("Performs an extra pass to determine if any more space can be saved.")
    
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
    
    def runStater(self,instance):
        if instance == True:
            self.runState = True
        elif instance == "pass":
            return self.runState
        else:
            self.runState = False
        print(self.runState)
        return self.runState
        
        
    def compress(self):
        global input1 
        input1 = self.textbox1.get()
        global input2
        input2 = self.textbox2.get()
        global input3
        input3 = self.slidera.get()
        global input4
        input4 = self.sliderb.get()
        print("Quality =",input3)
        global optimize
        optimize = self.opti
        print("Optimize =",optimize)
        if input1 == "" or input2 == "":
            print("No entry.\n")
            self.label0.configure(text = "Please select a source directory and destination directory.",fg="red")
        else:
            self.confirmation()
            
    def end(self):
        try:
            self.master2.destroy()
        finally:
            if self.runStater("pass") == False:
                print("Job not yet started.")
                self.new_labela("No job is currently active.")
                self.new_labelb("")
            else:
                print("Stopped.")
                self.runStater(False)
                self.new_labela("Job Stopped.")
                self.new_labelb("")
    
    def new_labela(self, data):
        try:
            if self.label5 != "":
                self.label5.destroy()
            self.label5 = Label(text = data)
            self.label5.place(x=0,y=260)
        except:
            self.label5 = Label(text = data)
            self.label5.place(x=0,y=260)
        
    def new_labelb(self, data):
        try:
            if self.label6 != "":
                self.label6.destroy()
            self.label6 = Label(text = data)
            self.label6.place(x=0,y=280)
        except:
            self.label6 = Label(text = data)
            self.label6.place(x=0,y=280)
    
    def confirmation(self):
        self.master2 = Tk()
        self.master2.title("Confirmation")
        self.master2.geometry("200x120")
        self.master2.resizable(0,0)
        
        self.runStater(True)
        self.master2.iconbitmap('QuickCompactBox.ico')
        if input1 == input2:
            self.warning = Label(self.master2, text = "Original images will be overwritten.")
            self.warning.place(x=5,y=5)
        self.label8 = Label(self.master2, text = "Are you sure?")
        self.label8.place(x=60,y=25)
        
        self.yes = Button(self.master2, text = "Confirm", command=self.confirm)
        self.yes.place(x=15,y=80)
        
        self.no = Button(self.master2, text = "Cancel", command=self.end)
        self.no.place(x=130,y=80)
        
        
    def confirm(self):
        self.master2.destroy()
        try:
            if self.label0 != "":
                self.label0.destroy()
                root.update()
        finally:
            compressor()
    
root = Tk()
myGUI = qcGUI(root)
root.mainloop()