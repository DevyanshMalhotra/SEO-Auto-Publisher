import os
import sys
from dotenv import load_dotenv
from ebaysdk.merchandising import Connection as MerchConnection
from ebaysdk.exception import ConnectionError

load_dotenv()

USE_SANDBOX      = os.getenv("EBAY_USE_SANDBOX", "false").lower() == "true"
PROD_APP_ID      = os.getenv("EBAY_APP_ID")
SANDBOX_APP_ID   = os.getenv("EBAY_SANDBOX_APP_ID")
APP_ID           = SANDBOX_APP_ID if USE_SANDBOX else PROD_APP_ID
DOMAIN           = "svcs.sandbox.ebay.com" if USE_SANDBOX else "svcs.ebay.com"

if not APP_ID:
    raise RuntimeError("Missing EBAY_APP_ID or EBAY_SANDBOX_APP_ID in .env")

def get_top_products(n=5):
    try:
        api = MerchConnection(appid=APP_ID, config_file=None, domain=DOMAIN)
        response = api.execute('getMostWatchedItems', {'maxResults': n})
        items = response.reply.itemRecommendations.item
        return [
            {"title": item.title, "url": item.viewItemURL}
            for item in items
        ]
    except ConnectionError as e:
        print(f"[eBay Scraper] API Error: {e}", file=sys.stderr)
        return []
