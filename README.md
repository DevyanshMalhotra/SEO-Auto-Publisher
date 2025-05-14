# SEO Auto‑Publisher

A fully automated pipeline that scrapes top‑watched eBay products, generates SEO‑optimized blog paragraphs via Mistral‑7B, and publishes them to your WordPress site every day at 9 UTC.

---

## 🚀 Features

- **eBay Scraping**: Fetch the top 5 most‑watched items on eBay (sandbox or production).  
- **Keyword Research**: Generate 4 SEO‑focused keywords per product using an instruction‑tuned LLM.  
- **Blog Generation**: Write a single 150–200 word engaging paragraph, naturally including your keywords, and ending with a call to action.  
- **WordPress Publishing**: Post directly to WordPress via the modern v2 JSON REST API.  
- **Scheduled Runs**: GitHub Actions workflow triggers every day at 9:00 UTC.  

---

## 📁 Repository Structure

```

seo-auto-publisher/
├── .github/
│   └── workflows/
│       └── schedule.yml          # Daily GitHub Actions pipeline
├── generator/
│   └── blog\_generator.py         # Blog paragraph generation
├── poster/
│   └── wordpress\_poster.py       # JSON‑based WordPress poster
├── scrapers/
│   └── ebay\_scraper.py           # eBay “most watched” scraper
├── seo/
│   └── keyword\_research.py       # SEO keyword suggester
├── main.py                       # Orchestrator script
├── requirements.txt              # Python dependencies
└── README.md                     # This file

````

---

## 🔧 Prerequisites

- Python 3.10+  
- A WordPress.com (or Jetpack‑connected) site  
- eBay Developer account (sandbox & production App IDs)  
- Hugging Face account with an API token  

---

## ⚙️ Configuration

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your‑username/seo‑auto‑publisher.git
   cd seo-auto-publisher
````

2. **Create & fill `.env`**
   Copy `.env.example` to `.env` and set each value:

   ```ini
   HF_TOKEN=hf_xxxYourHfTokenxxx
   EBAY_APP_ID=your_ebay_prod_app_id
   EBAY_SANDBOX_APP_ID=your_ebay_sandbox_app_id
   EBAY_USE_SANDBOX=false
   WORDPRESS_SITE=yourblog.wordpress.com
   WP_COM_TOKEN=your_wp_oauth_token
   ```

3. **Install dependencies**

   ```bash
   python3 -m venv env
   source env/bin/activate        # Linux/macOS
   .\env\Scripts\activate         # Windows
   pip install -r requirements.txt
   ```

---

## ▶️ Running Locally

```bash
python main.py
```

You’ll see console logs like:

```
[Main] Processing: Apple iPhone 13 A2482 128GB Network Unlocked Very Good Condition
[SEO] Keywords: ['iPhone 13 Unlocked', 'Apple iPhone 128GB', 'A2482 Refurbished', 'High Quality Unlocked iPhone']
[Gen] Generated 110 words
[Main] Published: https://seoblogtool5.wordpress.com/2025/05/15/apple-iphone-13-a2482-128gb-network-unlocked-very-good-condition/
```

---

## 🎯 Live Demo & Sample Output URLs

Check out the actual published posts on our demo site:

* [Apple iPhone 13 A2482 128GB Network Unlocked Very Good Condition](https://seoblogtool5.wordpress.com/2025/05/14/apple-iphone-13-a2482-128gb-network-unlocked-very-good-condition-4/)
* [Apple iPhone 6s-16GB 64GB 128GB GSM “Factory Unlocked” AND AT\&T Good Condition](https://seoblogtool5.wordpress.com/2025/05/14/apple-iphone-6s-16gb-64gb-128gb-gsm-factory-unlocked-and-att-good-condition-4/)
* [Apple iPhone 6 Plus-16GB 64GB GSM Factory Unlocked all colors Good Condition](https://seoblogtool5.wordpress.com/2025/05/14/apple-iphone-6-plus-16gb-64gb-gsm-factory-unlocked-all-colors-good-condition-3/)
* [Samsung Galaxy S21 5G 128GB G991U Unlocked - Good](https://seoblogtool5.wordpress.com/2025/05/14/samsung-galaxy-s21-5g-128gb-g991u-unlocked-good-3/)

---

## 📦 Deployment with GitHub Actions

1. **Push your code** to GitHub.
2. **Add secrets** in your repo’s Settings → Secrets:

   * `HF_TOKEN`
   * `EBAY_APP_ID`
   * `EBAY_SANDBOX_APP_ID`
   * `WORDPRESS_SITE`
   * `WP_COM_TOKEN`
3. The workflow at `.github/workflows/schedule.yml` will run daily at 9:00 UTC and publish new posts automatically.

---

## 🧪 Testing

*(Optional)* Add pytest tests in a `/tests` folder to mock:

* eBay SDK responses
* Hugging Face LLM calls
* WordPress API calls

Run:

```bash
pytest --maxfail=1 --disable-warnings -q
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push (`git push origin feat/my-feature`)
5. Open a Pull Request

---

