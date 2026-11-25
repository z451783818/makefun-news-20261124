#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news summary image (1024x1024 PNG).

One file, no network, no randomness: running it twice writes byte-identical
output. Layout: a navy header with the date, one wide lead card, then a
2x2 grid of four more stories. Each story has a number, a big title, a bold
accent stat line, one short body line, and a small geometric icon drawn with
plain Pillow shapes.
"""

import math

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (247, 243, 232)      # warm off-white background
NAVY = (14, 27, 51)         # header band
GOLD = (212, 160, 44)       # date line + rules
INK = (24, 24, 24)          # main text
CARD = (255, 255, 255)      # card fill
GREY = (90, 90, 90)         # footer text

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, s, f):
    return draw.textlength(s, font=f)


def rounded_card(draw, box, fill, outline, width):
    draw.rounded_rectangle(box, radius=16, fill=fill, outline=outline,
                           width=width)


def number_badge(draw, cx, cy, n, color):
    r = 26
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    f = font(FONT_BOLD, 30)
    draw.text((cx, cy), str(n), font=f, fill=(255, 255, 255), anchor="mm")


def chip(draw, x, y, label, color):
    """Filled pill with white bold text; returns its width."""
    f = font(FONT_BOLD, 22)
    w = int(text_w(draw, label, f)) + 30
    h = 34
    draw.rounded_rectangle([x, y, x + w, y + h], radius=17, fill=color)
    draw.text((x + 15, y + h // 2), label, font=f, fill=(255, 255, 255),
              anchor="lm")
    return w


def icon_tower(draw, x, y, color):
    # A tall tower: shaft, spire, and a small drone dot above.
    draw.rectangle([x + 14, y + 22, x + 34, y + 78], fill=color)
    draw.polygon([(x + 24, y), (x + 14, y + 24), (x + 34, y + 24)],
                 fill=color)
    draw.ellipse([x + 56, y + 8, x + 72, y + 24], fill=color)
    draw.line([x + 50, y + 16, x + 78, y + 16], fill=color, width=3)


def icon_chart_down(draw, x, y, color):
    # Axes and a falling line with an arrowhead.
    draw.line([x + 6, y + 70, x + 6, y + 10], fill=color, width=4)
    draw.line([x + 6, y + 70, x + 76, y + 70], fill=color, width=4)
    pts = [(x + 12, y + 18), (x + 30, y + 30), (x + 48, y + 28),
           (x + 66, y + 56)]
    draw.line(pts, fill=color, width=5, joint="curve")
    draw.polygon([(x + 66, y + 56), (x + 52, y + 52), (x + 60, y + 66)],
                 fill=color)


def icon_ship(draw, x, y, color):
    # Hull, mast and a small flag.
    draw.polygon([(x + 4, y + 48), (x + 76, y + 48), (x + 66, y + 70),
                  (x + 14, y + 70)], fill=color)
    draw.line([x + 40, y + 48, x + 40, y + 12], fill=color, width=4)
    draw.polygon([(x + 40, y + 12), (x + 62, y + 20), (x + 40, y + 28)],
                 fill=color)


def icon_blast(draw, x, y, color):
    # Eight-point starburst.
    cx, cy = x + 40, y + 40
    outer, inner = 38, 14
    pts = []
    for i in range(16):
        r = outer if i % 2 == 0 else inner
        a = 3.14159265 * i / 8.0
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    draw.polygon(pts, fill=color)
    draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(255, 255, 255))


def icon_rocket(draw, x, y, color):
    # Body, nose cone, fins and a flame. Fits in a 70px-tall box so it
    # never reaches the card title below it.
    draw.rounded_rectangle([x + 28, y + 18, x + 52, y + 50], radius=12,
                           fill=color)
    draw.polygon([(x + 40, y + 2), (x + 28, y + 22), (x + 52, y + 22)],
                 fill=color)
    draw.polygon([(x + 28, y + 42), (x + 16, y + 60), (x + 28, y + 55)],
                 fill=color)
    draw.polygon([(x + 52, y + 42), (x + 64, y + 60), (x + 52, y + 55)],
                 fill=color)
    draw.polygon([(x + 40, y + 50), (x + 34, y + 68), (x + 46, y + 68)],
                 fill=(232, 120, 30))
    draw.ellipse([x + 34, y + 28, x + 46, y + 40], fill=(255, 255, 255))


ICONS = [icon_tower, icon_chart_down, icon_ship, icon_blast, icon_rocket]

STORIES = [
    dict(n=1, accent=(0, 110, 70), title="RIYADH TOWER HIT AGAIN",
         stat="2ND STRIKE IN A WEEK",
         body="Houthi drone hits Riyadh's tallest tower. 11 injured.",
         lead=True),
    dict(n=2, accent=(150, 40, 40), title="NVIDIA FALLS 6%",
         stat="AI RALLY FADES", body="Shares drop after the rally."),
    dict(n=3, accent=(20, 80, 160), title="HORMUZ TANKERS HIT",
         stat="STRAIT OF HORMUZ", body="Iran says mines hit tankers."),
    dict(n=4, accent=(140, 90, 10), title="ZAPORIZHZHIA STRUCK",
         stat="2 KILLED, 40+ WOUNDED", body="Strike kills 2, wounds 40+."),
    dict(n=5, accent=(0, 110, 70), title="SHENZHOU-24 TO LAUNCH",
         stat="PAKISTAN JOINS CREW",
         body="First Pakistani astronaut aboard."),
]


def draw_lead(draw, s):
    x0, y0, x1, y1 = 24, 168, 1000, 392
    accent = s["accent"]
    draw.rectangle([x0, y0, x1, y0 + 12], fill=accent)
    rounded_card(draw, [x0, y0 + 12, x1, y1], CARD, accent, 4)
    number_badge(draw, x0 + 52, y0 + 62, s["n"], accent)
    ICONS[0](draw, x1 - 120, y0 + 40, accent)
    f_title = font(FONT_BOLD, 40)
    draw.text((x0 + 28, y0 + 96), s["title"], font=f_title, fill=INK)
    chip(draw, x0 + 28, y0 + 152, s["stat"], accent)
    f_body = font(FONT_REG, 23)
    draw.text((x0 + 28, y1 - 34), s["body"], font=f_body, fill=INK)


def draw_grid_card(draw, s, x0, y0, x1, y1):
    accent = s["accent"]
    draw.rectangle([x0, y0, x1, y0 + 12], fill=accent)
    rounded_card(draw, [x0, y0 + 12, x1, y1], CARD, accent, 4)
    number_badge(draw, x0 + 50, y0 + 60, s["n"], accent)
    ICONS[s["n"] - 1](draw, x1 - 112, y0 + 28, accent)
    f_title = font(FONT_BOLD, 27)
    draw.text((x0 + 24, y0 + 100), s["title"], font=f_title, fill=INK)
    f_stat = font(FONT_BOLD, 22)
    draw.text((x0 + 24, y0 + 148), s["stat"], font=f_stat, fill=accent)
    f_body = font(FONT_REG, 22)
    draw.text((x0 + 24, y1 - 40), s["body"], font=f_body, fill=INK)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # Header band.
    draw.rectangle([0, 0, W, 150], fill=NAVY)
    f_big = font(FONT_BOLD, 66)
    draw.text((24, 18), "WORLD NEWS", font=f_big, fill=(255, 255, 255))
    f_small = font(FONT_BOLD, 26)
    draw.text((1000, 30), "5 STORIES", font=f_small, fill=(255, 255, 255),
              anchor="ra")
    draw.text((1000, 64), "ONE IMAGE", font=f_small, fill=GOLD, anchor="ra")
    f_date = font(FONT_BOLD, 32)
    draw.text((24, 100), "TUESDAY 24 NOVEMBER 2026", font=f_date, fill=GOLD)
    draw.rectangle([0, 150, W, 158], fill=GOLD)

    draw_lead(draw, STORIES[0])

    gx, gy = 24, 410
    cw, ch, gap = 479, 250, 18
    grid = STORIES[1:]
    for i, s in enumerate(grid):
        cx = gx + (i % 2) * (cw + gap)
        cy = gy + (i // 2) * (ch + gap)
        draw_grid_card(draw, s, cx, cy, cx + cw, cy + ch)

    f_foot = font(FONT_REG, 20)
    draw.text((24, 942),
              "Sources: Reuters / RTHK / SRN News, 24 Nov 2026",
              font=f_foot, fill=GREY)

    img.save("asset.png", "PNG")
    print("Wrote asset.png (1024x1024)")


if __name__ == "__main__":
    main()
