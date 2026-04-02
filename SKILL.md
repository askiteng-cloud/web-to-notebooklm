# Skill: Web-to-Notebook (全自動網頁知識萃取 - 全能交互版)

## 🎯 核心目標
將網頁內容，透過 Jina Reader 物理去噪 -> Fabric-AI 語義萃取 -> 導入 NotebookLM。**過程具備高度交互性，包括本地備份確認與筆記本智能選擇。**

## 🛠️ 依賴工具
- `curl`: 抓取原始 MD。
- `fabric-ai`: 萃取精華 (`extract_wisdom`)。
- `mcp_notebooklm`: 筆記本管理與數據導入。

## 📂 本地存儲配置
- **路徑**: `~/Gemini_Knowledge_Vault/extracted/`
- **邏輯**: 萃取後顯示摘要 -> 詢問備份 (y/n) -> 存儲完成後回報完整路徑。

## 📝 執行邏輯 (Workflow - 終極版)

### 1. 處理流水線
1.  **Fetch (Jina)**: 獲取初步清理的 Markdown。
2.  **Refine (Fabric)**: 調用 `fabric-ai --pattern extract_wisdom` 獲取精華。
3.  **💡 User Choice (Local Backup)**: 
    - 顯示 One-Sentence Takeaway。
    - 詢問：「是否需要將此內容備份至本地知識庫？(y/n)」
    - 若 `y`: 保存並回報路徑。
4.  **💡 User Choice (NotebookLM Ingest)**:
    - **情境 A**: 使用者已指定筆記本 -> 直接導入。
    - **情境 B**: 使用者未指定 -> **主動列出最近 5 個筆記本** 並詢問：「請問要存入哪一個？(請輸入序號或名稱)」。
5.  **Finalize**: 執行上傳並回報「來源已成功加入」。

### 2. 異常處理
- 若抓取失敗 (429/404)，應分析原因並回報，不強行執行後續流程。

## 🗣️ 常用指令範例
- `web-to-notebook，處理 https://example.com。`
- `批量處理 urls.txt 並詢問備份。`
