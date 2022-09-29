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
    dvc add data/sample_file.txt

    git add data/sample_file.txt.dvc data/.gitignore
    git commit -m "Add raw data"
```