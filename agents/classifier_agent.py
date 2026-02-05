# from google.adk.agents.llm_agent import Agent

# Mock tool implementation
# def get_current_time(city: str) -> dict:
#     """Returns the current time in a specified city."""
#     return {"status": "success", "city": city, "time": "10:30 AM"}

# root_agent = Agent(
#     model='gemini-3-flash-preview',
#     name='root_agent',
#     description="Tells the current time in a specified city.",
#     instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
#     tools=[get_current_time],
# )

# Imports (always at the top)
# from google.adk.agents.llm_agent import Agent
# import json

# # Helper functions (definitions only)
# def load_prompt():
#     with open("prompts/cyberbully_classifier.txt", encoding="utf-8") as f:
#         return f.read()

# def safe_parse_json(raw: str) -> dict:
#     try:
#         return json.loads(raw)
#     except Exception:
#         return {
#             "is_cyberbullying": False,
#             "severity": "low",
#             "targeted_categories": [],
#             "explanation": "Invalid model output.",
#             "confidence": 0.0,
#         }

# # Agent class (definition only)
# class CyberbullyClassifierAgent:
#     def __init__(self):
#         self.agent = Agent(
#             model="gemini-3-flash-preview",
#             name="cyberbully_classifier",
#             instruction=load_prompt(),
#         )

#     def run(self, text: str) -> dict:
#         raw = self.agent.run(text)
#         return safe_parse_json(raw)

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


