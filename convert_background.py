#!/usr/bin/env python3
"""
Background Image Converter
Converts your crop field image to base64 for embedding in app.py
"""

import base64
import os
from pathlib import Path

def convert_image_to_base64(image_path):
    """Convert an image file to base64 string"""
    try:
        with open(image_path, "rb") as img_file:
            b64_string = base64.b64encode(img_file.read()).decode()
        
        # Determine image type
        ext = Path(image_path).suffix.lower()
        mime_type = {
            '.jpg': 'jpeg',
            '.jpeg': 'jpeg',
            '.png': 'png',
            '.webp': 'webp',
            '.gif': 'gif'
        }.get(ext, 'jpeg')
        
        data_uri = f"data:image/{mime_type};base64,{b64_string}"
        
        print(f"✅ Successfully converted: {image_path}")
        print(f"📊 Image size: {len(b64_string)} characters")
        print(f"📁 File type: {mime_type}")
        print("\n" + "="*70)
        print("Copy the following line to your app.py:")
        print("="*70)
        print(f"\nbackground-image: url('{data_uri[:100]}...');\n")
        print("="*70)
        print("⚠️  Full base64 string saved to: background_base64.txt")
        
        # Save to file for easy copying
        with open("background_base64.txt", "w") as f:
            f.write(data_uri)
        
        return data_uri
        
    except FileNotFoundError:
        print(f"❌ Error: File not found: {image_path}")
        print("\nMake sure your image is in the 'assets' folder")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    print("🌾 Background Image Converter for Smart Crop Yield Predictor")
    print("="*70)
    
    # Check if assets folder exists
    if not os.path.exists("assets"):
        os.makedirs("assets")
        print("📁 Created 'assets' folder")
    
    # Look for common image files
    common_names = [
        "assets/background.jpg",
        "assets/background.jpeg",
        "assets/background.png",
        "assets/wheat_field.jpg",
        "assets/crop_field.jpg"
    ]
    
    found_image = None
    for img_path in common_names:
        if os.path.exists(img_path):
            found_image = img_path
            break
    
    if found_image:
        print(f"\n📸 Found image: {found_image}")
        print("Converting...")
        convert_image_to_base64(found_image)
    else:
        print("\n📸 No background image found in 'assets' folder")
        print("\nPlease:")
        print("1. Save your crop field image to the 'assets' folder")
        print("2. Name it: background.jpg (or .png)")
        print("3. Run this script again")
        print("\nOr enter the path to your image:")
        
        image_path = input("\nImage path: ").strip()
        if image_path and os.path.exists(image_path):
            convert_image_to_base64(image_path)
        else:
            print("❌ Invalid path or file not found")

if __name__ == "__main__":
    main()
