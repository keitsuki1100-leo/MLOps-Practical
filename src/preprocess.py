import pandas as pd
import yaml

# Load parameters
with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

print("Preprocessing data...")

# Load data
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

# Simple preprocessing - normalize features
for col in ['feature1', 'feature2', 'feature3']:
    max_val = max(train[col].max(), test[col].max())
    train[col] = train[col] / max_val
    test[col] = test[col] / max_val

# Save processed data
train.to_csv('data/processed_train.csv', index=False)
test.to_csv('data/processed_test.csv', index=False)

print(f"Processed {len(train)} training and {len(test)} test samples")
print("Preprocessing complete!")