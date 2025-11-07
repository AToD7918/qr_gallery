# -*- coding: utf-8 -*-
"""
QR Code Generator for qr_gallery
Generates QR code for the deployed website URL
"""

import qrcode
from pathlib import Path
from datetime import datetime

def generate_qr():
    # Website URL
    url = "https://qr-gallery.vercel.app/"
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,  # Size (1-40, None for auto)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Pixel size per box
        border=4,  # Border size (minimum is 4)
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save location
    script_dir = Path(__file__).parent
    output_folder = script_dir / 'qr_codes'
    output_folder.mkdir(exist_ok=True)
    
    # Filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_folder / f'qr_gallery_{timestamp}.png'
    
    # Save image
    img.save(output_file)
    
    print("="*60)
    print("  QR Code Generated Successfully!")
    print("="*60)
    print(f"\nURL: {url}")
    print(f"Saved to: {output_file}")
    print("\nYou can now scan this QR code to access the menu gallery!")
    print("="*60)

if __name__ == '__main__':
    try:
        generate_qr()
    except ImportError:
        print("\nError: 'qrcode' module is not installed.")
        print("\nPlease install it using:")
        print("  pip install qrcode[pil]")
        print("\nor:")
        print("  pip install qrcode pillow")
    except Exception as e:
        print(f"\nError occurred: {e}")
