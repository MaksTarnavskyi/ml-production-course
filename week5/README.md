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

Deploy k8s: 

```
    kubectl create -f k8s/app-streamlit.yaml
    kubectl port-forward --address 0.0.0.0 svc/app-streamlit 8080:8080
```

# Fast API

Run locally: 

```
    make build_fast_api
    make run_fast_api
```

Deploy k8s: 

```
    kubectl create -f k8s/app-fastapi.yaml
    kubectl port-forward --address 0.0.0.0 svc/app-fastapi 8080:8080
```

Run tests
```
    python -m pytest tests/
```
# Seldon 

## Install with helm

```
    kubectl apply -f https://github.com/datawire/ambassador-operator/releases/latest/download/ambassador-operator-crds.yaml
    kubectl apply -n ambassador -f https://github.com/datawire/ambassador-operator/releases/latest/download/ambassador-operator-kind.yaml
    kubectl wait --timeout=180s -n ambassador --for=condition=deployed ambassadorinstallations/ambassador

    kubectl create namespace seldon-system

    helm install seldon-core seldon-core-operator \
        --repo https://storage.googleapis.com/seldon-charts \
        --set usageMetrics.enabled=true \
        --set ambassador.enabled=true \
        --namespace seldon-system
```

## Port forward 

```
    kubectl port-forward  --address 0.0.0.0 -n ambassador svc/ambassador 7777:80
```

## Custom example
```
    kubectl create -f k8s/seldon-custom.yaml

    open http://0.0.0.0:7777/seldon/default/nlp-sample/api/v1.0/doc/#/
    { "data": { "ndarray": ["this is an example"] } }


    curl -X POST "http://0.0.0.0:7777/seldon/default/nlp-sample/api/v1.0/predictions" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":{\"ndarray\":[\"this is an example\"]}}"

```

