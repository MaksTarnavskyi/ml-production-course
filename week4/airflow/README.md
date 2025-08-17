
Deploy airflow on k8s with custom config - to sync dags from git
```
    helm repo add apache-airflow https://airflow.apache.org
    helm upgrade --install airflow apache-airflow/airflow -f k8s/airflow.yaml --namespace airflow
```

Based on [airflow k8s install](https://airflow.apache.org/docs/helm-chart/stable/quick-start.html)

Create volumes
```
    kubectl create -f k8s/airflow-volumes.yaml
```