import numpy as np
import cv2
from PIL import Image, ImageFilter, ImageEnhance

W, H = 2560, 1440

y_coords, x_coords = np.mgrid[0:H, 0:W].astype(np.float32)

# 1. Multi-frequency organic water caustic wave simulation
# Voronoi / Perlin inspired caustic light net
t_x = x_coords / float(W) * 14.0
t_y = y_coords / float(H) * 8.0

# Layered sinusoidal caustic wave intersections
wave1 = np.sin(t_x * 1.5 + np.cos(t_y * 1.2)) * 0.5 + 0.5
wave2 = np.cos(t_y * 1.7 + np.sin(t_x * 1.1)) * 0.5 + 0.5
wave3 = np.sin((t_x + t_y) * 1.8 + np.sin(t_x * 0.8)) * 0.5 + 0.5
wave4 = np.cos((t_x * 1.3 - t_y * 1.4) + np.cos(t_y * 0.9)) * 0.5 + 0.5

# Caustic web: where waves constructively interfere
caustics = ((wave1 * wave2) ** 2.2 + (wave3 * wave4) ** 2.2) * 0.5

# 2. Add realistic concentric water ripples in corners/accents
# Ripple 1: Top-Right (x=1900, y=250)
r1 = np.sqrt((x_coords - 1900)**2 + ((y_coords - 250) * 1.4)**2)
ripple1 = np.sin(r1 * 0.04) * np.exp(-r1 * 0.0025) * np.clip(1.0 - r1 / 1000.0, 0, 1)

# Ripple 2: Bottom-Left (x=500, y=1100)
r2 = np.sqrt((x_coords - 500)**2 + ((y_coords - 1100) * 1.3)**2)
ripple2 = np.sin(r2 * 0.035) * np.exp(-r2 * 0.002) * np.clip(1.0 - r2 / 1100.0, 0, 1)

# Combined fluid energy
fluid_field = np.clip(caustics * 0.65 + ripple1 * 0.45 + ripple2 * 0.4, 0, 1)

# 3. Soft blur for liquid flow smoothness
fluid_blur = cv2.GaussianBlur(fluid_field, (25, 25), 0)

# 4. Colorization: Pure Water Cyan / Royal Blue on White
# Base: White (255, 255, 255)
# Water highlights: Light Sky Blue (224, 242, 254) -> Soft Azure (186, 230, 253) -> Light Blue (147, 197, 253)
r_chan = 255.0 - fluid_blur * 65.0   # 190..255
g_chan = 255.0 - fluid_blur * 30.0   # 225..255
b_chan = 255.0 - fluid_blur * 5.0    # 250..255

# Alpha channel: soft transparency so it can be overlaid anywhere seamlessly
alpha_chan = np.clip(fluid_blur * 210.0, 0.0, 255.0)

rgba = np.zeros((H, W, 4), dtype=np.uint8)
rgba[:, :, 0] = np.clip(r_chan, 0, 255).astype(np.uint8)
rgba[:, :, 1] = np.clip(g_chan, 0, 255).astype(np.uint8)
rgba[:, :, 2] = np.clip(b_chan, 0, 255).astype(np.uint8)
rgba[:, :, 3] = alpha_chan.astype(np.uint8)

img = Image.fromarray(rgba, 'RGBA')
img.save('public/images/bg_liquid_caustics_4k.png', 'PNG', optimize=True)
print('Generated public/images/bg_liquid_caustics_4k.png successfully! Size:', img.size)

# Also create a dedicated top hero ripple texture
H_top = 800
y_t, x_t = np.mgrid[0:H_top, 0:W].astype(np.float32)
r_top = np.sqrt((x_t - 1800)**2 + ((y_t - 200) * 1.5)**2)
rip_top = np.sin(r_top * 0.045) * np.exp(-r_top * 0.003) * np.clip(1.0 - r_top / 900.0, 0, 1)
rip_top_blur = cv2.GaussianBlur(rip_top, (15, 15), 0)

alpha_top = np.clip(rip_top_blur * 180.0 * ((H_top - y_t) / float(H_top)), 0, 255)
rgba_top = np.zeros((H_top, W, 4), dtype=np.uint8)
rgba_top[:, :, 0] = (255 - rip_top_blur * 55).astype(np.uint8)
rgba_top[:, :, 1] = (255 - rip_top_blur * 25).astype(np.uint8)
rgba_top[:, :, 2] = 255
rgba_top[:, :, 3] = alpha_top.astype(np.uint8)

img_top = Image.fromarray(rgba_top, 'RGBA')
img_top.save('public/images/bg_water_ripple_top.png', 'PNG', optimize=True)
print('Generated public/images/bg_water_ripple_top.png successfully!')

