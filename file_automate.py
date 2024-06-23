import os
import shutil

def automate_file(directory_path):
    
    # Create subfolders for different file types
    subfolders = {
        "myDocs": [".pdf", ".doc", ".docx", ".txt"],
        "myImgs": [".jpg", ".jpeg", ".png", ".gif"],
        "myVideo": [".mp4", ".avi", ".mov"],
        "myAudio": [".mp3", ".wav", ".aac"],
        # "myJson": [".json"],
        "others":[]
    }
    # Iterate over files in the main folder
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        # Check if it's a file (not a folder)
        if os.path.isfile(file_path):
            # Get the file extension
            #The underscore _ is a common convention in Python for a variable that is going to be ignored.
            _, extension = os.path.splitext(filename)
            
            # Determine the appropriate subfolder
            subfolder = "Others"
            for folder, extensions in subfolders.items():
                if extension.lower() in extensions:
                    subfolder = folder
                    break
            
            # Create the subfolder if it doesn't exist
            subfolder_path = os.path.join(directory_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)
            
            # Move the file to the appropriate subfolder
            destination_path = os.path.join(subfolder_path, filename)
            shutil.move(file_path, destination_path)
            
            print(f"Moved {filename} to {subfolder} folder.")
            
            

# Define the main folder path
directory_path = "C:\\Users\\Admin\\Downloads\\practice\\Data"
automate_file(directory_path)
