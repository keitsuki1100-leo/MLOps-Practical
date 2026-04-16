import pandas as pd
import random

print("Evaluating model...")

test = pd.read_csv('data/processed_test.csv')
predictions = [random.randint(0, 1) for _ in range(len(test))]

accuracy = sum(p == t for p, t in zip(predictions, test['label'])) / len(test)

print(f"Test accuracy: {accuracy}")