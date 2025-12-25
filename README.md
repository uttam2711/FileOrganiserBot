# FileOrganiserBot

I have created simple Python program that automatically organizes files in a folder based on their file type.

---

## What This Program Does

* It will scans a folder (like Downloads)
* It will checks file extensions (pdf, jpg, mp3, etc.)
* It will creates folders if they don’t exist
* Moves files into the correct folders

---

## Example

**Before**

```
Downloads/
  file.pdf
  image.jpg
  song.mp3
```

**After**

```
Downloads/
  Documents/file.pdf
  Images/image.jpg
  Music/song.mp3
```

---

## Technologies i have used

* Python
* os module
* shutil module
* time module

(All are built-in Python libraries)

---

## How to Run

1. Clone or download this project
2. Open the Python file
3. Set the folder path:

```python
SOURCE_FOLDER = "C:/Users/YourName/Downloads"
```

4. Run the program:

```bash
python file_organizer.py
```

---

## Menu Options

* Organize files once
* Auto organize every 10 seconds
* Exit

---

## Why I Made This

To practice Python basics and learn how automation works.

---

## Author

Uttam Prajapat

---


