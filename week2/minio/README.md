# Setup

Create/delete cluster
```
    kind create cluster --name week-2
    kind delete cluster --name week-2
```

Install minio on k8s
```
    kubectl create -f k8s/minio-pvc.yaml
    kubectl create -f k8s/minio-deployment.yaml
    kubectl create -f k8s/minio-service.yaml

    kubectl get svc minio-ui
    kubectl get svc minio-api

    kubectl port-forward svc/minio-api 9000:9000
    kubectl port-forward svc/minio-ui 9001:9001
```

Local testing
```
    python3 -m venv venv-minio
    source venv-minio/bin/activate

    pip install -r requirements.txt

    python -m pytest tests/ 
```

Docker
```
    docker build -t maksymtarnavskyi/minio-app:latest .
```

