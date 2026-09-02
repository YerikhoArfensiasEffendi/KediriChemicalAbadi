import numpy as np
import cv2
from PIL import Image, ImageEnhance, ImageFilter

# Load the authentic transparent PNG
orig_img = Image.open('/Users/arthur/.gemini/antigravity/brain/894a23c3-0b06-42cb-8ce0-b7c760180536/.user_uploaded/media_1788369636817.png')
w_orig, h_orig = orig_img.size

# Target 4K Ultra-Wide resolution: 4096 x 1364 (4x Scale)
target_w = 4096
target_h = int(round(h_orig * (target_w / float(w_orig))))

print(f"Upscaling from {w_orig}x{h_orig} to {target_w}x{target_h} using high-precision Lanczos...")

# 1. Super-sampling with Lanczos
hd_img = orig_img.resize((target_w, target_h), Image.Resampling.LANCZOS)

# 2. Separate RGB and Alpha
r, g, b, a = hd_img.split()
rgb_img = Image.merge('RGB', (r, g, b))

# 3. Enhance Sharpness on the RGB detail
sharpener = ImageEnhance.Sharpness(rgb_img)
rgb_sharp = sharpener.enhance(1.4)

# 4. Enhance Contrast slightly for crystal glint
contrast = ImageEnhance.Contrast(rgb_sharp)
rgb_enhanced = contrast.enhance(1.08)

# 5. Enhance Color Vibrance slightly for pure aqua blue
color = ImageEnhance.Color(rgb_enhanced)
rgb_final = color.enhance(1.05)

# Re-assemble RGBA with sharp alpha
r_f, g_f, b_f = rgb_final.split()
final_hd = Image.merge('RGBA', (r_f, g_f, b_f, a))

# Save Ultra HD 4K assets
final_hd.save('public/images/navbar_liquid_4k_ultra.png', format='PNG', optimize=True)
print("Saved public/images/navbar_liquid_4k_ultra.png successfully!")

# Also let's save a cropped top version that fits the navbar header directly (4096 x 600)
bbox = final_hd.getbbox()
print("Final HD Bounding Box:", bbox)
cropped_hd = final_hd.crop((0, 0, target_w, min(bbox[3] + 40, target_h)))
cropped_hd.save('public/images/navbar_liquid_4k_tight.png', format='PNG', optimize=True)
print(f"Saved tight fit version {cropped_hd.size} to public/images/navbar_liquid_4k_tight.png!")

