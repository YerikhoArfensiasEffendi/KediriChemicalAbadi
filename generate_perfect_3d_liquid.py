import numpy as np
import cv2
from PIL import Image, ImageFilter, ImageEnhance

# Canvas: 3840 x 360 (Ultra HD 4K, 16:9 ultra-wide)
W, H = 3840, 360

y_grid, x_grid = np.mgrid[0:H, 0:W].astype(np.float32)

# 1. Base Gradient Canvas (Crystal Clear Sky Cyan to Royal Blue Liquid)
# Center coordinates for ripples on left around the logo
cx, cy = 200.0, 90.0
r = np.sqrt((x_grid - cx)**2 + ((y_grid - cy) * 1.6)**2)

# Concentric Ripple Harmonics
ripples = (
    np.sin(r * 0.075) * np.exp(-r * 0.003) * 0.45 +
    np.sin(r * 0.038 - 0.7) * np.exp(-r * 0.0018) * 0.35 +
    np.sin(r * 0.11 + 1.2) * np.exp(-r * 0.005) * 0.2
) * np.clip(1.0 - r / 1100.0, 0, 1)

# 2. Dynamic 3D Liquid Waves (Dual Ribbon Flow across full width)
t = x_grid / float(W)

# Primary Wave: Dips down smoothly between x=0.3 and 0.8
wave1_y = 70.0 + 45.0 * np.sin(t * np.pi * 2.1 - 0.2) + 25.0 * np.sin(t * np.pi * 4.2 + 0.8)
dist1 = y_grid - wave1_y
w1_thick = 50.0 + 20.0 * np.sin(t * np.pi * 3.0)
wave1 = np.exp(-((dist1 / w1_thick) ** 2))
crest1 = np.exp(-(((dist1 + 14.0) / 11.0) ** 2)) * 0.85

# Secondary Wave: Intertwining wave ribbon for volumetric 3D liquid depth
wave2_y = 45.0 + 55.0 * np.sin(t * np.pi * 1.8 + 1.2) + 18.0 * np.cos(t * np.pi * 3.5)
dist2 = y_grid - wave2_y
wave2 = np.exp(-((dist2 / 38.0) ** 2)) * 0.65
crest2 = np.exp(-(((dist2 + 10.0) / 9.0) ** 2)) * 0.75

# 3. Micro Splash Droplets & Crystal Water Beads
np.random.seed(101)
droplets = np.zeros((H, W), dtype=np.float32)
for _ in range(140):
    dx_pos = np.random.uniform(50, W - 50)
    dt = dx_pos / float(W)
    wy = 60.0 + 45.0 * np.sin(dt * np.pi * 2.0) + np.random.uniform(-45, 60)
    rad = np.random.uniform(2.5, 12.0)
    br = np.random.uniform(0.5, 1.0)
    if 0 <= wy < H:
        d_dist = np.sqrt((x_grid - dx_pos)**2 + (y_grid - wy)**2)
        drop_val = np.exp(-((d_dist / rad)**2)) * br
        # Gleam highlight
        gleam = np.exp(-(((x_grid - dx_pos + rad*0.3)**2 + (y_grid - wy + rad*0.3)**2) / (rad*0.3)**2))
        droplets = np.maximum(droplets, drop_val + gleam * 0.8)

# 4. Total Fluid and Light Channels
fluid = np.clip(wave1 * 0.75 + wave2 * 0.5 + ripples * 0.55 + droplets * 0.75, 0, 1)
glint = np.clip(crest1 * 0.9 + crest2 * 0.7 + np.clip(ripples, 0, 1) * 0.45 + droplets * 0.65, 0, 1)

# Color shading:
# Deep blue in thick body: RGB(14, 88, 168)
# Aqua in mids: RGB(2, 132, 199)
# Cyan in crest: RGB(56, 189, 248)
# Glint in top highlights: RGB(255, 255, 255)

r_out = (12.0 * (1.0 - glint) + 245.0 * glint) * fluid + 255.0 * (1.0 - fluid)
g_out = (95.0 * (1.0 - glint) + 250.0 * glint) * fluid + 255.0 * (1.0 - fluid)
b_out = (185.0 * (1.0 - glint) + 255.0 * glint) * fluid + 255.0 * (1.0 - fluid)

# Vertical smooth organic fade (no hard line at bottom)
fade = np.clip((H - y_grid) / float(H * 0.45), 0.0, 1.0) ** 1.3
alpha = np.clip(fluid * 240.0 * fade, 0.0, 255.0)

# Build RGBA array
rgba = np.zeros((H, W, 4), dtype=np.uint8)
rgba[:, :, 0] = np.clip(r_out, 0, 255).astype(np.uint8)
rgba[:, :, 1] = np.clip(g_out, 0, 255).astype(np.uint8)
rgba[:, :, 2] = np.clip(b_out, 0, 255).astype(np.uint8)
rgba[:, :, 3] = alpha.astype(np.uint8)

img = Image.fromarray(rgba, 'RGBA')
img = img.filter(ImageFilter.SMOOTH_MORE)
img.save('public/images/header_liquid_4k_ultra.png', 'PNG')
print('Perfect 3840x360 4K 3D Liquid Wave Header created!')
