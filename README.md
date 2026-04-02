# Web-to-NotebookLM (OpenClaw / Gemini CLI Skill)

🚀 **全自動網頁知識萃取與導入工具**

本技能結合了 **Jina Reader (物理去噪)**、**Fabric-AI (語義萃取)** 與 **NotebookLM (雲端知識庫)**，旨在將網頁轉化為結構化的智慧財富。現在已全面適配 **OpenClaw**，支持多渠道（如 Telegram, WhatsApp）交互。

## ✨ 特性
- **極致去噪**：剔除 HTML 代碼、廣告與無關導航。
- **深度萃取**：利用 Fabric-AI 的 `extract_wisdom` 模式，提取摘要、核心觀點與金句。
- **多渠道支持**：完美支持 CLI 與 OpenClaw 多端交互。
- **本地備份**：可選的本地 Markdown 存檔。
- **智能導入**：自動對接 NotebookLM 並提供筆記本列表選擇。

## 📦 安裝步驟
```bash
git clone https://github.com/askiteng-cloud/web-to-notebooklm.git
cd web-to-notebooklm
python install.py
```

## 📖 使用範例
對著您的 Gemini CLI 或 OpenClaw 客戶端（如 Telegram）輸入：
- **基礎模式**：`web-to-notebooklm，處理 https://example.com。`
- **脫水模式 (IM 簡短)**：`脫水 https://mcp.io`
- **指定筆記本**：`處理網址並導入到 我的研究筆記本。`
