import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

# 1. Load the pristine clean in-painted crop from original mockup
orig_img = Image.open('public/images/header_liquid_clean.png').convert('RGB')
w_orig, h_orig = orig_img.size

# 2. Resize to 3840x360 with high-quality Lanczos resampling
orig_4k = orig_img.resize((3840, 360), Image.Resampling.LANCZOS)
orig_4k_np = np.array(orig_4k).astype(np.float32)

# 3. Load the procedurally synthesized 4K specular & caustic layer
synth_4k = Image.open('public/images/header_liquid_4k_ultra.png').convert('RGBA')
synth_4k_np = np.array(synth_4k).astype(np.float32)

# 4. Blend the two layers for maximum photorealism + 4K ultra-sharpness:
# Compute alpha mask where the wave exists in either layer
y_grid, x_grid = np.mgrid[0:360, 0:3840].astype(np.float32)

# Where the original has blue / water structure:
orig_diff = 255.0 - cv2.cvtColor(orig_4k_np.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
orig_blue = np.clip(orig_4k_np[:, :, 2] - orig_4k_np[:, :, 0], 0, 255)
orig_alpha = np.clip(orig_diff * 1.5 + orig_blue * 1.8, 0, 255)

# Smooth vertical organic fade at the bottom (y: 200 to 360)
fade = np.clip((360.0 - y_grid) / 160.0, 0.0, 1.0) ** 1.4
combined_alpha = np.clip(np.maximum(orig_alpha * fade, synth_4k_np[:, :, 3]), 0, 255)

# Blend RGB: combine original photo depth with procedural caustic glints
blended_rgb = orig_4k_np * 0.7 + synth_4k_np[:, :, :3] * 0.3

# Enhance sharpness & contrast
master_rgba = np.dstack((blended_rgb.astype(np.uint8), combined_alpha.astype(np.uint8)))
master_img = Image.fromarray(master_rgba, 'RGBA')

enhancer = ImageEnhance.Sharpness(master_img)
master_img = enhancer.enhance(1.25)

master_img.save('public/images/header_liquid_master_4k.png', 'PNG')
print('Master 4K 3840x360 Liquid Wave Header blended successfully!')
