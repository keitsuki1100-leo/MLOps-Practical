import pandas as pd

print("Preprocessing data...")

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

for col in ['feature1', 'feature2', 'feature3']:
    max_val = max(train[col].max(), test[col].max())
    train[col] = train[col] / max_val
    test[col] = test[col] / max_val

train.to_csv('data/processed_train.csv', index=False)
test.to_csv('data/processed_test.csv', index=False)

print("Done")