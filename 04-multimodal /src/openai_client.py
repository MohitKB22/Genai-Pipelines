from typing import Any, Dict
import openai
import os

class OpenAIClient:
    def __init__(self):
        self.api_key = os.getenv("https://platform.openai.com/api-keys)")
        openai.api_key = self.api_key

    def generate_response(self, prompt: str, model: str = "gpt-3.5-turbo", max_tokens: int = 150) -> Dict[str, Any]:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        return response.choices[0].message['content']