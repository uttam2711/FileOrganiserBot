import os
import shutil
import time

# ===== STEP 1: Folder Path (CHANGE THIS) =====
SOURCE_FOLDER = "C:\\Users\\uttam prajapat\\OneDrive\\Desktop\\Downloads"   # Example: "C:/Users/YourName/Downloads"

# ===== STEP 2: File Categories =====
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"]
}

# ===== STEP 3: It will Create Folder if Not Exists =====
def create_folder(folder_name):
    folder_path = os.path.join(SOURCE_FOLDER, folder_name)
    if not os.path.exists(folder_path):         # Create folder only if it does not already exist
        os.mkdir(folder_path)

# ===== STEP 4: Find File Category =====
def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return "Others"

# ===== STEP 5: Organize Files =====
def organize_files():
    print("📂 Organizing files...")

    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isdir(file_path):         #Skip folders, only process files
            continue

        extension = os.path.splitext(file)[1].lower()
        category = get_category(extension)

        create_folder(category)

        destination = os.path.join(SOURCE_FOLDER, category, file)

        # Handle duplicate file names
        if os.path.exists(destination):
            name, ext = os.path.splitext(file)
            destination = os.path.join(
                SOURCE_FOLDER, category, f"{name}_copy{ext}"
            )

        shutil.move(file_path, destination)   # Move file to the category folder

    print("✅ Files organized successfully!")

# ===== STEP 6: Menu Driven Program =====
def menu():
    while True:
        print("\n--- FILE ORGANIZER BOT ---")
        print("1. Organize files once")
        print("2. Auto organize every 10 seconds")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            organize_files()

        elif choice == "2":
            print("⏳ Auto organizer started (Press Ctrl + C to stop)")
            try:
                while True:
                    organize_files()
                    time.sleep(10)   # Wait for 10 seconds
            except KeyboardInterrupt:
                print("\n⛔ Auto organizer stopped")

        elif choice == "3":
            print("👋 Exited program")
            break

        else:
            print("❌ Invalid choice")

# ===== STEP 7: Run Program =====
if __name__ == "__main__":
    if not os.path.exists(SOURCE_FOLDER):
        print("❌ Source folder does not exist")    # Check if source folder exists before running
    else:
        menu()
