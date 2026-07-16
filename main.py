"""
webpage-to-markdown API — FastAPI + httpx + html2text
Usage: GET /convert?url=https://example.com → {"markdown": "...", "title": "..."}
"""
from fastapi import FastAPI, Query, HTTPException
import httpx
import html2text
import re
from urllib.parse import urlparse

app = FastAPI(title="Webpage to Markdown API", version="1.0.0")

@app.get("/convert")
async def convert(url: str = Query(..., description="URL to convert")):
    # Validate URL
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        raise HTTPException(status_code=400, detail="Invalid URL")
    
    try:
        async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
            resp = await client.get(url, headers={
                "User-Agent": "Mozilla/5.0 (compatible; WebpageToMarkdown/1.0)"
            })
            resp.raise_for_status()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch URL: {str(e)}")
    
    html = resp.text
    
    # Extract title
    title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else ""
    
    # Convert HTML to Markdown
    converter = html2text.HTML2Text()
    converter.body_width = 0  # no line wrapping
    converter.ignore_links = False
    converter.ignore_images = False
    converter.ignore_emphasis = False
    converter.skip_internal_links = True
    markdown = converter.handle(html)
    
    return {
        "url": url,
        "title": title,
        "markdown": markdown.strip(),
        "content_length": len(markdown.strip())
    }

@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
