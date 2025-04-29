from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()
hf_token = os.getenv("HF_TOKEN", None)

hf_client = InferenceClient(
    model="google/flan-t5-large",  
    token=hf_token                
)

def get_keywords(product_name: str, count: int = 4) -> list[str]:
    prompt = (
        f"Suggest {count} SEO-focused keywords for a blog post about "
        f"'{product_name}'. Return only the keywords separated by commas."
    )
    response = hf_client.text_generation(
        prompt=prompt,
        max_new_tokens=50,
        temperature=0.3
    )  

    text = getattr(response, "generated_text", str(response))
    return [kw.strip() for kw in text.split(",") if kw.strip()][:count]
