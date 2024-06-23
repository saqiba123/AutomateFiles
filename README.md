# File Organizer Script
## Overview
This Python script organizes files in a directory into subfolders based on their file types.

## Prerequisites
Python 3.x
## Usage
Clone the repository:
```
git clone https://github.com/saqiba123/file-organizer.git
```
cd file-organizer

Set directory path:

Modify directory_path in the script to your target directory.
Run the script:
```
python automate_file.py
```
## Functionality
Creates subfolders: Based on file types like documents, images, videos, audio, and others.
Moves files: Files are moved to corresponding subfolders.
### File Types
myDocs: .pdf, .doc, .docx, .txt
myImgs: .jpg, .jpeg, .png, .gif
myVideo: .mp4, .avi, .mov
myAudio: .mp3, .wav, .aac
others: Unspecified file types
Example
Before:
```
Data
├── file1.pdf
├── file2.jpg
├── file3.mp4
├── file4.mp3
└── file5.xyz
```
After:
```
Data
├── myDocs
│   └── file1.pdf
├── myImgs
│   └── file2.jpg
├── myVideo
│   └── file3.mp4
├── myAudio
│   └── file4.mp3
└── others
    └── file5.xyz
```
