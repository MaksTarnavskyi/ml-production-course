## Local deployment of Kubeflow Pipelines

```
    kind create cluster --name week-4

    export PIPELINE_VERSION=1.8.5
    kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
    kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
    kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"

    kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
```