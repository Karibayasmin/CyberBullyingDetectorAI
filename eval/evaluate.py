import csv
from pathlib import Path
from agents.classifier_agent import CyberbullyClassifierAgent

BASE_DIR = Path(__file__).resolve().parent.parent

def main():
    agent = CyberbullyClassifierAgent()
    csv_path = BASE_DIR / "data" / "cyberbullying_dataset.csv"

    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            text = row["tweet_text"]
            true_label = row["cyberbullying_type"]

            result = agent.run(text)

            print("\nText:", text)
            print("Dataset label:", true_label)
            print("Agent output:", result)

            if i >= 21:  
                break

if __name__ == "__main__":
    main()
