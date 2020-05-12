from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# make sure watchdog is installed - $ python -m pip install watchdog

import os 
import platform
import json
import time
import filetype

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if platform.system() == "Windows":
            #create relevant folders in Downloads directory
        
        if platform.system() == "Darwin":
            #create relevant folders in Downloads directory

        for filename in os.listdir(folder_to_track):
            file_name, file_extension = os.path.splitext(filename)
            if file_extension in audioExt:
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/Audio" + "/" + filename
                os.rename(src, new_destination)
            if file_extension == '.pdf':
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/PDF" + "/" + filename
                os.rename(src, new_destination)
            if file_extension == '.zip':
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/ZIP" + "/" + filename
                os.rename(src, new_destination)
            if file_extension == '.dmg':
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/DMG" + "/" + filename
                os.rename(src, new_destination)

folder_to_track = "/Users/redwankhan/Downloads"
folder_destination = "/Users/redwankhan/Downloads"

audioExt = ['.mp3'] 

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
    