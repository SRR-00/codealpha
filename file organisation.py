import os
import shutil

def organize_files(source_folder, destination_folder):
    # Ensure the destination folder exists; create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")

    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)

      
        if os.path.isfile(source_file):
           
            _, extension = os.path.splitext(filename)
            extension = extension[1:] 

            # Create a folder for the extension if it doesn't exist
            extension_folder = os.path.join(destination_folder, extension)
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)
                print(f"Created folder for {extension} files")

            # Prepare the destination path
            destination_file = os.path.join(extension_folder, filename)

            try:
                # Move the file to the destination folder
                shutil.move(source_file, destination_file)
                print(f"Moved {filename} to {extension} folder")
            except Exception as e:
                print(f"Failed to move {filename}: {e}")

if __name__ == "__main__":          
  
    source_folder = "C:/Users/DELL/Desktop/New folder (2)"
    destination_folder = "C:/Users/DELL/Desktop/project/notes"

    print(f"Organizing files from {source_folder} to {destination_folder}...")
    organize_files(source_folder, destination_folder)
    print("File organization complete.")
