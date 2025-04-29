import time
import random
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from huggingface_hub.utils import HfHubHTTPError
import re

load_dotenv()
hf_token = os.getenv("HF_TOKEN", None)

MODEL = "mistralai/Mistral-7B-Instruct-v0.3"

client = InferenceClient(token=hf_token)

def generate_blog(product: dict, keywords: list[str]) -> str:
    prompt = (
        "You are an expert SEO content writer. "
        "Write exactly one engaging 150–200 word paragraph about “"
        f"{product['title']}” in fluent, persuasive prose, "
        f"naturally including these keywords: {', '.join(keywords)}. "
        "Do not repeat the product title, dates, or internal instructions. "
        "Conclude with a concise call to action like “Read the full review on our blog now!”."
    )

    max_retries = 2
    base_delay  = 1.0

    for attempt in range(1, max_retries + 1):
        try:
            print(f"[Gen] {MODEL}, attempt {attempt}")
            response = client.text_generation(
                model=MODEL,
                prompt=prompt,
                max_new_tokens=200,
                temperature=0.6
            )
            text = getattr(response, "generated_text", str(response)).strip()

            if text and text[-1] not in ".?!":
                idx = max(
                    text.rfind("."),   
                    text.rfind("?"),   
                    text.rfind("!")    
                )
                if idx != -1:
                    text = text[:idx+1]  

            return text

        except HfHubHTTPError as e:
            status = getattr(e.response, "status_code", None)
            if status == 503:
                delay = (base_delay * (2 ** (attempt - 1))) + random.uniform(0, 0.1)
                print(f"[Gen] 503 received; retrying in {delay:.1f}s")
                time.sleep(delay)  
                continue
            raise

    raise RuntimeError("Text generation failed!")
