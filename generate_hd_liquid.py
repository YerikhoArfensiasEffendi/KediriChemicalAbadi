import numpy as np
import cv2
from PIL import Image, ImageFilter, ImageEnhance

W = 3840
H = 320

# Create canvas: RGBA float
img = np.zeros((H, W, 4), dtype=np.float32)

# Coordinate grids
y_coords, x_coords = np.mgrid[0:H, 0:W]

# -------------------------------------------------------------
# 1. LEFT CONCENTRIC WATER RIPPLES (Around Logo at x=160, y=80)
# -------------------------------------------------------------
cx, cy = 180.0, 75.0
dx = x_coords - cx
dy = (y_coords - cy) * 1.5  # elliptical ripple
r = np.sqrt(dx**2 + dy**2)

# Ripple wave frequencies
ripple_wave = (
    np.sin(r * 0.08) * np.exp(-r * 0.0035) * 0.5 +
    np.sin(r * 0.04 - 0.5) * np.exp(-r * 0.002) * 0.4 +
    np.sin(r * 0.12) * np.exp(-r * 0.006) * 0.25
)
ripple_mask = np.clip(1.0 - (r / 900.0), 0.0, 1.0) ** 1.5
left_ripples = ripple_wave * ripple_mask

# -------------------------------------------------------------
# 2. MAIN 3D FLUID WAVE RIBBON (Spanning Across x=0 to x=W)
# -------------------------------------------------------------
# Wave centerline path dipping across the header
t = x_coords / float(W)
wave_center_y = (
    45.0 + 
    35.0 * np.sin(t * np.pi * 2.2 - 0.3) +
    20.0 * np.sin(t * np.pi * 4.5 + 1.0) +
    15.0 * np.cos(t * np.pi * 1.2)
)

# Distance to wave center
dist_to_wave = y_coords - wave_center_y
wave_thickness = 40.0 + 25.0 * np.sin(t * np.pi * 3.0) + 15.0 * t

# Main wave body profile
wave_body = np.exp(-((dist_to_wave / wave_thickness) ** 2))

# Specular caustic crest highlights on the top curve of the wave
crest_highlight = np.exp(-(((dist_to_wave + 12.0) / 10.0) ** 2)) * (0.6 + 0.4 * np.sin(t * 15.0))

# Secondary wave ribbon overlapping for 3D depth
wave2_center_y = (
    30.0 + 
    45.0 * np.sin(t * np.pi * 2.0 + 0.8) +
    18.0 * np.cos(t * np.pi * 3.8)
)
dist_to_wave2 = y_coords - wave2_center_y
wave2_body = np.exp(-((dist_to_wave2 / 32.0) ** 2)) * 0.7
crest2_highlight = np.exp(-(((dist_to_wave2 + 8.0) / 8.0) ** 2)) * 0.5

# -------------------------------------------------------------
# 3. WATER SPLASH DROPLETS & CAUSTIC PARTICLES
# -------------------------------------------------------------
np.random.seed(42)
num_droplets = 90
droplets_field = np.zeros((H, W), dtype=np.float32)

for _ in range(num_droplets):
    # Scatter along the wave trajectory
    d_x = np.random.uniform(200, W - 100)
    d_t = d_x / float(W)
    base_y = 45.0 + 35.0 * np.sin(d_t * np.pi * 2.2 - 0.3) + 20.0 * np.sin(d_t * np.pi * 4.5 + 1.0)
    d_y = base_y + np.random.uniform(-40, 65)
    
    radius = np.random.uniform(3.0, 14.0)
    brightness = np.random.uniform(0.4, 0.95)
    
    if 0 <= d_y < H:
        d_dx = x_coords - d_x
        d_dy = y_coords - d_y
        d_dist = np.sqrt(d_dx**2 + d_dy**2)
        drop = np.exp(-((d_dist / radius) ** 2)) * brightness
        # Add tiny specular gleam on each droplet
        gleam = np.exp(-(((d_dx + radius * 0.3)**2 + (d_dy + radius * 0.3)**2) / (radius * 0.35)**2)) * 0.9
        droplets_field = np.maximum(droplets_field, drop + gleam)

# -------------------------------------------------------------
# 4. COMPOSITING LIQUID COLORS & SHADERS (Ultra HD Royal/Aqua)
# -------------------------------------------------------------
# Base water color palettes (RGB 0..255)
# Deep Royal Blue: (15, 88, 168)
# Vibrant Sky Aqua: (2, 132, 199)
# Crystal Light Cyan: (56, 189, 248)
# Pure Glint White: (255, 255, 255)

# Total fluid intensity
fluid_intensity = np.clip(
    wave_body * 0.75 + 
    wave2_body * 0.5 + 
    left_ripples * 0.55 + 
    droplets_field * 0.8,
    0.0, 1.0
)

# Total highlight intensity
highlight_intensity = np.clip(
    crest_highlight * 0.85 + 
    crest2_highlight * 0.6 + 
    np.clip(left_ripples, 0, 1) * 0.4 + 
    droplets_field * 0.6,
    0.0, 1.0
)

# Color interpolation
r_channel = (15.0 * (1.0 - highlight_intensity) + 245.0 * highlight_intensity) * fluid_intensity + 255.0 * (1.0 - fluid_intensity)
g_channel = (110.0 * (1.0 - highlight_intensity) + 250.0 * highlight_intensity) * fluid_intensity + 255.0 * (1.0 - fluid_intensity)
b_channel = (195.0 * (1.0 - highlight_intensity) + 255.0 * highlight_intensity) * fluid_intensity + 255.0 * (1.0 - fluid_intensity)

# Calculate Alpha: smooth organic fade at the bottom (no hard box line)
vertical_fade = np.clip((H - y_coords) / float(H * 0.4), 0.0, 1.0)
alpha_channel = np.clip(fluid_intensity * 230.0 * vertical_fade, 0.0, 255.0)

# Build RGBA
img[:, :, 0] = np.clip(r_channel, 0, 255)
img[:, :, 1] = np.clip(g_channel, 0, 255)
img[:, :, 2] = np.clip(b_channel, 0, 255)
img[:, :, 3] = alpha_channel

# Convert to uint8 PIL Image
out = Image.fromarray(img.astype(np.uint8), 'RGBA')

# Apply smooth anti-aliasing filter
out = out.filter(ImageFilter.SMOOTH_MORE)

# Save Master HD 4K Asset
out.save('public/images/header_liquid_4k_master.png', 'PNG')
print('4K Master 3840x320 3D Liquid Wave Header created successfully!')
