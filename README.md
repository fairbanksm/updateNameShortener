# updateNameShortener

### Purpose

This came about from a couple of servers we have that have issues with downloading updates from Mocrosoft automatically.  This lead to me downloading updates manually from the Microsoft Update Catalog site.  There's only a handful of servers that I do this for, so it's not a big deal.  

I also  wanted to be able to copy the files from server to server rather than trying to install across the network via a share.  Every now and then, Windows will complain that the file paths are too long.  

Since I've also been trying to learn Python, I thought it might be fun to try and write something that will automate some of this process.  

### Function
This is a pretty short and simple script, and here's what it does:
 * Looks in for folder defined in the **path** variable at the top of the script. 
 * If the filename ends with .lnk, the file will be skipped. 
 * Otherwise, the file/folder will be renamed.  Regardless of length, the new name will be shortented to only contain the first 7 and last 11 characters of the original name.  Microsoft if fairly consistent with their nameing convention and this will result in a filename that looks like this: 2020-07 (KN4565479)
 
### To-Do
 * Rather then an exception for .lnk files, have the script just differentiate between files and folders and only work with folders. 
   * Possibly have the script just exclude *.* as a workaround.
 * Have the script copy the folders to the other servers, even if it has to call something windows based like robocopy.
 * Have the script remove the folders for updates that have already been installed.  Perhaps if create date > two weeks. 

### Note
Yes, I know I should probably just fix the servers so they work with Windows update.  
