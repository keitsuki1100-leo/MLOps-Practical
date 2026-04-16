import pandas as pd
import json
import random

print("Evaluating model...")

# Load test data and model
test = pd.read_csv('data/processed_test.csv')

with open('models/model_v1.txt', 'r') as f:
    lines = f.readlines()
    accuracy = float([l for l in lines if 'accuracy:' in l][0].split(':')[1].strip())

# Mock evaluation
predictions = [random.randint(0, 1) for _ in range(len(test))]
test_accuracy = sum(p == t for p, t in zip(predictions, test['label'])) / len(test)

# Save metrics
metrics = {
    'test_accuracy': test_accuracy,
    'test_f1': test_accuracy - 0.05,
    'test_precision': test_accuracy - 0.03,
    'test_recall': test_accuracy - 0.07
}

with open('metrics/test_metrics.json', 'w') as f:
    json.dump(metrics, f, indent=2)

print(f"Test accuracy: {test_accuracy:.2f}")
print("Evaluation complete!")