# Webpage-to-Markdown API — Fly.io

**Live:** https://webpage-to-markdown-api-nmptcw.fly.dev

FastAPI micro-service that converts any URL to clean Markdown.

## API

### GET /health
```bash
curl https://webpage-to-markdown-api-nmptcw.fly.dev/health
# {"status":"ok","version":"1.0.0"}
```

### GET /convert?url=https://...
```bash
curl "https://webpage-to-markdown-api-nmptcw.fly.dev/convert?url=https://example.com"
# {"url":"...","title":"...","markdown":"# Example Domain...","content_length":167}
```

## Tech Stack

| Layer | Choice |
|:------|:-------|
| Runtime | python:3.12-slim (Dockerfile) |
| Framework | FastAPI |
| Dependencies | fastapi[standard], uvicorn, httpx, html2text |
| Port | 8080 (PORT env var) |
| Deploy | Fly.io (Git integration) |
| Repo | zhijiantai/webpage-to-markdown-api |

## Pricing (planned)

- Free tier: 10 calls/month
- Paid: $0.01/call
- Platform: RapidAPI (pending)

## SSRF Warning

`/convert` currently accepts arbitrary URLs. A domain allowlist should be added before public production use.
