## Local deployment of Kubeflow Pipelines

Create cluster
```
    kind create cluster --name week-4
```

Create directly
```
    export PIPELINE_VERSION=1.8.5
    kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
    kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
    kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
```

Create yaml and applay with kubectl
```
    export PIPELINE_VERSION=1.8.5
    kubectl kustomize "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION" > k8s/kfp.yaml
    kubectl create -f k8s/kfp.yaml

    kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io

    kubectl kustomize "github.com/kubeflow/pipelines/manifests/kustomize/env/dev?ref=$PIPELINE_VERSION" > k8s/pipelines.yaml
    kubectl create -f k8s/pipelines.yaml
```

Access UI and minio
```
    kubectl port-forward --address=0.0.0.0 svc/minio-service 9000:9000 -n kubeflow
    kubectl port-forward --address=0.0.0.0 svc/ml-pipeline-ui 8888:80 -n kubeflow

    kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
```

## Create pipelines

Setup env variables 

```
export WANDB_PROJECT=nlp-sample
export WANDB_API_KEY=****************
```


Training pipeline

```
python pipelines/kfp-training-pipeline.py http://0.0.0.0:8080
python pipelines/kfp-inference-pipeline.py http://0.0.0.0:8080
```
