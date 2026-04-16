# MLOps Practical Project

This is a simple project to learn DVC (Data Version Control).

## Files
- `data/train.csv` - Training data
- `data/test.csv` - Test data
- `models/model.txt` - Trained model

## How to use DVC

```bash
# Track a file
dvc add data/train.csv

# Check status
dvc status

# Push to storage
dvc push
```

## Setup
1. Install DVC: `pip install dvc`
2. Run `dvc init`
3. Add files with `dvc add filename`