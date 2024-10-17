from duckduckgo_search import DDGS
from components.prompt import get_prompt
from components.data import get_data
import re

def get_response(prompt_text):
    results = DDGS().chat(prompt_text)
    return results

def extract_output(response):
    match = re.search(r'<output>(.*?)</output>', response, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return "Ответ не содержит тега <output>"