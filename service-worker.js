// Create context menu on install
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: 'searchYahooFinance',
    title: 'Search Yahoo Finance for "%s"',
    contexts: ['selection']
  });
});

// Handle context menu click
chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === 'searchYahooFinance') {
    const symbol = info.selectionText.trim().toUpperCase();
    const url = `https://finance.yahoo.com/quote/${symbol}`;
    chrome.tabs.create({ url });
  }
});
