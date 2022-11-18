# Setup 

Create kind cluster with specific version

```
kind create cluster --name ml-week-5  --image=kindest/node:v1.21.2 --config=k8s/kind-cluster.yaml
```

For local testing
```
    export WANDB_API_KEY=******************
```

## Streamlit

Run localy
```
    make build_app_streamlit
    make run_app_streamlit
```
