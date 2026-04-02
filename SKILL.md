# Skill: Web-to-NotebookLM (全自動網頁知識萃取 - OpenClaw 多端適配版)

## 🎯 核心目標
將網頁內容，透過 Jina Reader 物理去噪 -> Fabric-AI 語義萃取 -> 導入 NotebookLM。**支持多渠道交互（CLI/IM），具備本地備份確認與筆記本智能選擇。**

## 🛠️ 依賴工具
- `curl`: 抓取原始 Markdown。
- `fabric-ai`: 語義萃取 (`extract_wisdom`)。
- `mcp_notebooklm`: 筆記本管理與數據導入。

## 📂 存儲配置 (Path)
- **技能路徑**: `~/.openclaw/skills/web-to-notebooklm/`
- **本地庫路徑**: `~/Gemini_Knowledge_Vault/extracted/`

## 📝 執行邏輯 (Workflow - OpenClaw 專用版)

### 1. 處理流水線
1.  **Fetch (Jina)**: 獲取初步清理的 Markdown (Jina Reader)。
2.  **Refine (Fabric)**: 調用 `fabric-ai --pattern extract_wisdom` 獲取精華。
3.  **💡 User Choice (Local Backup)**: 
    - 顯示 One-Sentence Takeaway。
    - 詢問：「是否需要將此內容備份至本地知識庫？(y/n)」。
    - 若 `y`: 保存至 `~/Gemini_Knowledge_Vault/extracted/` 並回報完整路徑。
4.  **💡 User Choice (NotebookLM Ingest)**:
    - **情境 A**: 已指定筆記本 -> 直接導入。
    - **情境 B**: 未指定 -> **主動列出最近 5 個筆記本** 並詢問：「請問要存入哪一個？(請輸入序號或名稱)」。
5.  **Finalize**: 執行雲端上傳並回報「來源已成功加入」。

### 2. 多端交互優化 (IM Support)
- 若來自 Telegram/WhatsApp：自動縮短摘要長度，避免過長消息。
- 默認備份策略：IM 模式下可配置為自動備份並提供 Markdown 檔案下載連結。

## 🗣️ 常用指令範例
- `web-to-notebooklm，處理 https://example.com。`
- `處理網址並導入到 我的研究筆記本。`
- `脫水 https://mcp.io` (IM 簡短指令)

