import os
import requests
from dotenv import load_dotenv

load_dotenv()
SITE  = os.getenv("WORDPRESS_SITE")    
TOKEN = os.getenv("WP_COM_TOKEN")      

if not SITE or not TOKEN:
    raise RuntimeError("Please set WORDPRESS_SITE and WP_COM_TOKEN in .env")

# 3. Base URL for WordPress.com REST API v1.1
API_URL = f"https://public-api.wordpress.com/rest/v1.1/sites/{SITE}/posts/new"

def post_to_wordpress(title: str, content: str) -> str:
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    data = {
        "title":   title,           
        "content": content,         
        "status":  "publish"        
    }
    
    res = requests.post(API_URL, headers=headers, data=data)
    res.raise_for_status()         

    json = res.json()
    return json.get("URL") or json.get("ID") or json.get("url") or json.get("ID")
