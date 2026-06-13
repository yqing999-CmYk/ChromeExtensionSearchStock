#!/usr/bin/env python3
"""Generate simple PNG icons for the extension."""
import os
from PIL import Image, ImageDraw, ImageFont

# Create icons directory
os.makedirs('icons', exist_ok=True)

# Define icon sizes
sizes = [16, 48, 128]

for size in sizes:
    # Create image with white background
    img = Image.new('RGB', (size, size), color='#1f77d9')  # Chrome blue
    draw = ImageDraw.Draw(img)

    # Draw a simple "$" symbol for stock
    # For small icons, just fill with gradient or pattern
    if size == 16:
        # Tiny icon: just a solid color
        pass
    elif size == 48:
        # Medium icon: draw a simple $ symbol
        draw.text((size//4, size//4), '$', fill='white')
    else:
        # Large icon: draw a styled $ symbol
        draw.text((size//3, size//3), '$', fill='white')

    # Save as PNG
    img.save(f'icons/icon-{size}.png')
    print(f'Created icons/icon-{size}.png')

print('Icons created successfully!')
