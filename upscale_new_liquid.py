import numpy as np
from PIL import Image, ImageEnhance

# Load new asset
orig_img = Image.open('/Users/arthur/.gemini/antigravity/brain/894a23c3-0b06-42cb-8ce0-b7c760180536/.user_uploaded/media_1788371031750.png')

# Tightly crop to content: y from 4 to 270
tight_crop = orig_img.crop((0, 4, 1024, 270))
w_c, h_c = tight_crop.size

# Target width 4096 px (4K Ultra HD)
target_w = 4096
target_h = int(round(h_c * (target_w / float(w_c))))

print(f"Upscaling from {w_c}x{h_c} to {target_w}x{target_h} using high-precision Lanczos...")

hd_img = tight_crop.resize((target_w, target_h), Image.Resampling.LANCZOS)

# Enhance clarity, glint, and vibrance
r, g, b, a = hd_img.split()
rgb = Image.merge('RGB', (r, g, b))

sharp = ImageEnhance.Sharpness(rgb).enhance(1.4)
contrast = ImageEnhance.Contrast(sharp).enhance(1.08)
color = ImageEnhance.Color(contrast).enhance(1.08)

r_f, g_f, b_f = color.split()
final_hd = Image.merge('RGBA', (r_f, g_f, b_f, a))

final_hd.save('public/images/navbar_liquid_vibrant_4k.png', format='PNG', optimize=True)
print(f"Saved new 4K liquid wave to public/images/navbar_liquid_vibrant_4k.png! Size: {final_hd.size}")
