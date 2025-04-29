import os
import sys
from dotenv import load_dotenv
from scrapers.ebay_scraper import get_top_products
from seo.keyword_research import get_keywords
from generator.blog_generator import generate_blog
from poster.wordpress_poster import post_to_wordpress

def main():
    load_dotenv()  
    products = get_top_products()
    if not products:
        print("[Main] No products fetched; exiting.")
        return

    for prod in products:
        print(f"[Main] Processing: {prod['title']}")
        kws = get_keywords(prod["title"])
        print(f"[SEO] Keywords: {kws}")
        post = generate_blog(prod, kws)
        print(f"[Gen] Generated {len(post.split())} words")
        url = post_to_wordpress(prod["title"], post)
        print(f"[Main] Published → {url}\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[Error] {e}", file=sys.stderr)
        raise
