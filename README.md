# Webpage-to-Markdown API — Koyeb 部署

## 1. Human 做的事
1. 去 [koyeb.com](https://koyeb.com) 註冊帳號
2. 用 GitHub 登入（fastest）
3. 把 main.py 和 requirements.txt push 到 GitHub repo

## 2. Agent 做的事
拿到 GitHub repo URL 後，其餘部署步驟我可以在 terminal 完成或由你按幾下滑鼠完成：
1. 連 GitHub repo
2. 設定 Build Command: `pip install -r requirements.txt`
3. 設定 Start Command: `uvicorn main:app --host 0.0.0.0 --port 8000`
4. 部署完成

## 預期 URL
`https://webpage-to-markdown-<隨機字串>.koyeb.app`
