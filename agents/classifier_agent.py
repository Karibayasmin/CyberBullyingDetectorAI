from google.adk.agents.llm_agent import Agent
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # project root

def load_prompt():
    prompt_path = BASE_DIR / "prompts" / "cyberbully_classifier.txt"
    return prompt_path.read_text(encoding="utf-8")

def safe_parse_json(raw) -> dict:
    if isinstance(raw, dict):
        return raw
    try:
        return json.loads(raw)
    except Exception:
        return {
            "is_cyberbullying": False,
            "severity": "low",
            "targeted_categories": [],
            "explanation": "Invalid model output.",
            "confidence": 0.0,
        }

class CyberbullyClassifierAgent:
    def __init__(self):
        self.agent = Agent(
            model="gemini-3-flash-preview",
            name="cyberbully_classifier",
            instruction=load_prompt(),
        )

    def run(self, text: str) -> dict:
        raw = self.agent.run(text)
        return safe_parse_json(raw)


