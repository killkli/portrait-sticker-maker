# 🎭 Portrait Sticker Maker (人像照片轉聊天表情貼圖 - Agent 原生版)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Dependency: Zero External Backend](https://img.shields.io/badge/Dependencies-Zero_External-brightgreen.svg)](#)
[![Output: Multi--Platform](https://img.shields.io/badge/Platforms-LINE_%7C_Telegram_%7C_Discord_%7C_WeChat-purple.svg)](#)

使用 Agent 內建的原生多模態生圖工具（`generate_image`）與本地 Sprite 後製引擎，將真實人像照片直接轉換為高品質、神韻精準、風格統一的整組聊天軟體表情貼圖包（支援 **LINE、Telegram、Discord、微信、WhatsApp**）。

**💡 完全免 GPU 伺服器、免 Google Colab、零外部算力依賴，對話中即可直接生成與導出！**

---

## ✨ 核心特色 (Key Features)

- **🚀 零外部算力依賴**：完全無需連接 Google Colab，不需設定任何雲端 GPU 環境或負擔運算配額，直接調用系統原生 `generate_image`。
- **🎯 肖像特徵與神韻鎖定**：透過原生多模態圖像理解，精準錨定用戶照片中的黑框眼鏡、髮型輪廓、表情神態與個人特質。
- **⚡ 3x3 九宮格單次生成策略**：單次生成包含 9 種不同聊天表情的洋紅底（`#FF00FF`）九宮格圖，確保整套貼圖角色造型、比例與色彩 100% 統一。
- **✂️ 專業實體貼圖白邊（Die-Cut Border）**：自動去除洋紅背景，沿著人物邊緣自動生成 8~12px 平滑純白裁切線與立體微投影，在深色或淺色聊天視窗皆具備極佳辨識度。
- **📦 全平台官方規格自動打包**：
  - **LINE 貼圖**：符合最大 370×320 px 規範，包含必備的 `main.png`（240×240 封面大圖）與 `tab.png`（96×74 聊天分頁小圖）。
  - **Telegram / Discord / WhatsApp**：512×512 px 高解析度透明圖檔。
  - **微信表情包**：240×240 px 輕量級透明 PNG。
  - **超清典藏母檔**：1024×1024 px 原生母檔。
- **🖼️ 全套展示海報自動生成**：自動合成為精美的整套貼圖展示海報（Montage Showcase）。

---

## 🎨 支援 7 大風格庫 (Supported Styles)

1. **`pop_mart_3d` (3D 盲盒公仔風)**：泡泡瑪特潮玩質感、軟陶黏土溫潤光澤、微縮 3D 黑框眼鏡、柔光箱立體棚拍感。
2. **`fauvism` (野獸派狂野風格)**：馬蒂斯與德蘭式的大膽撞色（朱紅、鈷藍、鎘黃、翠綠）、狂放藝術筆觸、張力十足。
3. **`chibi` (日系 Q 版萌系)**：2 頭身大頭小身、水汪汪大眼、粉嫩腮紅，經典可愛動漫周邊感（類似卡娜赫拉）。
4. **`retro_comic` (美式復古漫畫/普普風)**：粗黑輪廓墨線、班戴網點陰影、高對比原色、美漫狀聲詞對話框。
5. **`pixel_art` (經典 2D 像素風)**：16-bit 點陣像素表情包、懷舊 JRPG 遊戲頭像與表情符號。
6. **`meme` (搞笑魔性顏藝)**：誇張五官變形、爆笑肢體動作、草根塗鴉線條、LINE 爆笑迷因感。
7. **`korean_pastel` (韓系簡約手繪)**：簡約流暢鋼筆線條、低飽和馬卡龍粉彩色調、溫柔文青插畫。

---

## 📋 常用 9 宮格表情庫 (Expression Matrix)

| 編號 | 常用主題 | 肢體動作與視覺符號 | 推薦文字標籤 (繁中 / 英文) |
|:---:|:---|:---|:---:|
| 1 | **打招呼** | 燦爛微笑、熱情揮手、頭頂跳出音符 | 嗨！ / HELLO! |
| 2 | **讚 / OK** | 雙手或單手豎大拇指、自信眨眼、閃光 | OK啦！ / OK! |
| 3 | **謝謝** | 雙手合十微鞠躬、星星眼、小花圍繞 | 謝謝泥 / THANKS! |
| 4 | **大笑** | 捧腹大笑、眼角笑出淚珠、張嘴大笑 | 笑死！ / LOL! |
| 5 | **哭哭** | 瀑布狀眼淚噴發、咬手帕、抱頭崩潰 | 嗚嗚嗚 / NOOO! |
| 6 | **生氣** | 額頭爆青筋、面紅耳赤、雙耳噴蒸氣 | 氣炸！ / ANGRY! |
| 7 | **愛心** | 手比手指愛心、抱著大愛心、臉頰泛紅 | 愛你唷 / LOVE YOU |
| 8 | **晚安** | 裹在被子裡打瞌睡、鼻涕/口水泡泡、Zzz | 晚安安 / GOODNIGHT |
| 9 | **問號** | 歪頭抓抓頭髮、頭頂浮現大問號「???」 | 蛤？？ / WHAT?! |

---

## 🚀 執行流程 (Workflow)

### 1. 產生最佳化 Prompt
執行內建的 `prompt_builder.py` 取得針對該風格與九宮格佈局最佳化的生圖 Prompt：
```bash
python scripts/prompt_builder.py --style pop_mart_3d --lang zh-TW
```

### 2. 調用 Agent 原生 `generate_image` 工具
Agent 在對話中呼叫：
```json
{
  "AspectRatio": "1:1",
  "ImageName": "sticker_sheet_3x3",
  "ImagePaths": ["/path/to/photo.jpg"],
  "Prompt": "<generated_prompt>"
}
```

### 3. 本地端一鍵切分、去背與打包
生圖完成後，執行本地 `sticker_processor.py`：
```bash
python scripts/sticker_processor.py slice \
  --sheet "/path/to/generated_sheet.png" \
  --rows 3 --cols 3 \
  --output-dir "./output_stickers" \
  --border-width 10 \
  --export-packages \
  --montage \
  --labels "嗨！" "OK啦！" "謝謝泥" "笑死！" "嗚嗚嗚" "氣炸！" "愛你唷" "晚安安" "蛤？？"
```

---

## 📁 輸出目錄結構 (Output Structure)

```
output_stickers/
├── raw_sliced/                     # 9 張透明底、帶實體白邊的獨立貼圖 PNG
│   ├── 01_嗨.png
│   └── ...
├── packages/
│   ├── line_370x320/              # LINE 貼圖官方標準規格 (含 main.png 封面與 tab.png 分頁圖)
│   ├── telegram_discord_512x512/  # Telegram / Discord / WhatsApp 512x512 高清貼圖
│   ├── wechat_240x240/            # 微信表情包規格
│   └── master_hd_1024x1024/       # 1024x1024 超清母檔
└── sticker_montage_preview.png     # 整套 9 入貼圖展示預覽海報
```

---

## 📄 開源授權 (License)

本專案採用 [MIT License](LICENSE) 授權。
