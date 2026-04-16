import pandas as pd
import random

print("Training model...")

train = pd.read_csv('data/processed_train.csv')
random.seed(42)

weights = {col: random.random() for col in ['feature1', 'feature2', 'feature3']}

predictions = []
for _, row in train.iterrows():
    score = sum(row[col] * weights[col] for col in weights)
    predictions.append(1 if score > 0.5 else 0)

accuracy = sum(p == t for p, t in zip(predictions, train['label'])) / len(train)

with open('models/model.txt', 'w') as f:
    f.write(f"accuracy: {accuracy}\n")

print(f"Training done. Accuracy: {accuracy}")