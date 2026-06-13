# Stock Search Chrome Extension

A simple Chrome extension that lets you right-click on any stock symbol and search it on Yahoo Finance.

## Setup

### 1. Generate Icons
Run the icon generation script:
```powershell
python create-icons.py
```

This creates three PNG icons (16x16, 48x48, 128x128) in the `icons/` folder.

### 2. Load in Chrome

1. Open Chrome and go to `chrome://extensions/`
2. Enable **Developer mode** (toggle in top right)
3. Click **Load unpacked**
4. Select this folder (`ChromeExtensionSearchStock`)
5. The extension should appear in your extensions list

### 3. Use It

1. Highlight any stock symbol on any webpage (e.g., "AMZN", "GOOGL", "TSLA")
2. Right-click on the selection
3. Click **"Search Yahoo Finance for [SYMBOL]"**
4. A new tab opens with the Yahoo Finance quote page

## Files

- **manifest.json** — Extension metadata and permissions
- **service-worker.js** — Handles context menu and navigation logic
- **icons/** — Extension icons (created by `create-icons.py`)

## Features

- Works on any webpage
- Auto-converts to uppercase (so "amzn" → "AMZN")
- Opens Yahoo Finance in a new tab

## Future Enhancements

- Add options page for custom financial sites
- Price alerts
- Watchlist persistence
