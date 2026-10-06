---
name: portrait-sticker-maker
description: 使用 Agent 原生 generate_image 工具，自動將人像照片轉換為通訊軟體專用的一整組聊天表情貼圖（LINE、Telegram、Discord、微信、WhatsApp）。無需外部 Colab 算力，直接在對話中生成與切分，具備人像特徵鎖定、多風格切換、Sprite 格狀切分、洋紅去背、實體白邊裁切線 (Die-Cut Border) 與多平台規格導出。
---

# Portrait Sticker Maker (人像照片轉聊天表情貼圖 - Agent 原生版)

本 Skill 使用 Agent **內建的原生生圖工具（`generate_image`）** 與本地 Sprite 後製引擎，將使用者提供的人像照片直接轉換為高品質、神韻精準、風格統一的整組聊天軟體表情貼圖包（支援 LINE、Telegram、Discord、微信、WhatsApp 等）。

---

## 核心優勢與特色

- **零外部依賴、免 Colab**：完全不需連接 Google Colab，不需任何外部 GPU 算力額度或環境設定，開箱即用。
- **Agent 原生多模態生成**：直接調用系統原生 `generate_image` 工具，透過 `ImagePaths` 傳入參考照片，進行強大的面部特徵錨定與風格轉譯。
- **九宮格極速生成策略**：單次生成包含 9 種不同聊天表情的洋紅底（`#FF00FF`）九宮格圖，確保整套貼圖角色造型、比例與色彩 100% 統一。
- **Sprite 級後製引擎**：內建本地 Python 腳本（`scripts/sticker_processor.py`），自動完成精確去背、實體貼圖白邊裁切線（Die-Cut Border）、立體陰影、LINE/Telegram/微信全平台標準規格導出，以及全套展示海報。

---

## 核心工作流程 (5-Stage Workflow)

```
[使用者上傳照片] ──▶ 1. 人像特徵解析 (髮型、眼鏡、服飾、表情神韻)
                         │
                         ▼
                     2. 提供風格選單 (互動引導使用者選擇)
                         │
                         ▼
                     3. 表情動作規劃 (預設 3x3 九宮格)
                         │
                         ▼
                     4. 調用 Agent 原生 `generate_image` 生圖
                         │
                         ▼
                     5. 專屬 Sprite 後製切分與貼圖包規格化
                         ├─ 洋紅自動去背 (Chroma-Key Removal)
                         ├─ 實體白邊裁切線 (Die-Cut White Border + Shadow)
                         ├─ 規格適配 (LINE 370x320, TG/Discord 512x512, WeChat 240x240)
                         └─ 全套展示海報 (Montage Showcase)
```

---

## Stage 1: 照片接收與特徵錨定

Agent 接收照片後，需先提煉使用者的**標誌性特徵錨點（Identity Anchors）**：
- **髮型與髮色**（例如：黑短髮、旁分瀏海、微捲波浪、馬尾）
- **臉部特徵**（例如：黑框眼鏡、圓框眼鏡、絡腮鬍、招牌微笑）
- **代表性氣質與穿著**（例如：休閒 Polo 衫、連帽衫、活潑逗趣眼神）

---

## Stage 2: 風格推薦與互動選擇

向使用者展示 7 大熱門貼圖風格供其挑選：

1. **✨ 3D 盲盒公仔 (`pop_mart_3d`)**：泡泡瑪特潮玩公仔、軟陶黏土溫潤光澤、微縮 3D 黑框眼鏡、柔光箱棚拍立體感。
2. **🔥 野獸派狂野風格 (`fauvism`)**：馬蒂斯與德蘭式大膽撞色（朱紅、鈷藍、鎘黃、翠綠）、狂放藝術筆觸、張力十足。
3. **🧸 日系 Q 版萌系 (`chibi`)**：大頭小身 2 頭身、水汪汪大眼、粉嫩腮紅，經典可愛動漫周邊感（類似卡娜赫拉）。
4. **💥 美式復古漫畫/普普風 (`retro_comic`)**：粗黑輪廓墨線、班戴網點陰影、高對比原色、美漫狀聲詞對話框。
5. **👾 經典 2D 像素風 (`pixel_art`)**：16-bit 點陣像素表情包、懷舊 JRPG 遊戲頭像與表情符號。
6. **🤪 搞笑魔性顏藝 (`meme`)**：誇張五官變形、爆笑肢體動作、草根塗鴉線條、LINE 爆笑迷因感。
7. **🌿 韓系簡約手繪 (`korean_pastel`)**：簡約流暢鋼筆線條、低飽和馬卡龍粉彩色調、溫柔文青插畫。

---

## Stage 3: 表情動作矩陣規劃 (3x3 九宮格)

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

## Stage 4: 調用 Agent 原生 `generate_image` 生圖

Agent 直接呼叫原生 `generate_image` 工具生成 3x3 洋紅底貼圖圖紙：

```json
{
  "AspectRatio": "1:1",
  "ImageName": "sticker_sheet_3x3",
  "ImagePaths": ["/path/to/user_photo.jpg"],
  "Prompt": "A multi-panel sticker sheet containing EXACTLY 9 distinct emoji stickers arranged in a 3x3 grid (3 rows, 3 columns). Faithfully stylized based on the person in the reference photo... [Style prefix]... ABSOLUTE RULES: 1. SOLID FLAT MAGENTA (#FF00FF) background everywhere between cells. 2. Each character centered inside its cell with generous margin. 3. No body parts crossing cell boundaries."
}
```

> 💡 可透過執行 `python scripts/prompt_builder.py --style <風格名>` 快速取得標準最佳化 Prompt。

---

## Stage 5: 本地 Sprite 後製切分與全平台規格化

生圖完成後，直接調用內建的 `sticker_processor.py` 執行切片與包裝：

```bash
python ~/.gemini/config/skills/portrait-sticker-maker/scripts/sticker_processor.py slice \
  --sheet "/path/to/generated_artifact.png" \
  --rows 3 --cols 3 \
  --output-dir "./output_stickers" \
  --border-width 10 \
  --export-packages \
  --montage \
  --labels "嗨！" "OK啦！" "謝謝泥" "笑死！" "嗚嗚嗚" "氣炸！" "愛你唷" "晚安安" "蛤？？"
```

### 自動產出成品：
```
output_stickers/
├── raw_sliced/                     # 9 張透明底、帶實體白邊的獨立貼圖 PNG
├── packages/
│   ├── line_370x320/              # LINE 貼圖官方標準規格 (含 main.png 封面與 tab.png 分頁圖)
│   ├── telegram_discord_512x512/  # Telegram / Discord / WhatsApp 512x512 高清貼圖
│   ├── wechat_240x240/            # 微信表情包規格
│   └── master_hd_1024x1024/       # 1024x1024 超清母檔
└── sticker_montage_preview.png     # 整套 9 入貼圖展示預覽海報
```

---

## 相關參考資源

- [`references/styles.md`](file:///C:/Users/g1060/.gemini/config/skills/portrait-sticker-maker/references/styles.md)：7 大風格 Prompt 配方與視覺範例。
- [`references/expressions.md`](file:///C:/Users/g1060/.gemini/config/skills/portrait-sticker-maker/references/expressions.md)：常用貼圖表情動作庫與中英文對照。
- [`references/specs.md`](file:///C:/Users/g1060/.gemini/config/skills/portrait-sticker-maker/references/specs.md)：LINE、Telegram、Discord、微信貼圖官方規格規範。
