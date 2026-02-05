from dotenv import load_dotenv
load_dotenv()

from agents.classifier_agent import CyberbullyClassifierAgent

if __name__ == "__main__":
    agent = CyberbullyClassifierAgent()
    result = agent.run("You are useless old man")
    print(result)
