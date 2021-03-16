import os
from watchdog.events import FileSystemEventHandler
from cfg import *


class Handler(FileSystemEventHandler):

    def on_modified(self, event):

        for filename in os.listdir(folder_track):
            extension = filename.split(".")

            if len(extension) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "png"
                                       or extension[1].lower() == "svg"):
                file = folder_track + "\\" + filename
                new_path = folder_dest + "\\Pictures\\" + filename
                os.rename(file, new_path)

            elif len(extension) > 1 and extension[1].lower() == "mp4":
                file = folder_track + "\\" + filename
                new_path = folder_dest + "\\Videos\\" + filename
                os.rename(file, new_path)

            elif len(extension) > 1 and (extension[1].lower() == "doc" or extension[1].lower() == "docx" or
                                         extension[1].lower() == "pdf") :
                file = folder_track + "\\" + filename
                new_path = folder_dest + "\\Documents\\" + filename
                os.rename(file, new_path)

            elif len(extension) > 1 and (extension[1].lower() == "zip" or extension[1].lower() == "rar" or
                                         extension[1].lower() == "iso"):
                file = folder_track + "\\" + filename
                new_path = folder_dest + "\\WinRar\\" + filename
                os.rename(file, new_path)

            elif len(extension) > 1 and extension[1].lower() == "exe":
                file = folder_track + "\\" + filename
                new_path = folder_dest + "\\Exe\\" + filename
                os.rename(file, new_path)

            elif len(extension) > 1 and extension[1].lower() == "torrent":
                file = folder_track + "\\" + filename
                new_path = folder_dest + "\\torrent\\" + filename
                os.rename(file, new_path)

            elif len(extension) > 1 and extension[1].lower() == "py":
                file = folder_track + "\\" + filename
                new_path = folder_dest + "\\python\\" + filename
                os.rename(file, new_path)
