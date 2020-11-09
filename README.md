# updateNameShortener

### Purpose

This came about from a couple of servers we have that have issues with downloading updates from Microsoft automatically.  This lead to me downloading updates manually from the Microsoft Update Catalog site.  There's only a handful of servers that I do this for, so it's not a big deal.  

I also  wanted to be able to copy the files from server to server rather than trying to install across the network via a share.  Every now and then, Windows will complain that the file paths are too long.  

Since I've been trying to learn Python, I thought it might be fun to try and write something that will automate some of this process.  

### Function
This is a pretty short and simple script, and here's what it does:
 * Lists the contentents of the directory defined in the **path** variable at the top of the script. 
 * Each object will be tested as to whether or not it is a directory. 
 * If the object is found to be a directory, it will be renamed.  
 * Regardless of length, the new name will be shortented to only contain the first 7 and last 11 characters of the original name.  Microsoft is fairly consistent with their naming convention and this will result in a filename that looks like this: 2020-07 (KB4565479)
 
### To-Do
 * Have the script use regex for the rename rather than reliing on character count rules. 
   * For date at the beginning ##-####
   * For the KB at the end, look for KB########, disregard the number of digits and maybe keep the parenthesis.
 * Have the script copy the directories to the other servers, even if it has to call something Windows based like robocopy.  Preferably not though.
 * Have the script remove the directories for updates that have already been installed.  Perhaps if create date > two weeks. 
 * Delete the old updates.
   * Option 1 - Delete any directory with a last modified date older than a week or two. 
   * Option 2 - Get the script to read the current date, figure out what month it is, and then delete anything that doesn't match the ####-## format of the current month. 

### Note
Yes, I know I should probably just fix the servers so they work with Windows update.  
