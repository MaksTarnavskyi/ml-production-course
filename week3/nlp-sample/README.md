# Text quality model based on legendary NLP-sample

### Setup

First docker build
```
    make build
```

Then open docker in dev mode and there run training
```
    make run_dev
```

First, lest's run tests
```
    make format
    make lint
    make test_all
```


Inside docker dev mode
```
    export PYTHONPATH=.
    export WANDB_PROJECT=nlp-sample
    export WANDB_API_KEY=****************
```
And then for training
```
    make train_example
    make train_fast
```

Look report
```
    open https://wandb.ai/maksym-tarnavskyi/nlp-sample
```

### Data
(CoLA)[https://nyu-mll.github.io/CoLA/] (Corpus of Linguistic Acceptability) is a dataset containing sentences labeled grammatically correct or not.

