#=============================================================================
#   ZeroByteCleaner – Automated File System Cleanup Tool
#
#   Author  : Sanket Sadashiv Hajare
#   License : MIT License
#=============================================================================

import os
import sys
import time
import schedule

def DirectoryScanner(DirName):
    border = "-"*57

    timestamp = time.ctime()

    LogfileName = "ZeroByteCleaner_Report_%s.log" %(timestamp)

    LogfileName = LogfileName.replace(" ","_")               
    LogfileName = LogfileName.replace(":","_")                

    fobj = open(LogfileName,"w")

    fobj.write(border + "\n")
    fobj.write("     This is a log file created by 'ZeroByteCleaner'     \n")
    fobj.write("---------- Automated File System Cleanup Tool -----------\n")
    fobj.write(border + "\n")
    fobj.write("Author      : Sanket Sadashiv Hajare\n")
    fobj.write("Description : Removes empty (0-byte) files from directory\n")
    fobj.write(f"Timestamp  : {timestamp} \n")
    fobj.write(border + "\n\n")

    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        fobj.write(border+"\n")
        fobj.write(f"ERROR: '{DirName}' is not exist.\n")
        fobj.write(border+"\n")
        fobj.close()
        sys.exit()
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        fobj.write(border+"\n")
        fobj.write(f"ERROR: '{DirName}' is not a directory.\n")
        fobj.write(border+"\n")
        fobj.close()
        sys.exit()

    FileCount = 0
    EmptyFileCount = 0

    for FolderName, SubFolder, FileName in os.walk(DirName):
        
        for fname in FileName:
            FileCount = FileCount + 1
        
            fname = os.path.join(FolderName,fname)
            
            if(os.path.getsize(fname) == 0):       
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)

    fobj.write(border+"\n")
    fobj.write("Total file scanned          : "+str(FileCount)+"\n")
    fobj.write("Total Empty file found      : "+str(EmptyFileCount)+"\n")
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(border+"\n")

    fobj.close()


def main():
    border = "-"*56
    print(border)
    print("-------------- ZeroByteCleaner Automation --------------")
    print(border)
    
    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return
    
    DirectoryScanner(sys.argv[1])

    schedule.every(1).minutes.do(DirectoryScanner, sys.argv[1])

    while(True):
        schedule.run_pending()
        time.sleep(1)


    print(border)
    print("---- Thank You For Using ZeroByteCleaner Automation ----")
    print(border)

if __name__ == "__main__":
    main()