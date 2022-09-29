# DVC

### Install
```
    brew install dvc
```
### Init dvc
```
    dvc init --subdir
    git commit -m "Initialize DVC"
```
### Add file
```
    touch data/sample_file.txt

    dvc add data/sample_file.txt

    git add data/sample_file.txt.dvc data/.gitignore
    git commit -m "Add raw data"
```

### Add remote
```
    dvc remote add -d myremote /tmp/dvcstore
    dvc push
    dvc pull
    
```

```
    cat .dvc/config

    [core]
        remote = myremote
    ['remote "myremote"']
        url = /tmp/dvcstore
```

### Try modify data
```
    echo "hello world" >> data/sample_file.txt

    dvc add data/sample_file.txt
    git add data/sample_file.txt.dvc
    dvc push
```