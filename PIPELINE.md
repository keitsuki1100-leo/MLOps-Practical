# Pipeline Diagram

## DVC Pipeline
```
train.csv → preprocess.py → processed_train.py → train.py → model.txt
                                                              ↓
test.csv  → preprocess.py → processed_test.py → evaluate.py → results
```

## Jenkins Pipeline (Jenkinsfile)
```
Preprocess → Train → Evaluate
```

## Stages:
1. preprocess - cleans data
2. train - trains model
3. evaluate - tests model

## Run Pipeline:
dvc repro