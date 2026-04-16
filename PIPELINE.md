# Pipeline Diagram

train.csv -> preprocess.py -> processed_train.py -> train.py -> model.txt
                                                              ↓
test.csv  -> preprocess.py -> processed_test.py -> evaluate.py -> results

## Run Pipeline:
dvc repro