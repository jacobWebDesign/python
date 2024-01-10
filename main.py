import os
from pathlib import Path
import shutil


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

archive = (".zip", ".rar")

document = (".pdf", ".docx", ".txt", ".pptx", ".ppt", ".odt", ".csv", ".doc", ".ods", ".html", ".url", ".htm")

#Getting the OS username
def get_username_os():
    return os.getenv("USERNAME")
username = get_username_os()

#When user paste the link it often has double quotes at the beginning and the end. I wrote this to prevent script from crashing
def quote_remover(text):
    if '"' in text:
        text = text.replace('"', '')
    return text

#List of mine default directories
img_dir ='/Users/' + username + '/OneDrive/Obrazy'
audio_dir = '/Users/' + username + '/Music/'
video_dir = '/Users/' + username + '/Videos/'
archive_dir = ""
documents_dir = '/Users/'+ username +'/OneDrive/Dokumenty'

#Interactive script. It asks if user wants to create Archive's directory
def archive_create():
    while(True):
        value = input("Do you want to create a folder with archives?(.zip, .rar etc.)\nY/N\n")
        if value == "y" or value == "Y":
            while(True):
                try:
                    dir = quote_remover(input("Enter the directory where you want to create 'archive' folder"))
                    os.chdir(dir)
                    Path("archives").mkdir(exist_ok=True)
                    global archive_dir
                    archive_dir = dir+"/archives"
                    return True
                except FileNotFoundError:
                    print("There's no such directory, try again")

        elif value == "n" or value == "N":
            print("Okay, the folder won't be created")
            return False
        else:
            print("No such answer")
        
archive_defined = archive_create()
print(archive_dir)

#Checking if the default directories exists on the computer. If not, asks user to insert them
def dir_validation():
    try:
        global img_dir
        os.chdir(img_dir)
        
    except FileNotFoundError:
        img_dir = input("Image directory not found. Insert image directory\n")
        img_dir = quote_remover(img_dir)
        dir_validation()

    try:
        global audio_dir
        os.chdir(audio_dir)
    except FileNotFoundError:
        audio_dir = input("Audio directory not found. Insert audio directory\n")
        audio_dir = quote_remover(audio_dir)
        dir_validation()

    try:
        global video_dir
        os.chdir(video_dir)
    except FileNotFoundError:
        video_dir = input("Video directory not found. Insert video directory\n")
        video_dir = quote_remover(video_dir)
        dir_validation()
    if archive_defined == True:
        try:
            global archive_dir
            os.chdir(archive_dir)
        except FileNotFoundError:
            archive_dir = input("Archive directory not found. Insert archive files directory(zip, rar, itd)\n")
            archive_dir = quote_remover(archive_dir)
            dir_validation()

    try:
        global documents_dir
        os.chdir(documents_dir)
    except FileNotFoundError:
        documents_dir = input("Documents directory not found. Insert documents directory\n")
        documents_dir = quote_remover(documents_dir)
        dir_validation()

dir_validation()

#Defining a variable which will be used in the next script
working_dir = ""
#Setting the working directory and validation if it exists
def working_directory():
    try:
        working_dir = quote_remover(input("Choose the path in which you want to clean up the mess\n"))
        os.chdir(working_dir)
    except FileNotFoundError:
        print("Directory not found :c\n Try again!")
        working_directory()
    return working_dir

working_dir = working_directory()

#File's type checking script
def is_audio(file):
    return os.path.splitext(file)[1] in audio
def is_video(file):
    return os.path.splitext(file)[1] in video 
def is_img(file):
    return os.path.splitext(file)[1] in img    
def is_archive(file):
    return os.path.splitext(file)[1] in archive
def is_document(file):
    return os.path.splitext(file)[1] in document

#Sorting script
def organizer(dir):
    print("Directory ",dir)
    os.chdir(dir)
    print("Changed directory to ", dir)
    for file in os.listdir():
        if is_audio(file):
            shutil.move(file, audio_dir)
            print("Found audio")
        elif is_video(file):
            shutil.move(file, video_dir)
            print("Found video")
        elif is_img(file):
            shutil.move(file, img_dir)
            print("Found img")
        elif is_archive(file) and archive_defined == True:
            try:
                shutil.move(file, archive_dir)
            except:
                print("Found archive, but it already exists in the destination folder\n")
        elif is_document(file):
            shutil.move(file, documents_dir)

organizer(working_dir)
print("The sort is done :D")
