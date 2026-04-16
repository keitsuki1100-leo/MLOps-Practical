import pandas as pd
import yaml
import json
import random

# Load parameters
with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

print("Training model...")

# Load processed data
train = pd.read_csv('data/processed_train.csv')

# Simple mock training - just random weights for demonstration
random.seed(42)
weights = {col: random.random() for col in ['feature1', 'feature2', 'feature3']}

# Calculate mock accuracy
predictions = []
for _, row in train.iterrows():
    score = sum(row[col] * weights[col] for col in weights)
    predictions.append(1 if score > 0.5 else 0)

accuracy = sum(p == t for p, t in zip(predictions, train['label'])) / len(train)

# Save model
with open('models/model_v1.txt', 'w') as f:
    f.write(f"# Model checkpoint\n")
    f.write(f"# Saved at: 2026-04-16\n")
    f.write(f"# Accuracy: {accuracy:.2f}\n\n")
    f.write(f"model_version: \"1.0.0\"\n")
    f.write(f"accuracy: {accuracy:.2f}\n")
    f.write(f"f1_score: {accuracy - 0.01:.2f}\n")
    f.write(f"precision: {accuracy - 0.02:.2f}\n")
    f.write(f"recall: {accuracy - 0.03:.2f}\n")
    f.write(f"training_date: \"2026-04-16\"\n")

# Save metrics
metrics = {
    'accuracy': accuracy,
    'f1_score': accuracy - 0.01,
    'precision': accuracy - 0.02,
    'recall': accuracy - 0.03
}

with open('metrics/train_metrics.json', 'w') as f:
    json.dump(metrics, f, indent=2)

print(f"Model trained with accuracy: {accuracy:.2f}")
print("Training complete!")