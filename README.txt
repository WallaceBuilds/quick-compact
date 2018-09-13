								QuickCompact Documentation
								 Managed by WallaceBuilds

----- QuickCompact 0.9.0 -----
----- September 13, 2018 -----

--- Current Functions ---

Source Directory - This is the folder/directory that the program will draw files from. The program is not currently built to pull files discriminately, 
	so all files in the directory will be passed to the compression function and then verified to be compatible image files.

	If this section is not filled in, users will be asked to complete it with a dialogue between the "Compress" and "Cancel" buttons.

Destination Directory - This is the folder/directory that the program will place compressed files into. Since the program is not currently designed to 
	rename files as they are processed, choosing the Source Directory as the Destination Directory will result in a total overwrite of all image files
	that are passed through the compression function. At the confirmation window, a special dialogue will warn users that this is the intended function.
	
	If this section is not filled in, users will be asked to complete it with a dialogue between the "Compress" and "Cancel" buttons.

JPG Quality - A slider that ranges from 1 to 100, its purpose is to allow the user to manually set the quality of JPG images. Doing this also allows them to
	increase or decrease the file size of each JPG image. This slider defaults at 100, which is a full quality compression.

Optimize - This function has the potential to decrease the file size of each image at the sake of increasing the amount of time the batch will take.

Compress Ratio - A slider that ranges from 16 to 2, it determines the final, reduced size of each image. For example, a compress ratio of 2 will divide the 
	original image's x and y values by 2, whereas a compress ratio of 16 divides the original image's x and y values by 16. This slider defaults at 2, 
	which is technically a 4:1 compression.


--- Dev Notes ---

The program is functioning as anticipated on a Windows 10 machine, using Spyder as the IDE of choice.

When running on a Raspberry Pi (Raspbian Stretch with Python 3.5) I had an issue getting the QuickCompact .ico recognized by the machine. I commented this
out and it began running as expected (even the browse buttons were working). The GUI was not very clean like it is when running on Windows, this is due 
to each item being placed on the frame rather than being gridded onto the plane. I personally find the grid form of the program to be horrendous looking, 
but I may make a separate branch to make it prettier on Linux/other machines.

That time estimation algorithm is quick and dirty. I personally wish to revise it and find a way to make it accurate, but this will likely take some serious 
time. 

I would like to make JPG Quality applicable to other file formats as well, but this will take a lot more lines of code to complete, as each file type
requires a different process in order to change its "quality".

Optimize doesn't always make a filesize smaller, which is not at all what I expect when using it. Not sure why this is, but it could be a shortcoming of
the PIL library.

Speaking of shortcomings of the PIL library, I would like to see about replacing PIL with the actively-updated Pillow library. From what I have researched,
PIL has become abandonware. This is unfortunate, but changing over to Pillow may make some fixes easier to implement, such as making the Quality slider more
applicable to other file formats.




