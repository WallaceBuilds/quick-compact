								QuickCompact Documentation
								 Managed by WallaceBuilds

----- QuickCompact 0.9.0 -----
----- September 13, 2018 -----

--- Current Functions ---

Source Directory - This is the folder/directory that the program will draw files from. The program is not currently built to pull files discriminately, so all files in the directory will be passed to the compression function and then verified to be compatible image files.

NOTE: If this section is not filled in, users will be asked to complete it with a dialogue between the "Compress" and "Cancel" buttons.

Destination Directory - This is the folder/directory that the program will place compressed files into. Since the program is not currently designed to rename files as they are processed, choosing the Source Directory as the Destination Directory will result in a total overwrite of all image files that are passed through the compression function. At the confirmation window, a special dialogue will warn users that this is the intended function.
	
NOTE: If this section is not filled in, users will be asked to complete it with a dialogue between the "Compress" and "Cancel" buttons.

JPG Quality - A slider that ranges from 1 to 100, its purpose is to allow the user to manually set the quality of JPG images. Doing this also allows them to increase or decrease the file size of each JPG image. This slider defaults at 100, which is a full quality compression.

Optimize - This function has the potential to decrease the file size of each image at the sake of increasing the amount of time the batch will take.

Compress Ratio - A slider that ranges from 16 to 1, it determines the final, reduced size of each image. For example, a compress ratio of 2 will divide the original image's x and y values by 2, whereas a compress ratio of 16 divides the original image's x and y values by 16. This slider defaults at 4.


--- Dev Notes ---

- The program is functioning as anticipated on a Windows 10 machine, using Spyder as the IDE of choice.

- When running on a Raspberry Pi (Raspbian Stretch with Python 3.5) I had an issue getting the QuickCompact .ico recognized by the machine. I commented this out and it began running as expected (even the browse buttons were working). The GUI was not very clean like it is when running on Windows, this is due to each item being placed on the frame rather than being gridded onto the plane. I personally find the grid form of the program to be horrendous looking, but I may make a separate branch to make it prettier on Linux/other machines.

- That time estimation algorithm is quick and dirty. I personally wish to revise it and find a way to make it accurate, but this will likely take some serious time.
 
- Thinking about knocking out that time estimation program by having it determine the total size of the image files in a directory and then calculating out the KB/s threshold of the machine the code is currently running on. This will make the speed data much more accurate and it won't be relying on hacky .txt files.

- I would like to make JPG Quality applicable to other file formats as well, but this will take a lot more lines of code to complete, as each file type requires a different process in order to change its "quality".

- Optimize doesn't always make a filesize smaller, which is not at all what I expect when using it. Not sure why this is, but it could be a shortcoming of the PIL library.

- Speaking of shortcomings of the PIL library, I would like to see about replacing PIL with the actively-updated Pillow library. From what I have researched, PIL has become abandonware. This is unfortunate, but changing over to Pillow may make some fixes easier to implement, such as making the Quality slider more applicable to other file formats.

- I would like to separate the compression method into new methods, and make compression a class. This will be a small undertaking, but nothing too serious.

- Skipping files that cause critical errors means that an image file that could potentially be compressed is skipped, such as those with an incorrect extension in the name that does not accurately depict the filetype. This means the verifier needs to be re-written, as it relies on the name of the image rather than the actual extension.




----- QuickCompact 0.9.1 -----
-----   Weekend Update   -----
----- September 16, 2018 -----


--- Added Functions ---

Compress Ratio has been renamed to Resize Factor.

Antialias - This functtion allows the user to select or bypass the antialiasing tool built into PIL/Pillow. Using it will make text in image files much clearer, but this also adds more complexity to the image files, thus increasing the final filesize after compression.


--- Major Updates ---

- Completely rebuilt the compression script, now using classes and methods.
--- This made the code so much cleaner than before and gives me the ability to add extra things into it.
--- The time estimation is much better now. It doesn't rely on .txt files anymore, but I am looking at using Pickle to save a computer's average ability to run through files. This will help make the time estimation system a little more accurate over time.
--- I will update the script with comments soon, I'd like to have more documentation inside the code.

- Linux/Mac OS friendly version of QuickCompact
--- Font is manually set to Sans 12.
--- Window size is larger for both the main window and confirmation window.
--- Textboxes are expanded for larger directory paths.
--- The .ico has been reformatted to .xbm, it's not as pretty as the Windows .ico, but it actually operates. (Need to see if the .ico will work with Mac OS, I didn't have any callbacks when running the non-Linux friendly version.)

- Skipping files that can cause critical errors, such as files with incorrect file formats.


--- Minor Updates ---

- Commented on the major GUI elements under the __init__ method. This makes it a little easier to understand what is going on in the code.
- time.clock() replaced with time.perf_counter()
- Fixed bug that can cause the Confirmation window to be repeatedly called.


--- Dev Notes ---

- It would be nice to add some more features to the image processing, for example watermarking images or converting them to Black/White or Grayscale.
- The critical errors that occur from accessing files without proper permissions can still occur. For some reason they bypass the checker method and continue to be processed. I will be addressing this as soon as possible, but it will not be ready until 0.9.2 is done.
- Integration with the Pillow library works as expected, now I just need to determine what is possible with it.

