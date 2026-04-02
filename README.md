# Web-to-Notebook Skill (Gemini CLI)

🚀 **全自動網頁知識萃取與導入工具**

本技能結合了 **Jina Reader (物理去噪)**、**Fabric-AI (語義萃取)** 與 **NotebookLM (雲端知識庫)**，旨在將混亂的網頁轉化為結構化的智慧財富。

## ✨ 特性
- **極致去噪**：剔除 HTML 代碼、廣告與無關導航。
- **深度萃取**：利用 Fabric-AI 的 `extract_wisdom` 模式，提取摘要、核心觀點與金句。
- **本地備份**：可選的本地 Markdown 存檔功能。
- **智能導入**：自動對接 NotebookLM 並提供筆記本智能選擇。

## 🛠️ 安裝要求
1. **Gemini CLI**: 核心運行環境。
2. **Fabric-AI**: 建議使用 `pipx install fabric-ai`。
3. **Curl**: 用於數據抓取。

## 📦 安裝步驟
克隆倉庫並運行安裝腳本：
```bash
git clone https://github.com/askiteng-cloud/web-to-notebook-skill.git
cd web-to-notebook-skill
python install.py
```

## 📖 使用範例
對著您的 Gemini CLI 輸入以下指令：
- **基礎模式**：`處理 https://example.com。`
- **指定筆記本**：`處理網址並導入到 我的研究筆記本。`
- **批量處理**：`處理 urls.txt 並詢問備份。`

## 📂 本地知識庫
所有手動備份的內容將存儲於：`~/Gemini_Knowledge_Vault/extracted/`

---
⚡ 由 **askiteng-cloud** 提供技術支持
