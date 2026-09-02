from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def create_icon(base_size=1024, bg_color="#FF5722", text="AB", font_path=None):
    image = Image.new("RGBA", (base_size, base_size), bg_color)
    draw = ImageDraw.Draw(image)
    font_size = max(1, base_size // 3)
    font = (
        ImageFont.truetype(font_path, font_size)
        if font_path
        else ImageFont.load_default()
    )
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    draw.text(
        ((base_size - (right - left)) / 2 - left,
         (base_size - (bottom - top)) / 2 - top),
        text,
        fill="white",
        font=font,
    )
    image.save(Path(__file__).with_name("icon.png"))
    return image


if __name__ == "__main__":
    create_icon(
        base_size=1024,
        bg_color="#FF5722",
        text="AB",
        font_path=None,  # You can specify a .ttf font file path here
    )
