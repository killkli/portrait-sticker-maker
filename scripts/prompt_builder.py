#!/usr/bin/env python3
"""
Prompt Builder for Native Agent Portrait Sticker Maker.
Generates optimized prompts for the agent's built-in generate_image tool.
"""

from __future__ import annotations

import argparse
from typing import Dict, List

STYLES: Dict[str, Dict[str, str]] = {
    "pop_mart_3d": {
        "name": "3D 盲盒公仔 (Pop Mart / Clay 3D)",
        "prefix": (
            "Trendy 3D vinyl toy figurine chat sticker illustration, Pop Mart style, collectible designer art toy, "
            "faithfully stylized based on the person in reference photo. "
            "Chibi cute miniature toy proportions, smooth matte vinyl and polymer clay texture, warm studio softbox lighting, "
            "clean rim light highlights, glossy reflective eyes, sculpted hair. "
        ),
    },
    "fauvism": {
        "name": "野獸派狂野風格 (Fauvism Wild Expression)",
        "prefix": (
            "Wild Fauvism modern chat sticker illustration, inspired by Henri Matisse and André Derain. "
            "Bold, expressive, wild, and spontaneous brushstrokes, vibrant saturated clashing colors "
            "(fiery vermilion red, bright cadmium yellow, electric cobalt blue, wild emerald green, deep violet contours). "
            "Artistic, highly expressive character caricature capturing the recognizable facial features of the person in reference photo. "
            "Dynamic thick artistic outlines, raw painterly brush textures, energetic and passionate emotional expression, modern pop-art chat sticker aesthetics. "
        ),
    },
    "chibi": {
        "name": "日系 Q 版萌系 (Chibi Anime)",
        "prefix": (
            "Ultra-cute 2D Chibi anime character sticker design, "
            "based on the facial features, hairstyle, and likeness of the person in reference photo. "
            "2-head-tall proportions, adorable oversized head, cute expressive anime eyes, soft rosy blush, "
            "clean vector-like outlines, vibrant cell shading, die-cut sticker aesthetics. "
        ),
    },
    "retro_comic": {
        "name": "美式復古漫畫/普普風 (Retro Comic / Pop-Art)",
        "prefix": (
            "Vintage American comic book sticker illustration, 1960s pop-art Lichtenstein style, "
            "stylized portrait based on the person in reference photo. "
            "Heavy bold ink outlines, halftone Ben-Day dots shading, bold primary color palette, "
            "dynamic retro comic speech bubbles, sticker graphic aesthetics. "
        ),
    },
    "pixel_art": {
        "name": "經典 2D 像素風 (16-bit Pixel Art Sprite)",
        "prefix": (
            "Nostalgic 16-bit pixel art character sprite sticker, retro JRPG chat emote style, "
            "capturing key recognizable features from the person in reference photo. "
            "Crisp chunky pixel clusters, vibrant retro color palette, expressive retro arcade emote poses, "
            "game UI sticker aesthetics. "
        ),
    },
    "meme": {
        "name": "搞笑魔性顏藝 (Meme / Dramatic Expression)",
        "prefix": (
            "Humorous, funny exaggerated cartoon meme sticker, LINE sticker meme culture style, "
            "caricature based on the person in reference photo. "
            "Hilarious exaggerated facial expressions, funny dynamic body comedy gestures, "
            "hand-drawn doodle lines, playful anime reaction face sticker aesthetics. "
        ),
    },
    "korean_pastel": {
        "name": "韓系簡約手繪 (Korean Line & Pastel)",
        "prefix": (
            "Minimalist Korean warm line-drawing sticker, cozy lifestyle aesthetic, "
            "delicate stylized illustration of the person in reference photo. "
            "Smooth continuous pen lines, soothing muted pastel watercolor fills, charming gentle vibe, "
            "aesthetic daily chat sticker look. "
        ),
    },
}

