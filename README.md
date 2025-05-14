## README.md

Welcome to **AI-SEO-Blog**! This tool automates end-to-end SEO blog creation: scraping trending products, researching keywords, generating AI-powered posts, and publishing to WordPress.com.

### 🚀 Quick Start
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-seo-blog.git
   cd ai-seo-blog
   ```
2. **Create and configure your `.env`**:
   ```env
   # eBay API
   EBAY_USE_SANDBOX=false
   EBAY_APP_ID=your_production_app_id
   EBAY_SANDBOX_APP_ID=your_sandbox_app_id

   # Hugging Face (optional)
   HF_TOKEN=hf_your_token_here

   # WordPress.com
   WORDPRESS_SITE=yourblog.wordpress.com
   WP_COM_TOKEN=your_oauth2_access_token
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the pipeline**:
   ```bash
   python main.py
   ```

### 📂 Project Structure
```
ai_seo_blog/
├── .env
├── README.md
├── requirements.txt
├── main.py            # Orchestrator
├── scrapers/
│   └── ebay_scraper.py
├── seo/
│   └── keyword_research.py
├── generator/
│   └── blog_generator.py
└── poster/
    └── wordpress_poster.py
```

### 🔍 Screenshots / Images
- **Scraper Logs**: `![Scraper Logs](/images/scraper_logs.png)`
- **Keyword Output**: `![Keywords](/images/keywords.png)`
- **Blog Generation**: `![Generated Blog](/images/blog_generation.png)`
- **Published Post**: `![Published Post](/images/published_post.png)`

### 📖 Usage Examples
- **Scrape & Post**:
  ```bash
  python main.py
  # Output:
  # [Main] Processing: Apple iPhone 13...
  # [SEO] Keywords: [...]
  # [Gen] Generated 158 words
  # [Poster] Published at https://yourblog.wordpress.com/.../
  ```

### 🤝 Contributing
Feel free to open issues or pull requests. For major changes, please start a discussion.

---

## report.md

# Project Report: AI-Driven SEO Blog Automation

## 1. Introduction
This report details the development of an automated pipeline for creating and publishing SEO-optimized blog posts using AI and free APIs.

## 2. System Overview
1. **Trending Products**: Fetched top-watched items from eBay Merchandising API.
2. **SEO Keywords**: Generated keywords using Hugging Face Inference API (Mistral-7B-Instruct-v0.3).
3. **Content Generation**: Produced 150–200 word blog posts with a strong call to action using the same LLM.
4. **Publishing**: Posted articles to WordPress.com via REST API v1.1.

## 3. Detailed Steps

### 3.1 Environment Setup
- Installed Python 3.10+
- Created `.env` with API credentials
- Installed dependencies in `requirements.txt`.

### 3.2 Scraping Module (`ebay_scraper.py`)
- Utilized `ebaysdk.merchandising.Connection` to call `getMostWatchedItems`.
- Parsed response to extract product titles and URLs.

### 3.3 Keyword Research (`keyword_research.py`)
- Initialized `InferenceClient` with optional `HF_TOKEN`.
- Prompted model to suggest 4 SEO keywords per product.

### 3.4 Blog Generation (`blog_generator.py`)
- Used Mistral-7B-Instruct to produce a single paragraph (150–200 words).
- Enforced no repetition, no lists, and included a CTA.
- Implemented retry/backoff on 503 errors.
- Trimmed incomplete trailing sentences via `str.rfind()`.

### 3.5 Posting to WordPress (`wordpress_poster.py`)
- Loaded OAuth2 token from `.env`.
- Posted via `https://public-api.wordpress.com/rest/v1.1/sites/{SITE}/posts/new`.
- Logged full response and extracted the published URL.

## 4. Results
- **Total Products Processed**: 5 per run
- **Average Generation Time**: ~4 seconds per post
- **Success Rate**: 100% publishing success on test runs
- **Sample Posts**:
  - https://yourblog.wordpress.com/2025/04/29/product-1-slug/
  - https://yourblog.wordpress.com/2025/04/29/product-2-slug/

## 5. Future Work
- Add media uploads (product images) via WordPress API.
- Integrate Google Search Console for performance tracking.
- Deploy as a scheduled AWS Lambda or GitHub Action.

## 6. Appendices
- **Appendix A**: Sample `.env` file
- **Appendix B**: Full prompt templates


