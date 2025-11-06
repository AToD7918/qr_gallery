# -*- coding: utf-8 -*-
"""
Image File Renamer
Renames all images in the img folder to photo.jpg, photo1.jpg, photo2.jpg... format.
"""

import os
import sys
import shutil
from pathlib import Path

def get_script_directory():
    """Get the directory where the script or exe is located"""
    if getattr(sys, 'frozen', False):
        # Running as compiled exe
        return Path(sys.executable).parent
    else:
        # Running as script
        return Path(__file__).parent

def rename_images():
    # img folder path
    script_dir = get_script_directory()
    img_folder = script_dir / 'public' / 'img'
    
    # Create img folder if it doesn't exist
    if not img_folder.exists():
        print(f"Error: Cannot find '{img_folder}' folder.")
        input("Press Enter to exit...")
        return
    
    # Supported image extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.JPG', '.JPEG', '.PNG', '.GIF', '.WEBP', '.BMP'}
    
    # Find image files
    image_files = []
    for file in img_folder.iterdir():
        if file.is_file() and file.suffix in image_extensions:
            image_files.append(file)
    
    if not image_files:
        print("Error: No image files found in img folder.")
        input("Press Enter to exit...")
        return
    
    # Sort by filename (natural order)
    image_files.sort(key=lambda x: x.name.lower())
    
    # Create temporary folder
    temp_folder = img_folder / '_temp_rename'
    temp_folder.mkdir(exist_ok=True)
    
    try:
        # Rename all files
        temp_files = []
        for i, old_file in enumerate(image_files):
            # Use jpg extension
            if i == 0:
                new_name = 'photo.jpg'
            else:
                new_name = f'photo{i}.jpg'
            
            temp_path = temp_folder / new_name
            shutil.copy2(old_file, temp_path)
            temp_files.append((temp_path, new_name))
        
        # Delete original files
        for old_file in image_files:
            old_file.unlink()
        
        # Move from temp folder to img folder
        for temp_file, new_name in temp_files:
            final_path = img_folder / new_name
            shutil.move(str(temp_file), str(final_path))
        
        # Delete temp folder
        temp_folder.rmdir()
        
        print("="*60)
        print("  Image File Renamer - Complete!")
        print("="*60)
        print(f"\nRenamed {len(temp_files)} image(s) successfully:\n")
        
        # Show final result
        final_files = sorted([f for f in img_folder.iterdir() if f.is_file() and f.suffix.lower() in {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}], key=lambda x: x.name.lower())
        for file in final_files:
            print(f"  - {file.name}")
        
        # Update index.html
        update_index_html(len(final_files))
        
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("Cleaning up temporary files...")
        # Cleanup on error
        if temp_folder.exists():
            shutil.rmtree(temp_folder)
    
    print("\n" + "="*60)

def update_index_html(image_count):
    """Automatically update image list in index.html"""
    script_dir = get_script_directory()
    index_file = script_dir / 'public' / 'index.html'
    
    if not index_file.exists():
        print("\nWarning: Cannot find index.html file. Skipping update.")
        return
    
    try:
        # Generate image array
        if image_count == 1:
            images_array = "      'img/photo.jpg'"
        else:
            images_list = ["      'img/photo.jpg'"]
            for i in range(1, image_count):
                images_list.append(f"      'img/photo{i}.jpg'")
            images_array = ',\n'.join(images_list)
        
        # Read index.html
        content = index_file.read_text(encoding='utf-8')
        
        # Find and replace images array
        import re
        pattern = r'const images = \[\s*[^\]]*\];'
        new_images = f'const images = [\n{images_array}\n    ];'
        
        if re.search(pattern, content):
            new_content = re.sub(pattern, new_images, content)
            index_file.write_text(new_content, encoding='utf-8')
            print(f"\nindex.html updated successfully ({image_count} images)")
        else:
            print("\nWarning: Cannot find image array in index.html")
            
    except Exception as e:
        print(f"\nWarning: Error updating index.html: {e}")

if __name__ == '__main__':
    rename_images()
