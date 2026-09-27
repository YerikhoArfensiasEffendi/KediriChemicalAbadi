import os
import cv2
import numpy as np
import qrcode
from PIL import Image, ImageDraw, ImageFont

def create_kca_qrcode():
    target_url = "https://kedirichemical.id"
    output_dir = "QR_CODE_KCA"
    public_img_dir = "public/images"
    artifact_dir = "/Users/arthur/.gemini/antigravity/brain/894a23c3-0b06-42cb-8ce0-b7c760180536"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(public_img_dir, exist_ok=True)

    # 1. Load KCA Logo
    logo_path = "public/images/kca_logo.png"
    if not os.path.exists(logo_path):
        raise FileNotFoundError(f"Logo not found at {logo_path}")

    logo_raw = Image.open(logo_path).convert("RGBA")

    # Trim transparency
    arr = np.array(logo_raw)
    y_indices, x_indices = np.where(arr[:, :, 3] > 20)
    x_min, x_max = x_indices.min(), x_indices.max()
    y_min, y_max = y_indices.min(), y_indices.max()
    logo_trimmed = logo_raw.crop((x_min, y_min, x_max + 1, y_max + 1))

    # Also extract emblem only (top K mark, rows before gap ~530)
    alpha_top = arr[:530, :, 3]
    y_t, x_t = np.where(alpha_top > 20)
    emblem_trimmed = logo_raw.crop((x_t.min(), y_t.min(), x_t.max() + 1, y_t.max() + 1))

    # Helper function to build standalone QR code
    def build_qr(logo_to_use, fill_color, out_filename, badge_shape="rounded_rect", scale_factor=0.25):
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=40,
            border=4
        )
        qr.add_data(target_url)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color=fill_color, back_color="white").convert("RGBA")
        qr_w, qr_h = qr_img.size

        # Badge dimensions (calculated to maintain < 27% QR area for reliable H-level ECC)
        badge_w = int(qr_w * scale_factor)
        badge_h = badge_w if badge_shape == "square" else int(badge_w * (logo_to_use.height / logo_to_use.width) * 1.08)
        badge_h = max(badge_h, int(qr_w * 0.20))
        badge_h = min(badge_h, int(qr_w * 0.27))
        badge_w = min(badge_w, int(qr_w * 0.27))

        badge_x = (qr_w - badge_w) // 2
        badge_y = (qr_h - badge_h) // 2

        overlay = Image.new("RGBA", (qr_w, qr_h), (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)

        # Smooth white badge
        corner_radius = int(badge_w * 0.16)
        draw.rounded_rectangle(
            [badge_x, badge_y, badge_x + badge_w, badge_y + badge_h],
            radius=corner_radius,
            fill=(255, 255, 255, 255),
            outline=(226, 232, 240, 255),
            width=int(qr_w * 0.003)
        )

        pad_x = int(badge_w * 0.12)
        pad_y = int(badge_h * 0.12)
        target_logo_w = badge_w - (pad_x * 2)
        target_logo_h = badge_h - (pad_y * 2)

        logo_ratio = min(target_logo_w / logo_to_use.width, target_logo_h / logo_to_use.height)
        new_logo_w = int(logo_to_use.width * logo_ratio)
        new_logo_h = int(logo_to_use.height * logo_ratio)

        logo_resized = logo_to_use.resize((new_logo_w, new_logo_h), Image.Resampling.LANCZOS)
        logo_pos_x = badge_x + (badge_w - new_logo_w) // 2
        logo_pos_y = badge_y + (badge_h - new_logo_h) // 2

        qr_img = Image.alpha_composite(qr_img, overlay)
        qr_img.paste(logo_resized, (logo_pos_x, logo_pos_y), logo_resized)

        final_rgb = qr_img.convert("RGB")
        out_path = os.path.join(output_dir, out_filename)
        final_rgb.save(out_path, "PNG", dpi=(300, 300))
        print(f"Saved: {out_path} ({final_rgb.size[0]}x{final_rgb.size[1]} px, 300 DPI)")

        # Verify decoding
        arr_test = np.array(final_rgb)
        detector = cv2.QRCodeDetector()
        decoded_val, _, _ = detector.detectAndDecode(arr_test)
        status = "PASSED (100% Scannable)" if decoded_val == target_url else f"FAILED (Got: {decoded_val})"
        print(f"  -> Scanner Verification: {status}")

        return final_rgb, out_path

    # Generate Variant 1: Full KCA Logo (Emblem + Text), Pure Black QR
    img_full, path_full = build_qr(logo_trimmed, "black", "qrcode_kca_full_logo.png", badge_shape="rounded_rect", scale_factor=0.26)

    # Generate Variant 2: KCA 'K' Emblem Mark, Pure Black QR (Ultra-scannable & iconic)
    img_emblem, path_emblem = build_qr(emblem_trimmed, "black", "qrcode_kca_emblem.png", badge_shape="rounded_rect", scale_factor=0.23)

    # Generate Variant 3: Corporate Deep Navy Blue QR (#0A192F) with KCA Full Logo
    img_navy, path_navy = build_qr(logo_trimmed, "#0A192F", "qrcode_kca_navy_logo.png", badge_shape="rounded_rect", scale_factor=0.26)

    # Copy primary QR to public/images for website usage
    img_full.save(os.path.join(public_img_dir, "qrcode_kedirichemical.png"), "PNG", dpi=(300, 300))
    print(f"Copied primary QR to public/images/qrcode_kedirichemical.png")

    # Generate Variant 4: Ready-to-Print Corporate Display Standee / Flyer (2400 x 3300 px, 300 DPI)
    card_w, card_h = 2400, 3300
    card = Image.new("RGB", (card_w, card_h), (255, 255, 255))
    draw = ImageDraw.Draw(card)

    # Outer decorative card border
    draw.rounded_rectangle(
        [60, 60, card_w - 60, card_h - 60],
        radius=40,
        fill=(255, 255, 255),
        outline=(203, 213, 225),
        width=5
    )

    # Load system font
    font_path = "/System/Library/Fonts/HelveticaNeue.ttc"
    try:
        font_title = ImageFont.truetype(font_path, 66, index=0)
        font_sub = ImageFont.truetype(font_path, 36, index=0)
        font_url = ImageFont.truetype(font_path, 60, index=0)
        font_desc = ImageFont.truetype(font_path, 34, index=0)
        font_specs = ImageFont.truetype(font_path, 30, index=0)
    except Exception:
        font_title = font_sub = font_url = font_desc = font_specs = ImageFont.load_default()

    # Top Header Logo
    header_logo_w = 750
    header_logo_h = int(header_logo_w * (logo_trimmed.height / logo_trimmed.width))
    header_logo_resized = logo_trimmed.resize((header_logo_w, header_logo_h), Image.Resampling.LANCZOS)
    card.paste(header_logo_resized, ((card_w - header_logo_w) // 2, 160), header_logo_resized)

    # Top Subtitle (Pure Black as per kca_standards.md)
    sub_text = "PUSAT MANUFAKTUR & FORMULASI KIMIA INDUSTRI • EST. 2004"
    draw.text((card_w // 2, 180 + header_logo_h), sub_text, fill=(0, 0, 0), font=font_sub, anchor="mm")

    # Divider line
    div_y = 240 + header_logo_h
    draw.line([250, div_y, card_w - 250, div_y], fill=(226, 232, 240), width=3)

    # QR Code in Center
    qr_display_size = 1450
    qr_resized = img_full.resize((qr_display_size, qr_display_size), Image.Resampling.LANCZOS)
    qr_top_y = div_y + 60
    card.paste(qr_resized, ((card_w - qr_display_size) // 2, qr_top_y))

    # Bottom Content
    content_y = qr_top_y + qr_display_size + 70

    # Title Call To Action (Pure Black #000000)
    cta_title = "PINDAI UNTUK MENGAKSES KATALOG & KALKULATOR DOSIS"
    draw.text((card_w // 2, content_y), cta_title, fill=(0, 0, 0), font=font_title, anchor="mm")

    # Website URL Badge (Royal Blue fill or pure black text)
    url_box_y = content_y + 75
    url_w, url_h = 1000, 100
    draw.rounded_rectangle(
        [(card_w - url_w) // 2, url_box_y, (card_w + url_w) // 2, url_box_y + url_h],
        radius=20,
        fill=(240, 249, 255),
        outline=(15, 88, 168),
        width=3
    )
    draw.text((card_w // 2, url_box_y + (url_h // 2)), "https://kedirichemical.id", fill=(15, 88, 168), font=font_url, anchor="mm")

    # Instructional Text (Pure Black #000000)
    desc_text = "Arahkan kamera ponsel Anda ke QR code di atas untuk membuka portal resmi KCA."
    draw.text((card_w // 2, url_box_y + url_h + 60), desc_text, fill=(0, 0, 0), font=font_desc, anchor="mm")

    # Specs Footer Line (Pure Black #000000)
    specs_text = "ISO 9001:2015 SISTEM MUTU  •  100% BEBAS FOSFAT (STPP-FREE)  •  KAPASITAS 500+ TON/BULAN"
    draw.text((card_w // 2, card_h - 150), specs_text, fill=(0, 0, 0), font=font_specs, anchor="mm")

    card_out_path = os.path.join(output_dir, "kca_qrcode_display_card.png")
    card.save(card_out_path, "PNG", dpi=(300, 300))
    print(f"Saved refined corporate display card: {card_out_path}")

    # Copy files to artifacts directory
    import shutil
    for fname in ["qrcode_kca_full_logo.png", "qrcode_kca_emblem.png", "qrcode_kca_navy_logo.png", "kca_qrcode_display_card.png"]:
        src = os.path.join(output_dir, fname)
        dst = os.path.join(artifact_dir, fname)
        shutil.copy2(src, dst)
        print(f"Copied to artifact: {dst}")

if __name__ == "__main__":
    create_kca_qrcode()
