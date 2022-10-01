# Lake Fs

### Install
```
    docker run --pull always -p 8000:8000 treeverse/lakefs run --local-settings
```
Copy and save access_key_id and secret_access_key


## AWS CLI for LakeFS
And create s3 config for lakefs, where input these secret info

```
    aws configure --profile lakefs
```

First, let's add alias
```
    alias awslfs='aws --endpoint-url http://127.0.0.1:8000/ --profile lakefs'
```

Let's generate sample file
``` 
    mkdir data
    echo "hello world" >> data/sample_file.txt
```

List directory
```
    awslfs s3 ls s3://data-bucket/main/          
```

Copy from a local path to lakeFS
```
    
    awslfs s3 cp data/sample_file.txt s3://data-bucket/main/sample_file.txt
```

Copy from lakeFS to a local path
```
    awslfs s3 cp s3://data-bucket/main/sample_file.txt data/sample_file2.txt
```

Delete file
```
    awslfs s3 rm s3://data-bucket/main/sample_file.txt
```

## Install - Kubernetes

Generate template
```
    helm repo add lakefs https://charts.lakefs.io
    helm template my-lakefs lakefs/lakefs > lakefs-deploy.yaml
```

Deploy lakefs on k8s
```
    kubectl create -f lakefs-deploy.yaml
    kubectl port-forward svc/my-lakefs 5000:80
```