EXPRESSIONS_3X3: List[Dict[str, str]] = [
    {
        "id": "hello",
        "action": "waving cheerfully with a warm happy smile, welcoming gesture",
        "text_zh": "嗨！",
        "text_en": "HELLO!",
    },
    {
        "id": "ok_thumbs_up",
        "action": "giving confident double thumbs-up with an encouraging wink",
        "text_zh": "OK啦！",
        "text_en": "OK!",
    },
    {
        "id": "thank_you",
        "action": "clasping hands together in sincere gratitude with sparkling eyes",
        "text_zh": "謝謝泥",
        "text_en": "THANKS!",
    },
    {
        "id": "lol_laugh",
        "action": "holding belly laughing out loud with tears of joy, wide open-mouth grin",
        "text_zh": "笑死！",
        "text_en": "LOL!",
    },
    {
        "id": "crying_sad",
        "action": "comical waterfall streams of tears flowing from eyes, sobbing with pouty mouth",
        "text_zh": "嗚嗚嗚",
        "text_en": "NOOO!",
    },
    {
        "id": "angry_rage",
        "action": "fuming with anger, steam blowing from ears, red flushed face with comical rage vein",
        "text_zh": "氣炸！",
        "text_en": "ANGRY!",
    },
    {
        "id": "love_heart",
        "action": "blowing sweet finger-hearts or hugging a giant glowing red heart, blushing cheeks",
        "text_zh": "愛你唷",
        "text_en": "LOVE YOU",
    },
    {
        "id": "sleepy_goodnight",
        "action": "wrapped in a cozy blanket with sleepy eyes, drooling slightly, floating 'Zzz' bubbles",
        "text_zh": "晚安安",
        "text_en": "GOODNIGHT",
    },
    {
        "id": "confused_question",
        "action": "tilting head quizzically scratching head with giant floating question marks '???'",
        "text_zh": "蛤？？",
        "text_en": "WHAT?!",
    },
]


def build_sticker_prompt(
    style_key: str = "pop_mart_3d",
    layout: str = "3x3",
    lang: str = "zh-TW",
    custom_desc: str = "",
) -> str:
    style_info = STYLES.get(style_key, STYLES["pop_mart_3d"])
    expressions = EXPRESSIONS_3X3 if layout == "3x3" else EXPRESSIONS_3X3[:8]
    rows = 3 if layout == "3x3" else 2
    cols = 3 if layout == "3x3" else 4
    total = rows * cols

    items = []
    for idx, expr in enumerate(expressions):
        text_badge = ""
        if lang == "zh-TW" and expr.get("text_zh"):
            text_badge = f' with cute sticker text "{expr["text_zh"]}"'
        elif lang == "en" and expr.get("text_en"):
            text_badge = f' with cute sticker text "{expr["text_en"]}"'
        items.append(f"Cell {idx+1}: {expr['action']}{text_badge}")

    actions_joined = "; ".join(items)

    prompt = (
        f"{style_info['prefix']}"
        f"{custom_desc + ' ' if custom_desc else ''}"
        f"A multi-panel sticker sheet containing EXACTLY {total} distinct emoji stickers arranged in a {rows}x{cols} grid ({rows} rows, {cols} columns). "
        f"The subject must maintain the identical character identity and likeness of the person in the reference photo across every cell. "
        f"Specific expressions for each cell in order: {actions_joined}. "
        f"ABSOLUTE RULES: "
        f"1. SOLID FLAT MAGENTA (#FF00FF) background everywhere between cells, NO gradients, NO shadows on background. "
        f"2. Each sticker character is neatly centered inside its grid cell with generous margin around it. "
        f"3. No body parts or text crossing cell boundaries. "
        f"4. Distinct, high-contrast, cute sticker look ready for chat apps."
    )
    return prompt


def main():
    parser = argparse.ArgumentParser(description="Build prompt for agent's native generate_image tool.")
    parser.add_argument(
        "--style",
        type=str,
        default="pop_mart_3d",
        choices=list(STYLES.keys()),
        help="Sticker art style.",
    )
    parser.add_argument("--layout", type=str, default="3x3", choices=["3x3", "2x4"], help="Grid layout.")
    parser.add_argument("--lang", type=str, default="zh-TW", choices=["zh-TW", "en", "none"], help="Text label language.")
    parser.add_argument("--custom-desc", type=str, default="", help="Custom details (e.g. black glasses, short hair).")

    args = parser.parse_args()
    prompt = build_sticker_prompt(args.style, args.layout, args.lang, args.custom_desc)
    print(prompt)


if __name__ == "__main__":
    main()
